# {func}`~nicegui.ui.space` 空间 

这个元素基于 Quasar 的 [QSpace 组件](https://quasar.dev/vue-components/space)。

它的目的是简单地填充 flexbox 元素内的所有可用空间。

```python
from nicegui import ui

with ui.row().classes('w-full border'):
    ui.label('Left')
    ui.space()
    ui.label('Right')

# ui.run()
```

## {func}`~nicegui.ui.space` 垂直空间

这个元素也可以用来填充垂直空间。

```python
from nicegui import ui

with ui.column().classes('h-32 border'):
    ui.label('Top')
    ui.space()
    ui.label('Bottom')

# ui.run()
```
