# NiceGUI 向页面添加 HTML

您可以通过调用 `ui.add_head_html` 或 `ui.add_body_html` 向页面添加 HTML。这对于添加自定义 CSS 样式或 JavaScript 代码非常有用。

```python
from nicegui import ui

ui.add_head_html('''
    <style>
        .my-red-label {
            color: Crimson;
            font-weight: bold;
        }
    </style>
''')
ui.label('RED').classes('my-red-label')

# ui.run()
```
