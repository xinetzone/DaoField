# {func}`~nicegui.ui.expansion` 扩展元素

基于 Quasar 的 [QExpansionItem](https://quasar.dev/vue-components/expansion-item) 组件，提供了一个可展开的容器。

- `text`：标题文字
- `caption`：可选的副标题（或子标签）文字
- `icon`：可选的图标（默认：`None`）
- `group`：可选的组名，用于在组内协调打开/关闭状态，也称为“手风琴模式”
- `value`：创建时是否应展开扩展（默认：`False`）
- `on_value_change`：值改变时要执行的回调函数

```python
from nicegui import ui

with ui.expansion('Expand!', icon='work').classes('w-full'):
    ui.label('inside the expansion')

# ui.run()
```

## {func}`~nicegui.ui.expansion` 带有自定义表头的扩展

除了设置纯文本标题，您还可以通过将 UI 元素添加到 `"header"` 插槽中来填充扩展表头。

```python
from nicegui import ui

with ui.expansion() as expansion:
    with expansion.add_slot('header'):
        ui.image('https://nicegui.io/logo.png').classes('w-16')
    ui.label('What a nice GUI!')

# ui.run()
```

## {func}`~nicegui.ui.expansion` 带有自定义副标题的扩展

可以在标题下方添加副标题或子标签。

```python
from nicegui import ui

with ui.expansion('Expand!', caption='Expansion Caption').classes('w-full'):
    ui.label('inside the expansion')

# ui.run()
```

## {func}`~nicegui.ui.expansion` 带有分组的扩展

可以定义一个扩展组，以启用协调的打开/关闭状态，也称为“手风琴模式”。

```python
from nicegui import ui

with ui.expansion(text='Expand One!', group='group'):
    ui.label('inside expansion one')
with ui.expansion(text='Expand Two!', group='group'):
    ui.label('inside expansion two')
with ui.expansion(text='Expand Three!', group='group'):
    ui.label('inside expansion three')

# ui.run()
```
