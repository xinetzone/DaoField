# {func}`~nicegui.ui.slider` 线性进度条

线性进度条，包装了Quasar的[QLinearProgress组件](https://quasar.dev/vue-components/linear-progress)。

- `value`: 字段的初始值（从`0.0`到`1.0`）
- `size`: 进度条的高度（默认：带值标签时为`"20px"`，不带时为`"4px"`）
- `show_value`: 是否在中心显示值标签（默认：True）
- `color`: 颜色（可以是Quasar、Tailwind或CSS颜色，或者 `None`，默认：`"primary"`）

```python
from nicegui import ui

slider = ui.slider(min=0, max=1, step=0.01, value=0.5)
ui.linear_progress().bind_value_from(slider, 'value')

# ui.run()
```
