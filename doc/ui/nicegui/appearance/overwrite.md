# NiceGUI 覆盖 Tailwind 的默认样式

Tailwind 会重置 HTML 元素的默认样式，例如本例中的 `h2` 元素的字体大小。您可以通过添加一个类型为 `text/tailwindcss` 的 `style` 标签来覆盖这些默认值。如果没有这个类型，样式将被过早地评估并被 Tailwind 覆盖。

```python
from nicegui import ui

ui.add_head_html('''
    <style type="text/tailwindcss">
        h2 {
            font-size: 150%;
        }
    </style>
''')
ui.html('<h2>Hello world!</h2>')

# ui.run()
```
