# Dockerfile 指南

## 选择基础镜像

```{topic} 基本原则
- 官方镜像优于非官方的镜像，如果没有官方镜像，则尽量选择 Dockerfile 开源的。
- 固定版本 tag 而不是每次都使用 latest。
- 尽量选择体积小的镜像。
```

## 执行指令

```{topic} RUN
主要用于在镜像里执行指令，比如安装软件，下载文件等。
```

::::{tab-set}
:::{tab-item} 改进版
```Dockerfile
FROM python:3.8.13
RUN apt-get update \
    && apt-get install -y gcc g++ libtinfo-dev zlib1g-dev build-essential cmake \
    && apt install -y clang clangd llvm liblldb-dev libedit-dev libxml2-dev \
    && pip install decorator scipy attrs pandas toml
```
:::
:::{tab-item} 臃肿版
每一行的 `RUN` 命令都会产生一层镜像层，导致镜像的臃肿。
```Dockerfile
FROM python:3.8.13
RUN apt-get update
RUN apt-get install -y gcc g++ libtinfo-dev zlib1g-dev build-essential cmake
RUN apt install -y clang clangd llvm liblldb-dev libedit-dev libxml2-dev
RUN pip install decorator scipy attrs pandas toml
```
:::
::::

```{tip}
`docker image history fe5` 可以用于查看镜像历史。
```

## 文件复制和目录操作

往镜像里复制文件有两种方式，`COPY` 和 `ADD`。

### 复制普通文件

`COPY` 和 `ADD` 都可以把本地文件复制到镜像里，如果目标目录不存在，则会自动创建。

比如把本地的 `hello.py` 复制到 `/app` 目录下。若 `/app` 这个文件不存在，则会自动创建。

```Dockerfile
FROM python:3.9.5-alpine3.13
COPY hello.py /app/hello.py
```

### 复制压缩文件

`ADD` 比 `COPY` 高级一点的地方就是，如果复制的是 gzip 等压缩文件时，ADD 会帮助自动解压缩文件。

```Dockerfile
FROM python:3.9.5-alpine3.13
ADD hello.tar.gz /app/
```

### 如何选择

在 `COPY` 和 `ADD` 指令中选择的时候，可以遵循这样的原则：

> 所有的文件复制均使用 `COPY` 指令，仅在需要自动解压缩的场合使用 `ADD`。

## 构建参数和环境变量

`ARG` 和 `ENV` 是经常容易被混淆的两个 `Dockerfile` 的语法，都可以用来设置 “变量”。 但实际上两者有很多的不同。

::::{tab-set}
:::{tab-item} ENV
```Dockerfile
FROM ubuntu:20.04
ENV VERSION=2.0.1
RUN apt-get update && \
    apt-get install -y wget && \
    wget https://github.com/ipinfo/cli/releases/download/ipinfo-${VERSION}/ipinfo_${VERSION}_linux_amd64.tar.gz && \
    tar zxf ipinfo_${VERSION}_linux_amd64.tar.gz && \
    mv ipinfo_${VERSION}_linux_amd64 /usr/bin/ipinfo && \
    rm -rf ipinfo_${VERSION}_linux_amd64.tar.gz
```
:::
:::{tab-item} ARG
```Dockerfile
FROM ubuntu:20.04
ARG VERSION=2.0.1
RUN apt-get update && \
    apt-get install -y wget && \
    wget https://github.com/ipinfo/cli/releases/download/ipinfo-${VERSION}/ipinfo_${VERSION}_linux_amd64.tar.gz && \
    tar zxf ipinfo_${VERSION}_linux_amd64.tar.gz && \
    mv ipinfo_${VERSION}_linux_amd64 /usr/bin/ipinfo && \
    rm -rf ipinfo_${VERSION}_linux_amd64.tar.gz
```
:::
::::

- `ARG` 可以在镜像 build 的时候动态修改 `value`, 通过 `--build-arg`。
- `ENV` 设置的变量可以在镜像中保持，并在容器中可以被环境变量覆写。

## 构建镜像

```bash
docker image build -t demo ./
```

- `demo`：镜像的名称
- `./`：build context 所指向的目录

## `.dockerignore` 文件

```
.vscode/
env/
```

有了 `.dockerignore` 文件，构建时, build context 就小了很多。

## 尽量使用非 root 用户

## 多阶段构建镜像

