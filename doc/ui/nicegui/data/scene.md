# {func}`~nicegui.ui.scene` 3D 场景

使用 [`three.js`](https://threejs.org/)显示一个3D场景。目前NiceGUI支持盒子、球体、圆柱/圆锥、挤压、直线、曲线和纹理网格对象。对象可以进行平移、旋转，并以不同的颜色、不透明度或线框形式显示。它们也可以分组以应用联合运动。

- `width`: 画布的宽度
- `height`: 画布的高度
- `grid`: 是否显示网格
- `on_click`: 当点击3D对象时执行的回调函数
- `on_drag_start`: 当拖动3D对象时执行的回调函数
- `on_drag_end`: 当放下3D对象时执行的回调函数
- `drag_constraints`: 用于限制拖动对象位置的逗号分隔的JavaScript表达式（例如`'x = 0, z = y / 2'`）

```python
from nicegui import ui

with ui.scene().classes('w-full h-64') as scene:
    scene.sphere().material('#4488ff')
    scene.cylinder(1, 0.5, 2, 20).material('#ff8800', opacity=0.5).move(-2, 1)
    scene.extrusion([[0, 0], [0, 1], [1, 0.5]], 0.1).material('#ff8888').move(2, -1)

    with scene.group().move(z=2):
        scene.box().move(x=2)
        scene.box().move(y=2).rotate(0.25, 0.5, 0.75)
        scene.box(wireframe=True).material('#888888').move(x=2, y=2)

    scene.line([-4, 0, 0], [-4, 2, 0]).material('#ff0000')
    scene.curve([-4, 0, 0], [-4, -1, 0], [-3, -1, 0], [-3, 0, 0]).material('#008800')

    logo = 'https://avatars.githubusercontent.com/u/2843826'
    scene.texture(logo, [[[0.5, 2, 0], [2.5, 2, 0]],
                         [[0.5, 0, 0], [2.5, 0, 0]]]).move(1, -3)

    teapot = 'https://upload.wikimedia.org/wikipedia/commons/9/93/Utah_teapot_(solid).stl'
    scene.stl(teapot).scale(0.2).move(-3, 4)

    avocado = 'https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/Avocado/glTF-Binary/Avocado.glb'
    scene.gltf(avocado).scale(40).move(-2, -3, 0.5)

    scene.text('2D', 'background: rgba(0, 0, 0, 0.2); border-radius: 5px; padding: 5px').move(z=2)
    scene.text3d('3D', 'background: rgba(0, 0, 0, 0.2); border-radius: 5px; padding: 5px').move(y=-2).scale(.05)

# ui.run()
```

## {func}`~nicegui.ui.scene` 处理点击事件

您可以使用 `ui.scene` 的 `on_click` 参数来处理点击事件。回调函数会接收一个 `SceneClickEventArguments` 对象，该对象具有以下属性：

- `click_type`: 点击类型（`"click"`或`"dblclick"`）。
- `button`: 被点击的按钮（`1`、`2`或`3`）。
- `alt, ctrl, meta, shift`: `alt`、`ctrl`、`meta`或`shift`键是否被按下。
- `hits`: 按距离摄像机的距离排序的`SceneClickEventHit`对象列表。

`SceneClickEventHit`对象具有以下属性：

- `object_id`: 被点击对象的id。
- `object_name`: 被点击对象的名称。
- `x, y, z`: 点击的`x`、`y`和`z`坐标。

```python
from nicegui import events, ui

def handle_click(e: events.SceneClickEventArguments):
    hit = e.hits[0]
    name = hit.object_name or hit.object_id
    ui.notify(f'You clicked on the {name} at ({hit.x:.2f}, {hit.y:.2f}, {hit.z:.2f})')

with ui.scene(width=285, height=220, on_click=handle_click) as scene:
    scene.sphere().move(x=-1, z=1).with_name('sphere')
    scene.box().move(x=1, z=1).with_name('box')

# ui.run()
```

## {func}`~nicegui.ui.scene` 可拖曳对象

您可以使用`.draggable`方法使对象可拖动。`ui.scene`有一个可选的`on_drag_start`和`on_drag_end`参数来处理拖动事件。回调函数会接收一个`SceneDragEventArguments`对象，该对象具有以下属性：

- `type`: 拖动事件的类型（"dragstart"或"dragend"）。
- `object_id`: 被拖动对象的`id`。
- `object_name`: 被拖动对象的名称。
- `x, y, z`: 被拖动对象的`x`、`y`和`z`坐标。

您还可以使用`drag_constraints`参数设置逗号分隔的JavaScript表达式，用于限制被拖动对象的位置。

```python
from nicegui import events, ui

def handle_drag(e: events.SceneDragEventArguments):
    ui.notify(f'You dropped the sphere at ({e.x:.2f}, {e.y:.2f}, {e.z:.2f})')

with ui.scene(width=285, height=220,
              drag_constraints='z = 1', on_drag_end=handle_drag) as scene:
    sphere = scene.sphere().move(z=1).draggable()

ui.switch('draggable sphere',
          value=sphere.draggable_,
          on_change=lambda e: sphere.draggable(e.value))

# ui.run()
```

## {func}`~nicegui.ui.scene` 渲染点云

您可以使用 `point_cloud` 方法渲染点云。`points` 参数是一个点坐标的列表，`colors`参数是 RGB 颜色（0..1）的列表。

```python
import numpy as np
from nicegui import ui

with ui.scene().classes('w-full h-64') as scene:
    x, y = np.meshgrid(np.linspace(-3, 3), np.linspace(-3, 3))
    z = np.sin(x) * np.cos(y) + 1
    points = np.dstack([x, y, z]).reshape(-1, 3)
    scene.point_cloud(points=points, colors=points, point_size=0.1)

# ui.run()
```

## {func}`~nicegui.ui.scene` 等待场景初始化

您可以使用 `initialized` 方法等待场景初始化。这个演示在场景完全加载后动画化相机移动。

```python
from nicegui import ui

with ui.scene(width=285, height=220) as scene:
    scene.sphere()
    await scene.initialized()
    scene.move_camera(x=1, y=-1, z=1.5, duration=2)

ui.run()
```
