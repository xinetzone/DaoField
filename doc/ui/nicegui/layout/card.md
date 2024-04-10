# {func}`~nicegui.ui.card` 卡片

这个元素基于 Quasar 的 [QCard 组件](https://quasar.dev/vue-components/card)。它提供了带有阴影的容器。

注意：Quasar 组件和这个元素之间有一些细微差别。与这个元素相比，原始的 QCard 默认没有内边距，并且隐藏了嵌套元素的外部边框。如果您想要原始的行为，请使用 `tight` 方法。如果您希望嵌套子元素具有内边距和边框，请将子元素移动到另一个容器中。

```python
from nicegui import ui

with ui.card().tight():
    ui.image('https://picsum.photos/id/684/640/360')
    with ui.card_section():
        ui.label('Lorem ipsum dolor sit amet, consectetur adipiscing elit, ...')

# ui.run()
```

## NiceGUI 无阴影卡片

您可以通过添加 `no-shadow` 类来从卡片中移除阴影。以下演示展示了一个宽度为 1 像素的边框。

```python
from nicegui import ui

with ui.card().classes('no-shadow border-[1px]'):
    ui.label('See, no shadow!')

# ui.run()
```

## NiceGUI 嵌套边框问题

以下示例展示了一个嵌套在卡片中的表格。NiceGUI 中的卡片具有默认内边距，因此表格与卡片的边框不齐平。表格设置了 `flat` 和 `bordered` 属性，因此它应该有一个边框。然而，由于 QCard 的设计方式，边框不可见（第一个卡片）。有两种方法可以解决这个问题：

要获得原始的 QCard 行为，请使用 `tight` 方法（第二个卡片）。它会移除内边距，表格边框与卡片边框合并。

要保留内边距和表格边框，请将表格移动到另一个容器中，如 ui.row（第三个卡片）。

有关更多信息，请参阅 <https://github.com/zauberzeug/nicegui/issues/726>。

```python
from nicegui import ui

columns = [{'name': 'age', 'label': 'Age', 'field': 'age'}]
rows = [{'age': '16'}, {'age': '18'}, {'age': '21'}]

with ui.row():
    with ui.card():
        ui.table(columns, rows).props('flat bordered')

    with ui.card().tight():
        ui.table(columns, rows).props('flat bordered')

    with ui.card():
        with ui.row():
            ui.table(columns, rows).props('flat bordered')

# ui.run()
```
