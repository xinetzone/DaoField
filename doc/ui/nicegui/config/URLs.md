# NiceGUI URLs

您可以通过 `app.urls` 访问 NiceGUI 应用程序可用的所有 URL 列表。由于服务器尚未运行，因此在 `app.on_startup` 中无法访问这些 URL。相反，您可以在页面函数中访问它们，或者使用 `app.urls.on_change` 注册回调函数。

```python
from nicegui import app, ui

@ui.page('/')
def index():
    for url in app.urls:
        ui.link(url, target=url)

# ui.run()
```
