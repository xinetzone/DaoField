# {func}`~nicegui.ui.splitter` 分隔器

`ui.splitter` 元素将屏幕空间分割为可调整大小的部分，允许在应用程序中实现灵活和响应式布局。

基于 Quasar 的 Splitter 组件：[Splitter](https://quasar.dev/vue-components/splitter)

它提供三个可定制的插槽，`before`、`after` 和 `separator`，可用于在分隔器内嵌入其他元素。

- `horizontal`：是否水平分割而不是垂直分割
- `limits`：两个数字，表示两个面板的最小和最大分割尺寸
- `value`：第一个面板（或使用 `reverse` 时的第二个）的大小
- `reverse`：是否将模型大小应用于第二个面板而不是第一个
-`on_change`：当用户释放分隔器时调用的回调函数

```python
from nicegui import ui

with ui.splitter() as splitter:
    with splitter.before:
        ui.label('This is some content on the left hand side.').classes('mr-2')
    with splitter.after:
        ui.label('This is some content on the right hand side.').classes('ml-2')

# ui.run()
```

## {func}`~nicegui.ui.splitter` 高级用法

此演示展示了所有插槽和参数，包括一个工具提示、一个自定义分隔符和一个回调函数。

```python
from nicegui import ui

with ui.splitter(horizontal=False, reverse=False, value=60,
                 on_change=lambda e: ui.notify(e.value)) as splitter:
    ui.tooltip('This is the default slot.').classes('bg-green')
    with splitter.before:
        ui.label('This is the left hand side.').classes('mr-2')
    with splitter.after:
        ui.label('This is the right hand side.').classes('ml-2')
    with splitter.separator:
        ui.icon('lightbulb').classes('text-green')

ui.number('Split value', format='%.1f').bind_value(splitter)

# ui.run()
```

## {func}`~nicegui.ui.splitter` 图片乐趣

此演示展示了如何使用分隔器并排显示图像。

```python
from nicegui import ui

with ui.splitter().classes('w-72 h-48') \
        .props('before-class=overflow-hidden after-class=overflow-hidden') as splitter:
    with splitter.before:
        ui.image('https://cdn.quasar.dev/img/parallax1.jpg').classes('w-72 absolute-top-left')
    with splitter.after:
        ui.image('https://cdn.quasar.dev/img/parallax1-bw.jpg').classes('w-72 absolute-top-right')

# ui.run()
```
