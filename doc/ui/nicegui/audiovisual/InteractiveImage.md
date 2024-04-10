# {func}`~nicegui.ui.interactive_image` 可交互图像

翻译创建一个带有SVG叠加层的图像，该图像处理鼠标事件并产生图像坐标。它也是无闪烁图像更新的最佳选择。如果源URL的变化速度比浏览器加载图像的速度快，那么一些图像将被简单地跳过。因此，反复更新图像源将自动适应可用带宽。有关示例，请参见[OpenCV Webcam](https://github.com/zauberzeug/nicegui/tree/main/examples/opencv_webcam/main.py)。

翻译鼠标事件处理程序通过包含以下内容的鼠标事件参数进行调用：

- `type`（JavaScript事件的名称）
- `image_x` 和 `image_y`（以像素为单位的图像坐标）
- `button` 和 `buttons`（来自JavaScript事件的鼠标按钮编号），以及
- `alt`、`ctrl`、`meta` 和 `shift`（来自JavaScript事件的修饰键）

您也可以传递宽度和高度的元组代替图像源。这将创建一个给定大小的空白图像。

- `source`: 图像的来源；可以是URL、本地文件路径、`base64` 字符串或者仅仅是图像大小
- `content`: 应该叠加的SVG内容；视口具有与图像相同的尺寸
- `size`: 图像的大小（宽度、高度）以像素为单位；仅在未设置 `source` 时使用
- `on_mouse`: 鼠标事件的回调函数（包含以像素为单位的图像坐标 `image_x` 和 `image_y`）
- `events`: 要订阅的JavaScript事件列表（默认值：`['click']`）
- `cross`: 是否显示十字准线或颜色字符串（默认值：`False`）

```python
from nicegui import events, ui

def mouse_handler(e: events.MouseEventArguments):
    color = 'SkyBlue' if e.type == 'mousedown' else 'SteelBlue'
    ii.content += f'<circle cx="{e.image_x}" cy="{e.image_y}" r="15" fill="none" stroke="{color}" stroke-width="4" />'
    ui.notify(f'{e.type} at ({e.image_x:.1f}, {e.image_y:.1f})')

src = 'https://picsum.photos/id/565/640/360'
ii = ui.interactive_image(src, on_mouse=mouse_handler, events=['mousedown', 'mouseup'], cross=True)

# ui.run()
```

## {func}`~nicegui.ui.interactive_image` 嵌套元素

您可以在交互式图像内部嵌套元素。使用Tailwind类，如 `"absolute top-0 left-0"`，可以相对于图像绝对定位标签。当然，也可以使用普通的CSS来完成。

```python
from nicegui import ui

with ui.interactive_image('https://picsum.photos/id/147/640/360'):
    ui.button(on_click=lambda: ui.notify('thumbs up'), icon='thumb_up') \
        .props('flat fab color=white') \
        .classes('absolute bottom-0 left-0 m-2')

# ui.run()
```

## {func}`~nicegui.ui.interactive_image` 强制重新加载

您可以通过调用 `force_reload` 方法来强制图像重新加载。它将在图像URL后附加一个时间戳，这将使浏览器重新加载图像。


```python
from nicegui import ui

img = ui.interactive_image('https://picsum.photos/640/360').classes('w-64')

ui.button('Force reload', on_click=img.force_reload)

# ui.run()
```

## {func}`~nicegui.ui.interactive_image` 空白画布

您也可以创建一个给定大小的空白画布。如果您想在不加载背景图像的情况下绘制某些内容，这将非常有用。

```python
from nicegui import ui

ui.interactive_image(
    size=(800, 600), cross=True,
    on_mouse=lambda e: e.sender.set_content(f'''
        <circle cx="{e.image_x}" cy="{e.image_y}" r="50" fill="orange" />
    '''),
).classes('w-64 bg-blue-50')

# ui.run()
```

## {func}`~nicegui.ui.interactive_image` 加载完成事件

您可以监听 `"loaded"` 事件，以便知道图像何时已加载完成。

```python
import time
from nicegui import ui

ii = ui.interactive_image('https://picsum.photos/640/360')
ii.on('loaded', lambda e: ui.notify(f'loaded {e.args}'))
ui.button('Change Source', on_click=lambda: ii.set_source(f'https://picsum.photos/640/360?time={time.time()}'))

# ui.run()
```

## {func}`~nicegui.ui.interactive_image` 十字准线

您可以通过传递 `cross=True` 来显示十字准线。您还可以通过传递颜色字符串来更改十字准线的颜色。
```python
from nicegui import ui

ui.interactive_image('https://picsum.photos/id/565/640/360', cross='red')

# ui.run()
```
