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

## UsageTips

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

#### View run status
```shell
docker logs chatgpt
```

#### You can also modify the script and build the image manually

```shell
docker build -t chuanhuchatgpt:latest .
```
</details>


### Remote deployment

<details><summary>Please read this section if you need to deploy this project on a public server</summary>

### Deploy to a public server

Change the last sentence to read

```
demo.queue().launch(server_name="0.0.0.0", server_port=7860, share=False) # 可自定义端口
```
### Protect page with account password

Change the last sentence to read

```
demo.queue().launch(server_name="0.0.0.0", server_port=7860,auth=("fill in username here", "fill in password here")) # You can set username and password
```

### Configuring Nginx Reverse Proxy

Note: Configuring a reverse proxy is not required. If you need to use a domain name, you need to configure an Nginx reverse proxy.

Also: Currently, after configuring authentication, Nginx must be configured with SSL, otherwise [Cookie mismatch issue](https://github.com/GaiZhenbiao/ChuanhuChatGPT/issues/89) will occur.

Adding a standalone profile.
```nginx
server {
	listen 80;
	server_name /domain/; # Please fill in the domain name you set
	access_log off;
	error_log off;
	location / {
		proxy_pass http://127.0.0.1:7860;   # Note the port number
		proxy_redirect off;
		proxy_set_header Host $host;
		proxy_set_header X-Real-IP $remote_addr;
		proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
		proxy_set_header Upgrade $http_upgrade;		# Websocket configuration
		proxy_set_header Connection $connection_upgrade;		#Websocket configuration
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

Modify the `nginx.conf` configuration file (usually in `/etc/nginx/nginx.conf`) and add the following configuration to the http section.
(this step is to configure the websocket connection, if previously configured can be ignored)
```nginx
map $http_upgrade $connection_upgrade {
  default upgrade;
  ''      close;
  }
```

In order to configure both domain access and authentication, you need to configure the SSL certificate, you can refer to [this blog](https://www.gzblog.tech/2020/12/25/how-to-config-hexo/#%E9%85%8D%E7%BD%AEHTTPS) for one-click configuration


### Enabling HTTPS for ChuanhuChatGPT using Docker all the way

If your VPS port 80 and 443 are not occupied, then you can consider the following method, just bind your domain name to your VPS IP in advance. This method is provided by [@iskoldt-X](https://github.com/iskoldt-X).

First, run [nginx-proxy](https://github.com/nginx-proxy/nginx-proxy)

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
Next, run [acme-companion](https://github.com/nginx-proxy/acme-companion), which is the container used to automatically request TLS certificates

```
docker run --detach \
    --name nginx-proxy-acme \
    --volumes-from nginx-proxy \
    --volume /var/run/docker.sock:/var/run/docker.sock:ro \
    --volume acme:/etc/acme.sh \
    --env "DEFAULT_EMAIL=your email (for TLS certificate request)" \
    nginxproxy/acme-companion
```

Finally, you can run ChuanhuChatGPT
```
docker run -d --name chatgpt \
	-e my_api_key="Your API" \
	-e USERNAME="Replace with username" \
	-e PASSWORD="Replace with password" \
	-v ~/chatGPThistory:/app/history \
	-e VIRTUAL_HOST=Your domain name \
	-e VIRTUAL_PORT=7860 \
	-e LETSENCRYPT_HOST=Your domain name \
	tuchuanhuhuhu/chuanhuchatgpt:latest
```
This will enable automatic application of TLS certificate and HTTPS for ChuanhuChatGPT.
</details>

---

## Troubleshooting

First, try pulling the latest changes for this project and retry with the latest code.

Click `Download ZIP` on the web page to download the latest code, or
```shell
git pull https://github.com/GaiZhenbiao/ChuanhuChatGPT.git main -f
```

If you still have problems, try reinstalling gradio again:

```
pip install gradio --upgrade --force-reinstall
```

Very often, this solves the problem.

### Frequently Asked Questions

<details><summary>Configuration Proxy</summary>

OpenAI does not allow the use of the API in unsupported regions, otherwise it may result in the account being winded up. Example proxy configurations are given below.

In the Clash configuration file, add.

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
 - DOMAIN-SUFFIX,openai.com,your proxy rules
```

If you use Surge, add to the configuration file.

```
[Rule]
DOMAIN-SET,https://cdn.jsdelivr.net/gh/Loyalsoldier/surge-rules@release/private.txt,DIRECT
DOMAIN-SUFFIX,openai.com,your proxy rules
```
Note that if you already have corresponding fields, please merge these rules into the existing fields, otherwise the proxy software will report an error.

</details>

<details><summary><code>TypeError: Base.set () got an unexpected keyword argument</code></summary>

This is because Chuanhu ChatGPT keeps pace with Gradio development, and your Gradio version is too old. Please upgrade the dependency on.

```
pip install -r requirements.txt --upgrade
```
</details>

<details><summary><code>No module named '_bz2'</code></summary>

> Deployed on CentOS7.6,Python3.11.0, last error is ModuleNotFoundError. no module named '_bz2'

Download the `bzip` compiler environment before installing python

```
sudo yum install bzip2-devel
```
</details>

<details><summary><code>openai.error.APIConnectionError</code></summary>

> If someone is also getting the `openai.error.APIConnectionError` prompted error, it may be due to the `urllib3` version. If the `urllib3` version is greater than `1.25.11`, this problem will occur.
>
> The solution is to uninstall `urllib3` and reinstall it to `1.25.11` and run it again

See: [#5](https://github.com/GaiZhenbiao/ChuanhuChatGPT/issues/5)

Uninstall `urllib3` in terminal or command prompt

```
pip uninstall urllib3
```

Then, install the required version by using the `pip install` command with the specified version number:.

```
pip install urllib3==1.25.11
```

Referenced from.
[Solve the problem where OpenAI API can't connect even after using a proxy](https://zhuanlan.zhihu.com/p/611080662)
</details>

<details><summary><code>Verify fails after setting API Key in Python file</code></summary>

> Authentication error after setting APIkey in ChuanhuChatbot.py, prompting "An unknown error occurred Orz"

See: [#26](https://github.com/GaiZhenbiao/ChuanhuChatGPT/issues/26)
</details>

<details><summary><code>Always Waiting/SSL Error</code></summary>

> SSLError [#49](https://github.com/GaiZhenbiao/ChuanhuChatGPT/issues/49) after updating script file
>
> After running, the input problem seems to be unresponsive and no error is reported [#25](https://github.com/GaiZhenbiao/ChuanhuChatGPT/issues/25)
>
> ```
> requests.exceptions.SSLError: HTTPSConnectionPool(host='api.openai.com', port=443): Max retries exceeded with url: /v1/chat/completions (Caused by SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)')))
> ```

Please refer to the Configuring Proxies section and add `openai.com` to the proxy rules of the proxy app you are using. Be careful not to add `127.0.0.1` to the proxy, otherwise you will get the next error.

</details>

<details><summary><code>Webpage error Something went wrong</code></summary>

> ```
> Something went wrong
> Expecting value: 1ine 1 column 1 (char o)
> ```

The reason for this error is that `127.0.0.1` is being proxied, so the web page cannot communicate with the backend. Please set the proxy software to add `127.0.0.1` to the direct connection (see the "Waiting/SSL Error" section above for details).
</details>

<details><summary><code>No matching distribution found for openai>=0.27.0</code></summary>

The dependency `openai` has been removed. Please try to download the latest version of the script.
</details>

## Starchart

[![Star History Chart](https://api.star-history.com/svg?repos=GaiZhenbiao/ChuanhuChatGPT&type=Date)](https://star-history.com/#GaiZhenbiao/ChuanhuChatGPT&Date)

## Contributors

<a href="https://github.com/GaiZhenbiao/ChuanhuChatGPT/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=GaiZhenbiao/ChuanhuChatGPT" />
</a>

## Donation

🐯 Buy the author a Coke ~

<img width="350" alt="image" src="https://user-images.githubusercontent.com/51039745/223626874-f471e5f5-8a06-43d5-aa31-9d2575b6f631.JPG">
