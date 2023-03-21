# -*- coding:utf-8 -*-

# ChatGPT Settings
initial_prompt = "You are a helpful assistant."
API_URL = "https://api.openai.com/v1/chat/completions"
HISTORY_DIR = "history"
TEMPLATES_DIR = "templates"

# Error messages
standard_error_msg = "An error occurred at ☹️:" # Standard prefix for error messages
error_retrieve_prompt = "Please check the network connection, or if the API-Key is valid."  # An error occurred while getting the conversation
connection_timeout_prompt = "The connection timed out and the conversation could not be accessed."  # Connection timeout
read_timeout_prompt = "Read timeout, unable to fetch conversation."  # Read timeout
proxy_error_prompt = "Proxy error, unable to fetch conversation."  # Proxy error
ssl_error_prompt = "SSL error, unable to fetch conversation."  # SSL error
no_apikey_msg = "The API key length is not 51 bits, please check if it is entered correctly."  # API key length is less than 51 bits

max_token_streaming = 3500  # Maximum number of tokens when streaming conversations
timeout_streaming = 30  # Timeouts during streaming conversations
max_token_all = 3500  # Maximum number of tokens for non-streaming conversations
timeout_all = 200  # Timeout time for non-streaming conversations
enable_streaming_option = True  # Whether to enable the checkbox to select whether to display answers in real time
HIDE_MY_KEY = False  # If you want to hide your API key in the UI, set this value to True

SIM_K = 5
INDEX_QUERY_TEMPRATURE = 1.0

title = """<h1 align="left" style="min-width:200px; margin-top:0;">Chuanhu ChatGPT 🚀</h1>"""
description = """\
<div align="center" style="margin:16px 0">

由Bilibili [土川虎虎虎](https://space.bilibili.com/29125536) 和 [明昭MZhao](https://space.bilibili.com/24807452)开发

Visit Kawhoo ChatGPT's [GitHub project](https://github.com/GaiZhenbiao/ChuanhuChatGPT) to download the latest version of the script

This app uses the `gpt-3.5-turbo` large language model
</div>
"""

summarize_prompt = "Who are you? What did we just talk about?"  # prompt when summarizing the conversation

MODELS = [
    "gpt-3.5-turbo",
    "gpt-3.5-turbo-0301",
    "gpt-4",
    "gpt-4-0314",
    "gpt-4-32k",
    "gpt-4-32k-0314",
] # Optional models


WEBSEARCH_PTOMPT_TEMPLATE = """\
Web search results:

{web_results}
Current date: {current_date}

Instructions: Using the provided web search results, write a comprehensive reply to the given query. Make sure to cite results using [[number](URL)] notation after the reference. If the provided search results refer to multiple subjects with the same name, write separate answers for each subject.
Query: {query}
Reply in English """

PROMPT_TEMPLATE = """\
Context information is below.
---------------------
{context_str}
---------------------
Current date: {current_date}.
Using the provided context information, write a comprehensive reply to the given query.
Make sure to cite results using [number] notation after the reference.
If the provided context information refer to multiple subjects with the same name, write separate answers for each subject.
Use prior knowledge only if the given context didn't provide enough information.
Answer the question: {query_str}
Reply in Chinese
"""

REFINE_TEMPLATE = """\
The original question is as follows: {query_str}
We have provided an existing answer: {existing_answer}
We have the opportunity to refine the existing answer
(only if needed) with some more context below.
------------
{context_msg}
------------
Given the new context, refine the original answer to better
Answer in the same language as the question, such as English, 中文, 日本語, Español, Français, or Deutsch.
If the context isn't useful, return the original answer.
"""
