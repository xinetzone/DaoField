# {func}`nicegui.ui.image` 图像

显示一张图片。这个元素基于 Quasar 的 [QImg 组件](https://quasar.dev/vue-components/img)。

`source`：图像的来源，可以是 URL、本地文件路径、`base64` 字符串或 `PIL` 图像。
```python
from nicegui import ui

ui.image('https://picsum.photos/id/377/640/360')

# ui.run()
```

## {func}`nicegui.ui.image` 本地文件

您也可以通过传递图像文件的路径来使用本地图像。

```python
from nicegui import ui

ui.image('website/static/logo.png').classes('w-16')

# ui.run()
```
## {func}`nicegui.ui.image` Base64 字符串

您也可以使用 Base64 字符串作为图像源。

```python
from nicegui import ui

base64 = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO9TXL0Y4OHwAAAABJRU5ErkJggg=='
ui.image(base64).classes('w-2 h-2 m-auto')

# ui.run()
```

## {func}`nicegui.ui.image` {mod}`PIL` 图像

您也可以使用 `PIL` 图像作为图像源。

```python
import numpy as np
from nicegui import ui
from PIL import Image

image = Image.fromarray(np.random.randint(0, 255, (100, 100), dtype=np.uint8))
ui.image(image).classes('w-32')

# ui.run()
```

## {func}`nicegui.ui.image` Lottie 文件

您还可以使用带有动画的[Lottie文件](https://lottiefiles.com/)。

```python
from nicegui import ui

ui.add_body_html('<script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>')

src = 'https://assets1.lottiefiles.com/datafiles/HN7OcWNnoqje6iXIiZdWzKxvLIbfeCGTmvXmEm1h/data.json'
ui.html(f'<lottie-player src="{src}" loop autoplay />').classes('w-full')

# ui.run()
```

## {func}`nicegui.ui.image` 图像链接

通过将图像包裹在[ui.link](https://nicegui.io/documentation/link)中，图像可以链接到另一个页面。

```python
from nicegui import ui

with ui.link(target='https://github.com/zauberzeug/nicegui'):
    ui.image('https://picsum.photos/id/41/640/360').classes('w-64')

# ui.run()
```

## {func}`nicegui.ui.image` 强制重新加载

您可以通过调用 `force_reload` 方法来强制重新加载图像。它将在图像URL后附加一个时间戳，这将使浏览器重新加载图像。

```python
from nicegui import ui

img = ui.image('https://picsum.photos/640/360').classes('w-64')

ui.button('Force reload', on_click=img.force_reload)

# ui.run()
```

## {func}`nicegui.ui.image` 字幕和叠加层

通过在 `ui.image` 内部嵌套元素，您可以创建增强效果。

使用[Quasar类](https://quasar.dev/vue-components/img)进行字幕的定位和样式设计。要叠加SVG，请使`viewBox`的大小与图像的实际大小完全匹配，并提供`100%`的宽度/高度以匹配实际渲染的大小。

```python
from nicegui import ui

with ui.image('https://picsum.photos/id/29/640/360'):
    ui.label('Nice!').classes('absolute-bottom text-subtitle2 text-center')

with ui.image('https://cdn.stocksnap.io/img-thumbs/960w/airplane-sky_DYPWDEEILG.jpg'):
    ui.html('''
        <svg viewBox="0 0 960 638" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
        <circle cx="445" cy="300" r="100" fill="none" stroke="red" stroke-width="20" />
        </svg>
    ''').classes('bg-transparent')

# ui.run()
```
