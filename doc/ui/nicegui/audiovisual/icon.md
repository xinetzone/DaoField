# {func}`nicegui.ui.icon` [图标](https://nicegui.io/documentation/icon)

此元素基于Quasar的[QIcon](https://quasar.dev/vue-components/icon)组件。

[这里](https://fonts.google.com/icons?icon.set=Material+Icons)是可能名称的参考。

- `name`：图标的名称（snake 命名，例如 `add_circle`）
- `size`：CSS 单位中的大小，包括单位名称或标准大小名称（`xs|sm|md|lg|xl`），示例：`16px, 2rem`
- `color`：图标颜色（可以是 Quasar、Tailwind 或 CSS 颜色，或者是 `None`，默认值：`None`）

```python
from nicegui import ui

ui.icon('thumb_up', color='primary').classes('text-5xl')

# ui.run()
```

## {func}`nicegui.ui.icon` 材料图标和符号

您可以使用不同集合的材料图标和符号。[Quasar文档](https://quasar.dev/vue-components/icon#webfont-usage)概述了所有可用的图标集及其名称前缀：

* `None` 用于 [填充图标](https://fonts.google.com/icons?icon.set=Material+Icons&icon.style=Filled)
* `"o_"` 用于 [轮廓图标](https://fonts.google.com/icons?icon.set=Material+Icons&icon.style=Outlined)
* `"r_"` 用于 [圆角图标](https://fonts.google.com/icons?icon.set=Material+Icons&icon.style=Rounded)
* `"s_"` 用于 [锐利图标](https://fonts.google.com/icons?icon.set=Material+Icons&icon.style=Sharp)
* `"sym_o_"` 用于 [轮廓符号](https://fonts.google.com/icons?icon.set=Material+Symbols&icon.style=Outlined)
* "`sym_r_"` 用于 [圆角符号](https://fonts.google.com/icons?icon.set=Material+Symbols&icon.style=Rounded)
* `"sym_s_"` 用于 [锐利符号](https://fonts.google.com/icons?icon.set=Material+Symbols&icon.style=Sharp)

```python
from nicegui import ui

with ui.row().classes('text-4xl'):
    ui.icon('home')
    ui.icon('o_home')
    ui.icon('r_home')
    ui.icon('sym_o_home')
    ui.icon('sym_r_home')

# ui.run()
```

## {func}`nicegui.ui.icon` Eva 图标

您可以在应用程序中使用[Eva图标](https://akveo.github.io/eva-icons/)。

```python
from nicegui import ui

ui.add_head_html('<link href="https://unpkg.com/eva-icons@1.1.3/style/eva-icons.css" rel="stylesheet" />')

ui.icon('eva-github').classes('text-5xl')

# ui.run() 
```

## {func}`nicegui.ui.icon` 其他图标集

您可以使用相同的方法将其他图标集添加到您的应用程序中。一般来说，您需要引用相应的CSS文件，而该CSS文件会进一步引用字体文件。此演示展示了如何包含[Themify图标](https://themify.me/themify-icons)。

```python
from nicegui import ui

ui.add_head_html('<link href="https://cdn.jsdelivr.net/themify-icons/0.1.2/css/themify-icons.css" rel="stylesheet" />')

ui.icon('ti-car').classes('text-5xl')

# ui.run()
```

## {func}`nicegui.ui.icon` Lottie 文件

您还可以使用[Lottie文件](https://lottiefiles.com/)与动画一起。

```python
from nicegui import ui

ui.add_body_html('<script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>')

src = 'https://assets5.lottiefiles.com/packages/lf20_MKCnqtNQvg.json'
ui.html(f'<lottie-player src="{src}" loop autoplay />').classes('w-24')

# ui.run()
```
