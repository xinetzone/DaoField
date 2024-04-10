# {func}`~nicegui.ui.colors` 颜色主题

设置 [Quasar](https://quasar.dev/) 使用的主要颜色（primary, secondary, accent等）。

```python
from nicegui import ui

ui.button('Default', on_click=lambda: ui.colors())
ui.button('Gray', on_click=lambda: ui.colors(primary='#555'))

# ui.run()
```
