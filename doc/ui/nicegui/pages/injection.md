# NiceGUI 参数注入

多亏了 FastAPI，一个页面函数可以接受可选参数，以提供[路径参数](https://fastapi.tiangolo.com/tutorial/path-params/)、[查询参数](https://fastapi.tiangolo.com/tutorial/query-params/)或整个传入[请求](https://fastapi.tiangolo.com/advanced/using-request-directly/)，以便访问主体负载、标头、cookie等。

```python
from nicegui import ui

@ui.page('/icon/{icon}')
def icons(icon: str, amount: int = 1):
    ui.label(icon).classes('text-h3')
    with ui.row():
        [ui.icon(icon).classes('text-h3') for _ in range(amount)]
ui.link('Star', '/icon/star?amount=5')
ui.link('Home', '/icon/home')
ui.link('Water', '/icon/water_drop?amount=3')

# ui.run()
```
