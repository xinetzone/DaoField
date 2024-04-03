# Deta 部署（暂未成功）

```bash
space login
space new
space push
space release
```

启动服务：

```bash
uvicorn main:app --reload --proxy-headers --host 0.0.0.0 --port 9000
```
