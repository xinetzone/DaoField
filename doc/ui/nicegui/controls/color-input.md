# {func}`~nicegui.ui.color_input` 颜色输入

`Color Input` 元素扩展了 Quasar 的 [QInput](https://quasar.dev/vue-components/input) 组件，增加了颜色选择器。

- `label`: 颜色输入的显示标签
-`placeholder`: 如果没有选择颜色，显示的文本
- `value`: 当前的颜色值
- `on_change`: 当值改变时执行的回调函数
- `preview`: 将更改按钮背景变为所选颜色（默认：`False`）

```python
from nicegui import ui

label = ui.label('Change my color!')
ui.color_input(label='Color', value='#000000',
               on_change=lambda e: label.style(f'color:{e.value}'))

# ui.run()
```
