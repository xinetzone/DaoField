# {func}`~nicegui.ui.tooltip` 工具提示

这个元素基于 Quasar 的 [QTooltip 组件](https://quasar.dev/vue-components/tooltip)。它可以放置在另一个元素内，以在悬停时显示额外信息。

除了将字符串作为第一个参数传递外，您还可以在工具提示内嵌套其他元素。

`text`：工具提示的内容（默认为 `''`）

```python
from nicegui import ui

with ui.button(icon='thumb_up'):
    ui.tooltip('I like this').classes('bg-green')

# ui.run()
```

## {func}`~nicegui.ui.tooltip` 工具提示方法

除了将工具提示元素嵌套在另一个元素内，您也可以使用工具提示方法。

```python
from nicegui import ui

ui.label('Tooltips...').tooltip('...are shown on mouse over')

# ui.run()
```

## {func}`~nicegui.ui.tooltip` 工具提示中的 HTML

您可以通过嵌套一个 `ui.html` 元素在工具提示中使用 HTML。

```python
from nicegui import ui

with ui.label('HTML...'):
    with ui.tooltip():
        ui.html('<b>b</b>, <em>em</em>, <u>u</u>, <s>s</s>')

# ui.run()
```

## {func}`~nicegui.ui.tooltip` 工具提示中的其他内容

您可以在工具提示中使用 HTML。

```python
from nicegui import ui

with ui.label('Mountains...'):
    with ui.tooltip().classes('bg-transparent'):
        ui.image('https://picsum.photos/id/377/640/360').classes('w-64')

# ui.run()
```

## {func}`~nicegui.ui.tooltip` HTML 和 Markdown 上的工具提示

一些元素，如 `ui.html` 和 `ui.markdown`，不支持嵌套元素。在这种情况下，您可以将此类元素嵌套在一个带有工具提示的容器元素内。

```python
from nicegui import ui

with ui.element().tooltip('...with a tooltip!'):
    ui.html('This is <u>HTML</u>...')

# ui.run()
```
