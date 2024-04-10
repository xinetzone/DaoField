# NiceGUI CSS 变量

您可以通过设置 CSS 变量来自定义 NiceGUI 的外观。目前，以下变量及其默认值可用：

- `--nicegui-default-padding: 1rem`
- `--nicegui-default-gap: 1rem`

```python
from nicegui import ui

ui.add_style('''
    :root {
        --nicegui-default-padding: 0.5rem;
        --nicegui-default-gap: 3rem;
    }
''')
with ui.card():
    ui.label('small padding')
    ui.label('large gap')

# ui.run()
```
