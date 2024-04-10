# NiceGUI 查询选择器

要操作像文档 `body` 这样的元素，您可以使用 `ui.query` 函数。通过查询结果，您可以像操作其他 UI 元素一样添加类、样式和属性。例如，这可以用于更改页面背景颜色（例如 `ui.query('body').classes('bg-green')`）。

`selector`：CSS 选择器（例如 `"body"`、`"#my-id"`、`".my-class"`、`"div > p"`）

```python
from nicegui import ui

def set_background(color: str) -> None:
    ui.query('body').style(f'background-color: {color}')

ui.button('Blue', on_click=lambda: set_background('#ddeeff'))
ui.button('Orange', on_click=lambda: set_background('#ffeedd'))

# ui.run()
```

## NiceGUI 设置背景渐变

设置背景渐变、图像或类似效果非常简单。有关使用 CSS 设置背景的更多信息，请参见 [`w3schools.com`](https://www.w3schools.com/cssref/pr_background-image.php)。

```python
from nicegui import ui

ui.query('body').classes('bg-gradient-to-t from-blue-400 to-blue-100')

# ui.run()
```

## NiceGUI 修改默认页面内边距

默认情况下，NiceGUI 在页面内容周围提供了一个内置的内边距。您可以使用类选择器 `.nicegui-content` 来修改它。

```python
from nicegui import ui

ui.query('.nicegui-content').classes('p-0')
with ui.column().classes('h-screen w-full bg-gray-400 justify-between'):
    ui.label('top left')
    ui.label('bottom right').classes('self-end')

# ui.run()
```
