# {func}`~nicegui.ui.tree` 树

使用Quasar的[QTree](https://quasar.dev/vue-components/tree)组件显示层次数据。

如果使用 `ID`，确保它们在整个树中是唯一的。

要使用复选框和 `on_tick`，请将 `tick_strategy` 参数设置为 `"leaf"`、`"leaf-filtered"`或`"strict"`。

- `nodes`: 节点对象的分层列表
- `node_key`: 每个节点对象的属性名，用于存储其唯一id（默认：`"id"`）
- `label_key`: 每个节点对象的属性名，用于存储其标签（默认：`"label"`）
- `children_key`: 每个节点对象的属性名，用于存储其子列表（默认：`"children"`）
- `on_select`: 当节点选择改变时调用的回调函数
- `on_expand`: 当节点展开状态改变时调用的回调函数
- `on_tick`: 当节点被勾选或取消勾选时调用的回调函数
- `tick_strategy`: 是否以及如何使用复选框（`"leaf"`、`"leaf-filtered"`或`"strict"`；默认：`None`）

```python
from nicegui import ui

ui.tree([
    {'id': 'numbers', 'children': [{'id': '1'}, {'id': '2'}]},
    {'id': 'letters', 'children': [{'id': 'A'}, {'id': 'B'}]},
], label_key='id', on_select=lambda e: ui.notify(e.value))

# ui.run()
```

## 自定义树冠和树干

树节点的头部和主体可以使用作用域插槽来插入自定义内容。更多信息请参阅[Quasar文档](https://quasar.dev/vue-components/tree#customize-content)。

```python
from nicegui import ui

tree = ui.tree([
    {'id': 'numbers', 'description': 'Just some numbers', 'children': [
        {'id': '1', 'description': 'The first number'},
        {'id': '2', 'description': 'The second number'},
    ]},
    {'id': 'letters', 'description': 'Some latin letters', 'children': [
        {'id': 'A', 'description': 'The first letter'},
        {'id': 'B', 'description': 'The second letter'},
    ]},
], label_key='id', on_select=lambda e: ui.notify(e.value))

tree.add_slot('default-header', '''
    <span :props="props">Node <strong>{{ props.node.id }}</strong></span>
''')
tree.add_slot('default-body', '''
    <span :props="props">Description: "{{ props.node.description }}"</span>
''')

# ui.run()
```

## 编程式的展开和折叠

整个树或单个节点可以使用 `expand()` 和 `collapse()` 方法进行编程式的展开和折叠。即使节点被禁用（例如，用户无法点击），这也同样适用。

```python
from nicegui import ui

t = ui.tree([
    {'id': 'A', 'children': [{'id': 'A1'}, {'id': 'A2'}], 'disabled': True},
    {'id': 'B', 'children': [{'id': 'B1'}, {'id': 'B2'}]},
], label_key='id').expand()

with ui.row():
    ui.button('+ all', on_click=t.expand)
    ui.button('- all', on_click=t.collapse)
    ui.button('+ A', on_click=lambda: t.expand(['A']))
    ui.button('- A', on_click=lambda: t.collapse(['A']))

# ui.run()
```

## 带有复选框的树

通过设置 `"tick-strategy"` 属性，树可以与复选框一起使用。

```python
from nicegui import ui

ui.tree([
    {'id': 'A', 'children': [{'id': 'A1'}, {'id': 'A2'}]},
    {'id': 'B', 'children': [{'id': 'B1'}, {'id': 'B2'}]},
], label_key='id', tick_strategy='leaf', on_tick=lambda e: ui.notify(e.value))

# ui.run()
```
