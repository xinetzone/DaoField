# {func}`~nicegui.ui.list` 列表

基于 Quasar 的 [QList](https://quasar.dev/vue-components/list-and-list-items#qlist-api) 组件的列表元素。它为列表项提供了一个容器。

```python
from nicegui import ui

with ui.list().props('dense separator'):
    with ui.item():
        with ui.item_section():
            ui.item_label('3 Apples')
    with ui.item():
        with ui.item_section():
            ui.item_label('5 Bananas')
    with ui.item():
        with ui.item_section():
            ui.item_label('8 Strawberries')
    with ui.item():
        with ui.item_section():
            ui.item_label('13 Walnuts')

# ui.run()
```

## {func}`~nicegui.ui.list` 列表项、分区和标签

列表项使用项目分区来组织其内容。根据属性的不同，项目标签的位置也不同。

```python
from nicegui import ui

with ui.list().props('bordered separator'):
    ui.item_label('Contacts').props('header').classes('text-bold')
    ui.separator()
    with ui.item(on_click=lambda: ui.notify('Selected contact 1')):
        with ui.item_section().props('avatar'):
            ui.icon('person')
        with ui.item_section():
            ui.item_label('Nice Guy')
            ui.item_label('name').props('caption')
        with ui.item_section().props('side'):
            ui.icon('chat')
    with ui.item(on_click=lambda: ui.notify('Selected contact 2')):
        with ui.item_section().props('avatar'):
            ui.icon('person')
        with ui.item_section():
            ui.item_label('Nice Person')
            ui.item_label('name').props('caption')
        with ui.item_section().props('side'):
            ui.icon('chat')

# ui.run()
```
