# {func}`~nicegui.ui.spinner` 转轮

这个元素基于Quasar的[QSpinner组件](https://quasar.dev/vue-components/spinners)。

- `type`: 转轮的类型（例如：`"audio"`、`"ball"`、`"bars"` 等，默认：`"default"`）
- `size`: 转轮的大小（例如：`"3em"`、"10px"、"xl"等，默认："1em"）
- `color`: 转轮的颜色（可以是Quasar、Tailwind或CSS颜色，或者 `None`，默认：`"primary"`）
- `thickness`: 转轮的厚度（仅适用于 `"default"` 类型的转轮，默认：`5.0`）

```python
from nicegui import ui

with ui.row():
    ui.spinner(size='lg')
    ui.spinner('audio', size='lg', color='green')
    ui.spinner('dots', size='lg', color='red')

# ui.run()
```
