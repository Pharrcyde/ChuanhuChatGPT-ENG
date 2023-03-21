# -*- coding:utf-8 -*-
from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable, Dict, List, Tuple, Type
import logging
import json
import os
import datetime
import hashlib
import csv
import requests
import re

import gradio as gr
from pypinyin import lazy_pinyin
import tiktoken
import mdtex2html
from markdown import markdown
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

from presets import *

# logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] [%(filename)s:%(lineno)d] %(message)s")

if TYPE_CHECKING:
    from typing import TypedDict

    class DataframeData(TypedDict):
        headers: List[str]
        data: List[List[str | int | bool]]


def count_token(message):
    encoding = tiktoken.get_encoding("cl100k_base")
    input_str = f"role: {message['role']}, content: {message['content']}"
    length = len(encoding.encode(input_str))
    return length

def markdown_to_html_with_syntax_highlight(md_str):
    def replacer(match):
        lang = match.group(1) or 'text'
        code = match.group(2)

        try:
            lexer = get_lexer_by_name(lang, stripall=True)
        except ValueError:
            lexer = get_lexer_by_name("text", stripall=True)

        formatter = HtmlFormatter()
        highlighted_code = highlight(code, lexer, formatter)

        return f"<pre><code class=\"{lang}\">{highlighted_code}</code></pre>"

    code_block_pattern = r'```(\w+)?\n([\s\S]+?)\n```'
    md_str = re.sub(code_block_pattern, replacer, md_str, flags=re.MULTILINE)

    html_str = markdown(md_str)
    return html_str

def normalize_markdown(md_text: str) -> str:
    lines = md_text.split('\n')
    normalized_lines = []
    inside_list = False

    for i, line in enumerate(lines):
        if re.match(r'^(\d+\.|-|\*|\+)\s', line.strip()):
            if not inside_list and i > 0 and lines[i - 1].strip() != '':
                normalized_lines.append('')
            inside_list = True
            normalized_lines.append(line)
        elif inside_list and line.strip() == '':
            if i < len(lines) - 1 and not re.match(r'^(\d+\.|-|\*|\+)\s', lines[i + 1].strip()):
                normalized_lines.append(line)
            continue
        else:
            inside_list = False
            normalized_lines.append(line)

    return '\n'.join(normalized_lines)

def convert_mdtext(md_text):
    code_block_pattern = re.compile(r'```(.*?)(?:```|$)', re.DOTALL)
    code_blocks = code_block_pattern.findall(md_text)
    non_code_parts = code_block_pattern.split(md_text)[::2]

    result = []
    for non_code, code in zip(non_code_parts, code_blocks + ['']):
        if non_code.strip():
            non_code = normalize_markdown(non_code)
            result.append(mdtex2html.convert(non_code, extensions=['tables']))
        if code.strip():
            code = f"```{code}\n\n```"
            code = markdown_to_html_with_syntax_highlight(code)
            result.append(code)
    result = "".join(result)
    return result

def detect_language(code):
    if code.startswith("\n"):
        first_line = ""
    else:
        first_line = code.strip().split('\n', 1)[0]
    language = first_line.lower() if first_line else ''
    code_without_language = code[len(first_line):].lstrip() if first_line else code
    return language, code_without_language


def construct_text(role, text):
    return {"role": role, "content": text}


def construct_user(text):
    return construct_text("user", text)


def construct_system(text):
    return construct_text("system", text)


def construct_assistant(text):
    return construct_text("assistant", text)


def construct_token_message(token, stream=False):
    return f "Token count: {token}"


def delete_last_conversation(chatbot, history, previous_token_count):
    if len(chatbot) > 0 and standard_error_msg in chatbot[-1][1]:
        logging.info("Only chatbot records are deleted due to the inclusion of error messages")
        chatbot.pop()
        return chatbot, history
    if len(history) > 0:
        logging.info("Deleted a set of conversation history")
        history.pop()
        history.pop()
    if len(chatbot) > 0:
        logging.info("Deleted a set of chatbot conversations")
        chatbot.pop()
    if len(previous_token_count) > 0:
        logging.info("Deleted a token count record for a set of conversations")
        previous_token_count.pop()
    return (
        chatbot,
        history,
        previous_token_count,
        construct_token_message(sum(previous_token_count)),
    )


def save_file(filename, system, history, chatbot):
    logging.info("Saving conversation history in ......")
    os.makedirs(HISTORY_DIR, exist_ok=True)
    if filename.endswith(".json"):
        json_s = {"system": system, "history": history, "chatbot": chatbot}
        print(json_s)
        with open(os.path.join(HISTORY_DIR, filename), "w") as f:
            json.dump(json_s, f)
    elif filename.endswith(".md"):
        md_s = f"system: \n- {system} \n"
        for data in history:
            md_s += f"\n{data['role']}: \n- {data['content']} \n"
        with open(os.path.join(HISTORY_DIR, filename), "w", encoding="utf8") as f:
            f.write(md_s)
    logging.info("Finished saving conversation history")
    return os.path.join(HISTORY_DIR, filename)


def save_chat_history(filename, system, history, chatbot):
    if filename == "":
        return
    if not filename.endswith(".json"):
        filename += ".json"
    return save_file(filename, system, history, chatbot)


def export_markdown(filename, system, history, chatbot):
    if filename == "":
        return
    if not filename.endswith(".md"):
        filename += ".md"
    return save_file(filename, system, history, chatbot)


def load_chat_history(filename, system, history, chatbot):
    logging.info("Loading conversation history in ......")
    if type(filename) != str:
        filename = filename.name
    try:
        with open(os.path.join(HISTORY_DIR, filename), "r") as f:
            json_s = json.load(f)
        try:
            if type(json_s["history"][0]) == str:
                logging.info("History format is old, being converted ......")
                new_history = []
                for index, item in enumerate(json_s["history"]):
                    if index % 2 == 0:
                        new_history.append(construct_user(item))
                    else:
                        new_history.append(construct_assistant(item))
                json_s["history"] = new_history
                logging.info(new_history)
        except:
            # No history of dialogue
            pass
        logging.info("Loading conversation history complete")
        return filename, json_s["system"], json_s["history"], json_s["chatbot"]
    except FileNotFoundError:
        logging.info("No conversation history file found, no action performed")
        return filename, system, history, chatbot


def sorted_by_pinyin(list):
    return sorted(list, key=lambda char: lazy_pinyin(char)[0][0])


def get_file_names(dir, plain=False, filetypes=[".json"]):
    logging.info(f "Get a list of file names, directory {dir}, file type {filetypes}, whether it is a plain text list {plain}")
    files = []
    try:
        for type in filetypes:
            files += [f for f in os.listdir(dir) if f.endswith(type)]
    except FileNotFoundError:
        files = []
    files = sorted_by_pinyin(files)
    if files == []:
        files = [""]
    if plain:
        return files
    else:
        return gr.Dropdown.update(choices=files)


def get_history_names(plain=False):
    logging.info("Get a list of history filenames")
    return get_file_names(HISTORY_DIR, plain)


def load_template(filename, mode=0):
    logging.info(f "Loading template file {filename} with mode {mode} (0 to return dictionary and dropdown menu, 1 to return dropdown menu, 2 to return dictionary)")
    lines = []
    logging.info("Loading template...")
    if filename.endswith(".json"):
        with open(os.path.join(TEMPLATES_DIR, filename), "r", encoding="utf8") as f:
            lines = json.load(f)
        lines = [[i["act"], i["prompt"]] for i in lines]
    else:
        with open(
            os.path.join(TEMPLATES_DIR, filename), "r", encoding="utf8"
        ) as csvfile:
            reader = csv.reader(csvfile)
            lines = list(reader)
        lines = lines[1:]
    if mode == 1:
        return sorted_by_pinyin([row[0] for row in lines])
    elif mode == 2:
        return {row[0]: row[1] for row in lines}
    else:
        choices = sorted_by_pinyin([row[0] for row in lines])
        return {row[0]: row[1] for row in lines}, gr.Dropdown.update(
            choices=choices, value=choices[0]
        )


def get_template_names(plain=False):
    logging.info("Get a list of template filenames")
    return get_file_names(TEMPLATES_DIR, plain, filetypes=[".csv", "json"])


def get_template_content(templates, selection, original_system_prompt):
    logging.info(f "In the application template, the selection is {selection} and the original system prompt is {original_system_prompt}")
    try:
        return templates[selection]
    except:
        return original_system_prompt


def reset_state():
    logging.info("Reset Status")
    return [], [], [], construct_token_message(0)


def reset_textbox():
    return gr.update(value="")


def reset_default():
    global API_URL
    API_URL = "https://api.openai.com/v1/chat/completions"
    os.environ.pop("HTTPS_PROXY", None)
    os.environ.pop("https_proxy", None)
    return gr.update(value=API_URL), gr.update(value=""), "API URL and proxy have been reset"


def change_api_url(url):
    global API_URL
    API_URL = url
    msg = f "API address changed to {url}"
    logging.info(msg)
    return msg


def change_proxy(proxy):
    os.environ["HTTPS_PROXY"] = proxy
    msg = f "Proxy changed to {proxy}"
    logging.info(msg)
    return msg


def hide_middle_chars(s):
    if len(s) <= 8:
        return s
    else:
        head = s[:4]
        tail = s[-4:]
        hidden = "*" * (len(s) - 8)
        return head + hidden + tail


def submit_key(key):
    key = key.strip()
    msg = f "API key changed to {hide_middle_chars(key)}"
    logging.info(msg)
    return key, msg


def sha1sum(filename):
    sha1 = hashlib.sha1()
    sha1.update(filename.encode("utf-8"))
    return sha1.hexdigest()


def replace_today(prompt):
    today = datetime.datetime.today().strftime("%Y-%m-%d")
    return prompt.replace("{current_date}", today)

def get_geoip():
    response = requests.get('https://ipapi.co/json/', timeout=5)
    data = response.json()
    if "error" in data.keys():
        logging.warning(f "Unable to get IP address information. \n{data}")
        if data['reason'] == "RateLimited":
            return f "Failed to get IP geolocation because the rate limit for detecting IPs was reached. The chat feature may still be available, but please note that you may experience problems if your IP address is in an unsupported region."
        else:
            return f "Failed to get IP geolocation. Reason: {data['reason']}"
    else:
        country = data['country_name']
        if country == "China":
            text = "**Your IP region: China. Please check the proxy settings immediately, using the API in an unsupported region may result in account banning. **"
        else:
            text = f "Your IP region: {country}."
        logging.info(text)
        return text
