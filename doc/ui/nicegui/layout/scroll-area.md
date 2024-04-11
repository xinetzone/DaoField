# {func}`~nicegui.ui.scroll_area` 滚动区域

通过封装内容来自定义滚动条。此元素公开了 Quasar [ScrollArea](https://quasar.dev/vue-components/scroll-area/) 组件。

`on_scroll`：滚动位置改变时要调用的函数

```python
from nicegui import ui

with ui.row():
    with ui.scroll_area().classes('w-32 h-32 border'):
        ui.label('I scroll. ' * 20)
    with ui.column().classes('p-4 w-32 h-32 border'):
        ui.label('I will not scroll. ' * 10)

# ui.run()
```

## {func}`~nicegui.ui.scroll_area` 处理滚动事件

您可以在 `ui.scroll_area` 中使用 `on_scroll` 参数来处理滚动事件。回调函数会接收一个带有以下属性的 `ScrollEventArguments` 对象：

- `sender`：生成事件的滚动区域
- `client`：匹配的客户端
- 其他参数如 Quasar 文档中针对 [ScrollArea API 所述](https://quasar.dev/vue-components/scroll-area/#qscrollarea-api)

```python
from nicegui import ui

position = ui.number('scroll position:').props('readonly')
with ui.card().classes('w-32 h-32'):
    with ui.scroll_area(on_scroll=lambda e: position.set_value(e.vertical_percentage)):
        ui.label('I scroll. ' * 20)

# ui.run()
```

## {func}`~nicegui.ui.scroll_area` 设置滚动位置

您可以使用 `scroll_to` 来以编程方式设置滚动位置。这对于导航或多个滚动区域的同步非常有用。

```python
from nicegui import ui

ui.number('position', value=0, min=0, max=1, step=0.1,
          on_change=lambda e: area1.scroll_to(percent=e.value)).classes('w-32')

with ui.row():
    with ui.card().classes('w-32 h-48'):
        with ui.scroll_area(on_scroll=lambda e: area2.scroll_to(percent=e.vertical_percentage)) as area1:
            ui.label('I scroll. ' * 20)

    with ui.card().classes('w-32 h-48'):
        with ui.scroll_area() as area2:
            ui.label('I scroll. ' * 20)

# ui.run()
```
