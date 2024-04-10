# NiceGUI 服务器托管

要将你的 NiceGUI 应用部署到服务器上，你需要在你的云基础设施上执行你的 `main.py`（或包含 `ui.run(...)` 的任何文件）。例如，你可以通过 `pip` 安装 NiceGUI Python 包，并使用 `systemd` 或类似的服务来启动主脚本。在大多数情况下，你会将端口设置为 `80`（或者如果你想使用 HTTPS，则设置为 `443`），以便通过 `ui.run` 命令从外部轻松访问。

一个方便的替代方案是使用我们预构建的多架构 Docker 镜像，其中包含了所有必要的依赖项。使用以下命令，你可以在当前目录中启动脚本 `main.py`，并将其公开在端口 `80` 上运行：

```bash
docker run -it --restart always \
-p 80:8080 \
-e PUID=$(id -u) \
-e PGID=$(id -g) \
-v $(pwd)/:/app/ \
zauberzeug/nicegui:latest
```

演示程序假设 `main.py` 在 `ui.run` 命令中使用端口 `8080`（这是默认值）。`-d` 告诉 `docker` 在后台运行，`--restart always` 确保如果应用程序崩溃或服务器重启时容器会重新启动。当然，这也可以写在一个 Docker compose 文件中：

`docker-compose.yml`
```
app:
    image: zauberzeug/nicegui:latest
    restart: always
    ports:
        - 80:8080
    environment:
        - PUID=1000 # change this to your user id
        - PGID=1000 # change this to your group id
    volumes:
        - ./:/app/
```

这个Docker镜像中还有其他实用的功能，比如非root用户执行和信号穿透。想要了解更多细节，我们建议你查看我们的[Docker示例](https://github.com/zauberzeug/nicegui/tree/main/examples/docker_image)。

你可以使用[FastAPI](https://fastapi.tiangolo.com/deployment/https/)直接提供SSL证书。在生产环境中，我们也喜欢使用像[Traefik](https://doc.traefik.io/traefik/)或[NGINX](https://www.nginx.com/)这样的反向代理来为我们处理这些细节。查看我们的开发[docker-compose.yml](https://github.com/zauberzeug/nicegui/blob/main/docker-compose.yml)作为示例。

你也可以查看[我们用于使用自定义FastAPI应用的演示](https://github.com/zauberzeug/nicegui/tree/main/examples/fastapi)。这将允许你进行如[FastAPI文档](https://fastapi.tiangolo.com/deployment/)中描述的非常灵活的部署。注意，要允许多个worker，需要进行额外的步骤。