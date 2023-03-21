<h1 align="center">ChatGPT 🐯 Chuanhu ChatGPT</h1>
<div align="center">
  <a href="https://github.com/GaiZhenBiao/ChuanhuChatGPT">
    <img src="https://user-images.githubusercontent.com/70903329/226267132-e5295925-f53a-4e9d-a221-6099583da98d.png" alt="Logo" height="156">
  </a>

  <p align="center">
    <h3>Provides a light and easy to use web GUI for the ChatGPT API</h3>
    <p align="center">
      <a href="https://github.com/GaiZhenbiao/ChuanhuChatGPT/blob/main/LICENSE">
        <img alt="Tests Passing" src="https://img.shields.io/github/license/GaiZhenbiao/ChuanhuChatGPT" />
      </a>
      <a href="https://gradio.app/">
        <img alt="GitHub Contributors" src="https://img.shields.io/badge/Base-Gradio-fb7d1a?style=flat" />
      </a>
      <a href="https://github.com/GaiZhenBiao/ChuanhuChatGPT/graphs/contributors">
        <img alt="GitHub Contributors" src="https://img.shields.io/github/contributors/GaiZhenBiao/ChuanhuChatGPT" />
      </a>
      <a href="https://github.com/GaiZhenBiao/ChuanhuChatGPT/issues">
        <img alt="Issues" src="https://img.shields.io/github/issues/GaiZhenBiao/ChuanhuChatGPT?color=0088ff" />
      </a>
      <a href="https://github.com/GaiZhenBiao/ChuanhuChatGPT/pulls">
        <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/GaiZhenBiao/ChuanhuChatGPT?color=0088ff" />
      </a>
      <p>
      	Real-time replies / Unlimited conversations / Save conversation logs / Preset Prompt sets / Network search / Upload files
      	<br/>
      	Render LaTex / Render Forms / Render Code / Code Highlighting / Custom api-URL / "Small and Beautiful" Experience / Ready for GPT-4
      </p>
      <a href="https://www.bilibili.com/video/BV1mo4y1r7eE"><strong>Video Tutorials</strong></a>
        ·
      <a href="https://www.bilibili.com/video/BV1184y1w7aP"><strong>2.0 Introduction Video</strong></a>
	·
      <a href="https://huggingface.co/spaces/JohnSmith9982/ChuanhuChatGPT"><strong>Online Experience</strong></a>
    </p>
    <p align="center">
      <img alt="Animation Demo" src="https://user-images.githubusercontent.com/51039745/226255695-6b17ff1f-ea8d-464f-b69b-a7b6b68fffe8.gif" />
    </p>
  </p>
</div>

## Contents
|[UsageTips](#UsageTips)|[Installation](#Installation)|[Troubleshooting](#Troubleshooting)| [Buy a Coke for the author🥤](#Donation) |
|  ----  | ----  | ----  | --- |

## Usage Tips

- Prerequisites can be set very efficiently using System Prompt.
- To use the Prompt template function, select the Prompt template collection file and then select the desired prompt from the drop-down menu.
- If you are not satisfied with the answer, you can use the `Rebuild` button and try again.
- For long conversations, you can use the `Optimize Tokens` button to reduce Tokens usage.
- The input box supports line feeds, just press `shift enter`.
- Deploy to server: change the last sentence of the program to `demo.launch(server_name="0.0.0.0", server_port=<your port number>)`.
- Get the public link: change the last sentence of the program to `demo.launch(share=True)`. Note that the program must be running in order to be accessible via public links.
- Use on Hugging Face: It is recommended to **Duplicate this Space** in the upper right corner before using it, this will greatly reduce the queuing time and the app will respond more quickly.
  <img width="300" alt="image" src="https://user-images.githubusercontent.com/51039745/223447310-e098a1f2-0dcf-48d6-bcc5-49472dd7ca0d.png">

## Installation

### Local deployment

1. **Download this project**

	```shell
	git clone https://github.com/GaiZhenbiao/ChuanhuChatGPT.git
	cd ChuanhuChatGPT
	```
	Or, click `Download ZIP` in the upper right corner of the web page, download and unzip it, then enter the folder and go to `Terminal` or `Command Prompt`.

	If you are using Windows, you should hold down `shift` and right click in the folder and select "Open in Terminal". If this option is not available, select "Open Powershell window here". If you are using macOS, you can right click on the current folder in the path bar at the bottom of the Finder and select `Service - New Terminal Tab in Folder Location`.

	<img width="200" alt="downloadZIP" src="https://user-images.githubusercontent.com/23137268/223696317-b89d2c71-c74d-4c6d-8060-a21406cfb8c8.png">

2. **Fill in the API key**

	Choose any one of the following 3 methods.

	<details><summary>1. Fill in your API key in the GUI</summary>

	Keys set this way will be cleared after the page is refreshed.

	<img width="760" alt="image" src="https://user-images.githubusercontent.com/51039745/222873756-3858bb82-30b9-49bc-9019-36e378ee624d.png"></details>
	<details><summary>2. Fill in your OpenAI API key in the direct code</summary>

	The key set in this way will become the default key. Here you can also choose whether to hide the key input box in the UI.

	<img width="525" alt="image" src="https://user-images.githubusercontent.com/51039745/223440375-d472de4b-aa7f-4eae-9170-6dc2ed9f5480.png"></details>

	<details><summary>3. Set the default key, username password in the file</summary>

	The key set in this way can be retained after pulling the project update.

	Create these two new files: `api_key.txt` and `auth.json` in the project folder.

	Fill in your API-Key in `api_key.txt`, be careful not to fill in any irrelevant content。

	Fill in your username and password in `auth.json`.

	```
	{
    "username": "Username",
    "password": "Password"
	}
	```

	</details>

3. **Installation of Dependencies**

	Type the following command in the terminal and enter.

	```shell
	pip install -r requirements.txt
	```

	If an error is reported, try

	```shell
	pip3 install -r requirements.txt
	```

	If it still doesn't work, please [install Python] first(https://www.runoob.com/python/python-install.html)。

	If the download is slow, we suggest [Configure Tsinghua Source](https://mirrors.tuna.tsinghua.edu.cn/help/pypi/), or scientific Internet access.

4. **Start up**

	Please use the following command.

	```shell
	python ChuanhuChatbot.py
	```

	If an error is reported, try

	```shell
	python3 ChuanhuChatbot.py
	```

	If it still doesn't work, please [install Python] first(https://www.runoob.com/python/python-install.html)。
<br />

If all goes well, you should now be able to view and use ChuanhuChatGPT by typing [`http://localhost:7860`](http://localhost:7860) into your browser address bar.

**If you encounter problems during installation, please check the [Troubleshooting](#Troubleshooting) section first. **

### Running with Docker

<details><summary>If you find the above method cumbersome, we provide a Docker image</summary>

#### Pull Image

```shell
docker pull tuchuanhuhuhu/chuanhuchatgpt:latest
```

#### Run

```shell
docker run -d --name chatgpt \
	-e my_api_key="Replace with API" \
	-e USERNAME="Replace with username" \
	-e PASSWORD="Replace with password" \
	-v ~/chatGPThistory:/app/history \
	-p 7860:7860 \
	tuchuanhuhuhu/chuanhuchatgpt:latest
```

Note: The `USERNAME` and `PASSWORD` lines can be omitted. If omitted, authentication will not be enabled.

#### 查看运行状态
```shell
docker logs chatgpt
```

#### 也可修改脚本后手动构建镜像

```shell
docker build -t chuanhuchatgpt:latest .
```
</details>


### 远程部署

<details><summary>如果需要在公网服务器部署本项目，请阅读该部分</summary>

### 部署到公网服务器

将最后一句修改为

```
demo.queue().launch(server_name="0.0.0.0", server_port=7860, share=False) # 可自定义端口
```
### 用账号密码保护页面

将最后一句修改为

```
demo.queue().launch(server_name="0.0.0.0", server_port=7860,auth=("在这里填写用户名", "在这里填写密码")) # 可设置用户名与密码
```

### 配置 Nginx 反向代理

注意：配置反向代理不是必须的。如果需要使用域名，则需要配置 Nginx 反向代理。

又及：目前配置认证后，Nginx 必须配置 SSL，否则会出现 [Cookie 不匹配问题](https://github.com/GaiZhenbiao/ChuanhuChatGPT/issues/89)。

添加独立配置文件：
```nginx
server {
	listen 80;
	server_name /域名/;   # 请填入你设定的域名
	access_log off;
	error_log off;
	location / {
		proxy_pass http://127.0.0.1:7860;   # 注意端口号
		proxy_redirect off;
		proxy_set_header Host $host;
		proxy_set_header X-Real-IP $remote_addr;
		proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
		proxy_set_header Upgrade $http_upgrade;		# Websocket配置
		proxy_set_header Connection $connection_upgrade;		#Websocket配置
		proxy_max_temp_file_size 0;
		client_max_body_size 10m;
		client_body_buffer_size 128k;
		proxy_connect_timeout 90;
		proxy_send_timeout 90;
		proxy_read_timeout 90;
		proxy_buffer_size 4k;
		proxy_buffers 4 32k;
		proxy_busy_buffers_size 64k;
		proxy_temp_file_write_size 64k;
	}
}
```

修改`nginx.conf`配置文件（通常在`/etc/nginx/nginx.conf`），向http部分添加如下配置：
（这一步是为了配置websocket连接，如之前配置过可忽略）
```nginx
map $http_upgrade $connection_upgrade {
  default upgrade;
  ''      close;
  }
```

为了同时配置域名访问和身份认证，需要配置SSL的证书，可以参考[这篇博客](https://www.gzblog.tech/2020/12/25/how-to-config-hexo/#%E9%85%8D%E7%BD%AEHTTPS)一键配置


### 全程使用Docker 为ChuanhuChatGPT 开启HTTPS

如果你的VPS 80端口与443端口没有被占用，则可以考虑如下的方法，只需要将你的域名提前绑定到你的VPS 的IP即可。此方法由[@iskoldt-X](https://github.com/iskoldt-X) 提供。

首先，运行[nginx-proxy](https://github.com/nginx-proxy/nginx-proxy)

```
docker run --detach \
    --name nginx-proxy \
    --publish 80:80 \
    --publish 443:443 \
    --volume certs:/etc/nginx/certs \
    --volume vhost:/etc/nginx/vhost.d \
    --volume html:/usr/share/nginx/html \
    --volume /var/run/docker.sock:/tmp/docker.sock:ro \
    nginxproxy/nginx-proxy
```
接着，运行[acme-companion](https://github.com/nginx-proxy/acme-companion)，这是用来自动申请TLS 证书的容器

```
docker run --detach \
    --name nginx-proxy-acme \
    --volumes-from nginx-proxy \
    --volume /var/run/docker.sock:/var/run/docker.sock:ro \
    --volume acme:/etc/acme.sh \
    --env "DEFAULT_EMAIL=你的邮箱（用于申请TLS 证书）" \
    nginxproxy/acme-companion
```

最后，可以运行ChuanhuChatGPT
```
docker run -d --name chatgpt \
	-e my_api_key="你的API" \
	-e USERNAME="替换成用户名" \
	-e PASSWORD="替换成密码" \
	-v ~/chatGPThistory:/app/history \
	-e VIRTUAL_HOST=你的域名 \
	-e VIRTUAL_PORT=7860 \
	-e LETSENCRYPT_HOST=你的域名 \
	tuchuanhuhuhu/chuanhuchatgpt:latest
```
如此即可为ChuanhuChatGPT实现自动申请TLS证书并且开启HTTPS
</details>

---

## 疑难杂症解决

首先，请先尝试拉取本项目的最新更改，使用最新的代码重试。

点击网页上的 `Download ZIP` 下载最新代码，或
```shell
git pull https://github.com/GaiZhenbiao/ChuanhuChatGPT.git main -f
```

如果还有问题，可以再尝试重装 gradio:

```
pip install gradio --upgrade --force-reinstall
```

很多时候，这样就可以解决问题。

### 常见问题

<details><summary>配置代理</summary>

OpenAI不允许在不受支持的地区使用API，否则可能会导致账号被风控。下面给出代理配置示例：

在Clash配置文件中，加入：

```
rule-providers:
  private:
    type: http
    behavior: domain
    url: "https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/lancidr.txt"
    path: ./ruleset/ads.yaml
    interval: 86400

rules:
 - RULE-SET,private,DIRECT
 - DOMAIN-SUFFIX,openai.com,你的代理规则
```

如果你使用 Surge，请在配置文件中加入：

```
[Rule]
DOMAIN-SET,https://cdn.jsdelivr.net/gh/Loyalsoldier/surge-rules@release/private.txt,DIRECT
DOMAIN-SUFFIX,openai.com,你的代理规则
```
注意，如果你本来已经有对应的字段，请将这些规则合并到已有字段中，否则代理软件会报错。

</details>

<details><summary><code>TypeError: Base.set () got an unexpected keyword argument</code></summary>

这是因为川虎ChatGPT紧跟Gradio发展步伐，你的Gradio版本太旧了。请升级依赖：

```
pip install -r requirements.txt --upgrade
```
</details>

<details><summary><code>No module named '_bz2'</code></summary>

> 部署在CentOS7.6,Python3.11.0上,最后报错ModuleNotFoundError: No module named '_bz2'

安装python前先下载 `bzip` 编译环境

```
sudo yum install bzip2-devel
```
</details>

<details><summary><code>openai.error.APIConnectionError</code></summary>

> 如果有人也出现了`openai.error.APIConnectionError`提示的报错，那可能是`urllib3`的版本导致的。`urllib3`版本大于`1.25.11`，就会出现这个问题。
>
> 解决方案是卸载`urllib3`然后重装至`1.25.11`版本再重新运行一遍就可以

参见：[#5](https://github.com/GaiZhenbiao/ChuanhuChatGPT/issues/5)

在终端或命令提示符中卸载`urllib3`

```
pip uninstall urllib3
```

然后，通过使用指定版本号的`pip install`命令来安装所需的版本：

```
pip install urllib3==1.25.11
```

参考自：
[解决OpenAI API 挂了代理还是连接不上的问题](https://zhuanlan.zhihu.com/p/611080662)
</details>

<details><summary><code>在 Python 文件里 设定 API Key 之后验证失败</code></summary>

> 在ChuanhuChatbot.py中设置APIkey后验证出错，提示“发生了未知错误Orz”

参见：[#26](https://github.com/GaiZhenbiao/ChuanhuChatGPT/issues/26)
</details>

<details><summary><code>一直等待/SSL Error</code></summary>

> 更新脚本文件后，SSLError [#49](https://github.com/GaiZhenbiao/ChuanhuChatGPT/issues/49)
>
> 跑起来之后，输入问题好像就没反应了，也没报错 [#25](https://github.com/GaiZhenbiao/ChuanhuChatGPT/issues/25)
>
> ```
> requests.exceptions.SSLError: HTTPSConnectionPool(host='api.openai.com', port=443): Max retries exceeded with url: /v1/chat/completions (Caused by SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)')))
> ```

请参考配置代理部分，将`openai.com`加入你使用的代理App的代理规则。注意不要将`127.0.0.1`加入代理，否则会有下一个错误。

</details>

<details><summary><code>网页提示错误 Something went wrong</code></summary>

> ```
> Something went wrong
> Expecting value: 1ine 1 column 1 (char o)
> ```

出现这个错误的原因是`127.0.0.1`被代理了，导致网页无法和后端通信。请设置代理软件，将`127.0.0.1`加入直连（具体方法见上面“一直等待/SSL Error”部分）。
</details>

<details><summary><code>No matching distribution found for openai>=0.27.0</code></summary>

`openai`这个依赖已经被移除了。请尝试下载最新版脚本。
</details>

## Starchart

[![Star History Chart](https://api.star-history.com/svg?repos=GaiZhenbiao/ChuanhuChatGPT&type=Date)](https://star-history.com/#GaiZhenbiao/ChuanhuChatGPT&Date)

## Contributors

<a href="https://github.com/GaiZhenbiao/ChuanhuChatGPT/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=GaiZhenbiao/ChuanhuChatGPT" />
</a>

## 捐款

🐯请作者喝可乐～

<img width="350" alt="image" src="https://user-images.githubusercontent.com/51039745/223626874-f471e5f5-8a06-43d5-aa31-9d2575b6f631.JPG">
