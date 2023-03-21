# -*- coding:utf-8 -*-
from __future__ import annotations
from typing import TYPE_CHECKING, List

import logging
import json
import os
import requests
import urllib3

from tqdm import tqdm
import colorama
from duckduckgo_search import ddg
import asyncio
import aiohttp

from presets import *
from llama_func import *
from utils import *

# logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] [%(filename)s:%(lineno)d] %(message)s")

if TYPE_CHECKING:
    from typing import TypedDict

    class DataframeData(TypedDict):
        headers: List[str]
        data: List[List[str | int | bool]]


initial_prompt = "You are a helpful assistant."
API_URL = "https://api.openai.com/v1/chat/completions"
HISTORY_DIR = "history"
TEMPLATES_DIR = "templates"

def get_response(
    openai_api_key, system_prompt, history, temperature, top_p, stream, selected_model
):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai_api_key}",
    }

    history = [construct_system(system_prompt), *history]

    payload = {
        "model": selected_model,
        "messages": history,  # [{"role": "user", "content": f"{inputs}"}],
        "temperature": temperature,  # 1.0,
        "top_p": top_p,  # 1.0,
        "n": 1,
        "stream": stream,
        "presence_penalty": 0,
        "frequency_penalty": 0,
    }
    if stream:
        timeout = timeout_streaming
    else:
        timeout = timeout_all

    # Get the proxy settings in environment variables
    http_proxy = os.environ.get("HTTP_PROXY") or os.environ.get("http_proxy")
    https_proxy = os.environ.get("HTTPS_PROXY") or os.environ.get("https_proxy")

    # If proxy settings exist, use them
    proxies = {}
    if http_proxy:
        logging.info(f"Using HTTP proxy: {http_proxy}")
        proxies["http"] = http_proxy
    if https_proxy:
        logging.info(f"Using HTTPS proxy: {https_proxy}")
        proxies["https"] = https_proxy

    # If there is a proxy, use the proxy to send the request, otherwise use the default settings to send the request
    if proxies:
        response = requests.post(
            API_URL,
            headers=headers,
            json=payload,
            stream=True,
            timeout=timeout,
            proxies=proxies,
        )
    else:
        response = requests.post(
            API_URL,
            headers=headers,
            json=payload,
            stream=True,
            timeout=timeout,
        )
    return response


def stream_predict(
    openai_api_key,
    system_prompt,
    history,
    inputs,
    chatbot,
    all_token_counts,
    top_p,
    temperature,
    selected_model,
    fake_input=None,
    display_append=""
):
    def get_return_value():
        return chatbot, history, status_text, all_token_counts

    logging.info("Real-time answer mode")
    partial_words = ""
    counter = 0
    status_text = "Starting real-time transmission of answers to ......"
    history.append(construct_user(inputs))
    history.append(construct_assistant(""))
    if fake_input:
        chatbot.append((fake_input, ""))
    else:
        chatbot.append((inputs, ""))
    user_token_count = 0
    if len(all_token_counts) == 0:
        system_prompt_token_count = count_token(construct_system(system_prompt))
        user_token_count = (
            count_token(construct_user(inputs)) + system_prompt_token_count
        )
    else:
        user_token_count = count_token(construct_user(inputs))
    all_token_counts.append(user_token_count)
    logging.info(f "Input token count: {user_token_count}")
    yield get_return_value()
    try:
        response = get_response(
            openai_api_key,
            system_prompt,
            history,
            temperature,
            top_p,
            True,
            selected_model,
        )
    except requests.exceptions.ConnectTimeout:
        status_text = (
            standard_error_msg + connection_timeout_prompt + error_retrieve_prompt
        )
        yield get_return_value()
        return
    except requests.exceptions.ReadTimeout:
        status_text = standard_error_msg + read_timeout_prompt + error_retrieve_prompt
        yield get_return_value()
        return

    yield get_return_value()
    error_json_str = ""

    for chunk in tqdm(response.iter_lines()):
        if counter == 0:
            counter += 1
            continue
        counter += 1
        # check whether each line is non-empty
        if chunk:
            chunk = chunk.decode()
            chunklength = len(chunk)
            try:
                chunk = json.loads(chunk[6:])
            except json.JSONDecodeError:
                logging.info(chunk)
                error_json_str += chunk
                status_text = f "JSON parsing error. Please reset the conversation. Received: {error_json_str}"
                yield get_return_value()
                continue
            # decode each line as response data is in bytes
            if chunklength > 6 and "delta" in chunk["choices"][0]:
                finish_reason = chunk["choices"][0]["finish_reason"]
                status_text = construct_token_message(
                    sum(all_token_counts), stream=True
                )
                if finish_reason == "stop":
                    yield get_return_value()
                    break
                try:
                    partial_words = (
                        partial_words + chunk["choices"][0]["delta"]["content"]
                    )
                except KeyError:
                    status_text = (
                        standard_error_msg
                        + "Content not found in API reply. It is likely that the Token count has reached the upper limit. Please reset the conversation. Current Token Count: "
                        + str(sum(all_token_counts))
                    )
                    yield get_return_value()
                    break
                history[-1] = construct_assistant(partial_words)
                chatbot[-1] = (chatbot[-1][0], partial_words+display_append)
                all_token_counts[-1] += 1
                yield get_return_value()


def predict_all(
    openai_api_key,
    system_prompt,
    history,
    inputs,
    chatbot,
    all_token_counts,
    top_p,
    temperature,
    selected_model,
    fake_input=None,
    display_append=""
):
    logging.info("One-time answer mode")
    history.append(construct_user(inputs))
    history.append(construct_assistant(""))
    if fake_input:
        chatbot.append((fake_input, ""))
    else:
        chatbot.append((inputs, ""))
    all_token_counts.append(count_token(construct_user(inputs)))
    try:
        response = get_response(
            openai_api_key,
            system_prompt,
            history,
            temperature,
            top_p,
            False,
            selected_model,
        )
    except requests.exceptions.ConnectTimeout:
        status_text = (
            standard_error_msg + connection_timeout_prompt + error_retrieve_prompt
        )
        return chatbot, history, status_text, all_token_counts
    except requests.exceptions.ProxyError:
        status_text = standard_error_msg + proxy_error_prompt + error_retrieve_prompt
        return chatbot, history, status_text, all_token_counts
    except requests.exceptions.SSLError:
        status_text = standard_error_msg + ssl_error_prompt + error_retrieve_prompt
        return chatbot, history, status_text, all_token_counts
    response = json.loads(response.text)
    content = response["choices"][0]["message"]["content"]
    history[-1] = construct_assistant(content)
    chatbot[-1] = (chatbot[-1][0], content+display_append)
    total_token_count = response["usage"]["total_tokens"]
    all_token_counts[-1] = total_token_count - sum(all_token_counts)
    status_text = construct_token_message(total_token_count)
    return chatbot, history, status_text, all_token_counts


def predict(
    openai_api_key,
    system_prompt,
    history,
    inputs,
    chatbot,
    all_token_counts,
    top_p,
    temperature,
    stream=False,
    selected_model=MODELS[0],
    use_websearch=False,
    files = None,
    should_check_token_count=True,
):  # repetition_penalty, top_k
    logging.info("输入为：" + colorama.Fore.BLUE + f"{inputs}" + colorama.Style.RESET_ALL)
    if files:
        msg = "Building index in ...... (this may take a bit longer)"
        logging.info(msg)
        yield chatbot, history, msg, all_token_counts
        index = construct_index(openai_api_key, file_src=files)
        msg = "Index build complete, fetching answer in ......"
        yield chatbot, history, msg, all_token_counts
        history, chatbot, status_text = chat_ai(openai_api_key, index, inputs, history, chatbot)
        yield chatbot, history, status_text, all_token_counts
        return

    old_inputs = ""
    link_references = []
    if use_websearch:
        search_results = ddg(inputs, max_results=5)
        old_inputs = inputs
        web_results = []
        for idx, result in enumerate(search_results):
            logging.info(f "Search result {idx + 1}: {result}")
            domain_name = urllib3.util.parse_url(result["href"]).host
            web_results.append(f'[{idx+1}]"{result["body"]}"\nURL: {result["href"]}')
            link_references.append(f"{idx+1}. [{domain_name}]({result['href']})\n")
        link_references = "\n\n" + "".join(link_references)
        inputs = (
            replace_today(WEBSEARCH_PTOMPT_TEMPLATE)
            .replace("{query}", inputs)
            .replace("{web_results}", "\n\n".join(web_results))
        )
    else:
        link_references = ""

    if len(openai_api_key) != 51:
        status_text = standard_error_msg + no_apikey_msg
        logging.info(status_text)
        chatbot.append((inputs, ""))
        if len(history) == 0:
            history.append(construct_user(inputs))
            history.append("")
            all_token_counts.append(0)
        else:
            history[-2] = construct_user(inputs)
        yield chatbot, history, status_text, all_token_counts
        return

    yield chatbot, history, "Start generating answers to ......", all_token_counts

    if stream:
        logging.info("Using streaming")
        iter = stream_predict(
            openai_api_key,
            system_prompt,
            history,
            inputs,
            chatbot,
            all_token_counts,
            top_p,
            temperature,
            selected_model,
            fake_input=old_inputs,
            display_append=link_references
        )
        for chatbot, history, status_text, all_token_counts in iter:
            yield chatbot, history, status_text, all_token_counts
    else:
        logging.info("Not using streaming")
        chatbot, history, status_text, all_token_counts = predict_all(
            openai_api_key,
            system_prompt,
            history,
            inputs,
            chatbot,
            all_token_counts,
            top_p,
            temperature,
            selected_model,
            fake_input=old_inputs,
            display_append=link_references
        )
        yield chatbot, history, status_text, all_token_counts

    logging.info(f "Transfer completed. Current token count is {all_token_counts}")
    if len(history) > 1 and history[-1]["content"] != inputs:
        logging.info(
            "The answer is:"
            + colorama.Fore.BLUE
            + f"{history[-1]['content']}"
            + colorama.Style.RESET_ALL
        )

    if stream:
        max_token = max_token_streaming
    else:
        max_token = max_token_all

    if sum(all_token_counts) > max_token and should_check_token_count:
        status_text = f "streamline token in {all_token_counts}/{max_token}"
        logging.info(status_text)
        yield chatbot, history, status_text, all_token_counts
        iter = reduce_token_size(
            openai_api_key,
            system_prompt,
            history,
            chatbot,
            all_token_counts,
            top_p,
            temperature,
            stream=False,
            selected_model=selected_model,
            hidden=True,
        )
        for chatbot, history, status_text, all_token_counts in iter:
            status_text = f "Token reached limit, Token count has been automatically reduced to {status_text}"
            yield chatbot, history, status_text, all_token_counts


def retry(
    openai_api_key,
    system_prompt,
    history,
    chatbot,
    token_count,
    top_p,
    temperature,
    stream=False,
    selected_model=MODELS[0],
):
    logging.info("Retry in progress ......")
    if len(history) == 0:
        yield chatbot, history, f"{standard_error_msg} context is empty", token_count
        return
    history.pop()
    inputs = history.pop()["content"]
    token_count.pop()
    iter = predict(
        openai_api_key,
        system_prompt,
        history,
        inputs,
        chatbot,
        token_count,
        top_p,
        temperature,
        stream=stream,
        selected_model=selected_model,
    )
    logging.info("Retry completed")
    for x in iter:
        yield x


def reduce_token_size(
    openai_api_key,
    system_prompt,
    history,
    chatbot,
    token_count,
    top_p,
    temperature,
    stream=False,
    selected_model=MODELS[0],
    hidden=False,
):
    logging.info("Starting to reduce the number of tokens ......")
    iter = predict(
        openai_api_key,
        system_prompt,
        history,
        summarize_prompt,
        chatbot,
        token_count,
        top_p,
        temperature,
        stream=stream,
        selected_model=selected_model,
        should_check_token_count=False,
    )
    logging.info(f"chatbot: {chatbot}")
    for chatbot, history, status_text, previous_token_count in iter:
        history = history[-2:]
        token_count = previous_token_count[-1:]
        if hidden:
            chatbot.pop()
        yield chatbot, history, construct_token_message(
            sum(token_count), stream=stream
        ), token_count
    logging.info("Reducing the number of tokens is complete")
