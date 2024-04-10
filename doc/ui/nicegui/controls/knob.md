# {func}`~nicegui.ui.knob`

这个元素是基于Quasar框架中的[`QKnob`组件](https://quasar.dev/vue-components/knob)。该元素用于通过鼠标/触摸平移从用户那里获取数字输入。

- `value`: 初始值（默认：`0.0`）
- `min`: 最小值（默认：`0.0`）
- `max`: 最大值（默认：`1.0`）
- `step`: 步长（默认：`0.01`）
- `color`: 旋钮颜色（可以是Quasar、Tailwind或CSS颜色，或者 `None`，默认：`"primary"`）
- `center_color`: 组件中心部分的颜色名称，示例：`primary`, `teal-10`
- `track_color`: 组件轨道的颜色名称，示例：`primary`, `teal-10`
- `size`: CSS单位大小，包括单位名称或标准大小名称（`xs|sm|md|lg|xl`），示例：`16px, 2rem`
- `show_value`: 是否以文本形式显示值
- `on_change`: 值改变时执行的回调函数

```python
from nicegui import ui

knob = ui.knob(0.3, show_value=True)

with ui.knob(color='orange', track_color='grey-2').bind_value(knob, 'value'):
    ui.icon('volume_up')

# ui.run()
```
