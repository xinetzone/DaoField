# {func}`~nicegui.ui.circular_progress` 环形进度条

环形进度条，包装了Quasar的[QCircularProgress](https://quasar.dev/vue-components/circular-progress)。

- `value`: 字段的初始值
- `min`: 最小值（默认：`0.0`）
- `max`: 最大值（默认：`1.0`）
- `size`: 进度圈的大小（默认：`"xl"`）
- `show_value`: 是否在中心显示值标签（默认：`True`）
- `color`: 颜色（可以是Quasar、Tailwind或CSS颜色，或者None，默认：`"primary"`）

```python
from nicegui import ui

slider = ui.slider(min=0, max=1, step=0.01, value=0.5)
ui.circular_progress().bind_value_from(slider, 'value')

# ui.run()
```

## {func}`~nicegui.ui.circular_progress` 嵌套元素

您可以使用 `with` 语句，在环形进度条中放置任何元素，如图标、按钮等。只需确保它适应边界并禁用显示值的默认行为。

```python
from nicegui import ui

with ui.row().classes('items-center m-auto'):
    with ui.circular_progress(value=0.1, show_value=False) as progress:
        ui.button(
            icon='star',
            on_click=lambda: progress.set_value(progress.value + 0.1)
        ).props('flat round')
    ui.label('click to increase progress')

# ui.run()
```
