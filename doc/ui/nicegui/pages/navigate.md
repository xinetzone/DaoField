# {func}`~nicegui.ui.navigate` 导航函数

这些函数允许您在浏览器历史中进行导航，并跳转到外部 URL。

```python
from nicegui import ui

with ui.row():
    ui.button('Back', on_click=ui.navigate.back)
    ui.button('Forward', on_click=ui.navigate.forward)
    ui.button(icon='savings',
              on_click=lambda: ui.navigate.to('https://github.com/sponsors/zauberzeug'))

# ui.run()
```

## `ui.navigate.to`

可用于以编程方式打开不同的页面或URL。

当使用 `new_tab` 参数时，浏览器可能会阻止新标签页的打开。这是浏览器设置，应用程序无法更改。您可能希望改用 `ui.link` 及其 `new_tab` 参数。

此功能以前作为 `ui.open` 提供，现已弃用。

注意：当使用自动索引页面（例如没有 `@page` 装饰器）时，除非指定了套接字，否则连接到该页面的所有客户端（即浏览器）都将打开目标 URL。用户事件（如按钮点击）提供了这样的套接字。

- `target`：页面函数、同一页面上的NiceGUI元素或从基本URL开始的绝对URL或相对路径的字符串
- `new_tab`：是否在新标签页中打开目标（可能会被浏览器阻止）

```python
from nicegui import ui

url = 'https://github.com/zauberzeug/nicegui/'
ui.button('Open GitHub', on_click=lambda: ui.navigate.to(url, new_tab=True))

# ui.run()
```
