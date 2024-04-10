# {func}`~nicegui.ui.avatar` 头像

包装 Quasar 的 [QAvatar](https://quasar.dev/vue-components/avatar) 组件的头像元素。

- `icon`：图标的名称或带有"img:"前缀的图像路径（例如`"map"`, `"img:path/to/image.png"`）
- `color`：背景颜色（可以是Quasar、Tailwind或CSS颜色，或者`None`，默认值：`"primary"`）
- `text_color`：来自Quasar色彩调色板的颜色名称（例如`"primary"`, `"teal-10"`）
- `size`：CSS单位中的大小，包括单位名称或标准大小名称（`xs|sm|md|lg|xl`）（例如`"16px"`, `"2rem"`）
- `font_size`：内容（图标，文字）的CSS单位大小，包括单位名称（例如`"18px"`, `"2rem"`）
- `square`：移除border-radius以使边框成方形（默认值：`False`）
- `rounded`：为组件的方形形状应用一个小的标准 `border-radius`（默认值：`False`）

```python
from nicegui import ui

ui.avatar('favorite_border', text_color='grey-11', square=True)
ui.avatar('img:https://nicegui.io/logo_square.png', color='blue-2')

# ui.run()
```

## {func}`~nicegui.ui.avatar` 照片

要使用照片作为头像，您可以在 `ui.avatar` 内使用 `ui.image`。

```python
from nicegui import ui

with ui.avatar():
    ui.image('https://robohash.org/robot?bgset=bg2')

# ui.run()
```
