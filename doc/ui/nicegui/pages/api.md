# NiceGUI API 响应

NiceGUI 基于 FastAPI 构建。这意味着您可以使用 FastAPI 的所有功能。例如，除了图形用户界面外，您还可以实现 RESTful API。您只需从 `nicegui` 中导入 `app` 对象。或者，您可以通过使用 `ui.run_with(app)` 而不是自动启动服务器的 `ui.run()` 来在您自己的 FastAPI 应用程序上运行 NiceGUI。

您还可以在页面函数内返回任何其他 FastAPI 响应对象。例如，在某些条件满足时，您可以返回 `RedirectResponse` 以将用户重定向到另一个页面。这在[身份验证](https://github.com/zauberzeug/nicegui/tree/main/examples/authentication/main.py)演示中使用。

```python
import random
from nicegui import app, ui

@app.get('/random/{max}')
def generate_random_number(max: int):
    return {'min': 0, 'max': max, 'value': random.randint(0, max)}

max = ui.number('max', value=100)
ui.button('generate random number',
          on_click=lambda: ui.navigate.to(f'/random/{max.value:.0f}'))

# ui.run()
```
