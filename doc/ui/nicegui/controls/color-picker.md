# {func}`~nicegui.ui.color_picker` 颜色拾取

`Color Picker` 元素是基于Quasar的 [QMenu](https://quasar.dev/vue-components/menu) 和 [QColor](https://quasar.dev/vue-components/color) 组件。

- `on_pick`: 当选择颜色时执行的回调函数
- `value`: 菜单是否已经打开（默认：`False`）

```python
from nicegui import ui

with ui.button(icon='colorize') as button:
    ui.color_picker(on_pick=lambda e: button.style(f'background-color:{e.color}!important'))

# ui.run()
```
