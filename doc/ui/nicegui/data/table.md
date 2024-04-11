# {func}`nicegui.ui.table` 表格

基于Quasar的[QTable组件](https://quasar.dev/vue-components/table)的表格。

- `columns`: 列对象列表
- `rows`: 行对象列表
- `row_key`: 包含唯一数据以标识行的列的名称（默认：`"id"`）
- `title`: 表格的标题
- `selection`: 选择类型（`"single"`或`"multiple"`；默认：`None`）
- `pagination`: 与分页对象或每页行数相关的字典（None隐藏分页，0表示"无限"；默认：`None`）。
- `on_select`: 当选择改变时调用的回调函数
- `on_pagination_change`: 当分页改变时调用的回调函数

如果选择是`'single'`或`'multiple'`，那么可以访问包含所选行的属性`selected`。

```python
from nicegui import ui

columns = [
    {'name': 'name', 'label': 'Name', 'field': 'name', 'required': True, 'align': 'left'},
    {'name': 'age', 'label': 'Age', 'field': 'age', 'sortable': True},
]
rows = [
    {'name': 'Alice', 'age': 18},
    {'name': 'Bob', 'age': 21},
    {'name': 'Carol'},
]
ui.table(columns=columns, rows=rows, row_key='name')

# ui.run()
```

## {func}`nicegui.ui.table` 具有可展开行的表格

可以使用作用域插槽插入按钮，以切换表格行的展开状态。有关更多信息，请参阅[Quasar文档](https://quasar.dev/vue-components/table#expanding-rows)。

```python
from nicegui import ui

columns = [
    {'name': 'name', 'label': 'Name', 'field': 'name'},
    {'name': 'age', 'label': 'Age', 'field': 'age'},
]
rows = [
    {'name': 'Alice', 'age': 18},
    {'name': 'Bob', 'age': 21},
    {'name': 'Carol'},
]

table = ui.table(columns=columns, rows=rows, row_key='name').classes('w-72')
table.add_slot('header', r'''
    <q-tr :props="props">
        <q-th auto-width />
        <q-th v-for="col in props.cols" :key="col.name" :props="props">
            {{ col.label }}
        </q-th>
    </q-tr>
''')
table.add_slot('body', r'''
    <q-tr :props="props">
        <q-td auto-width>
            <q-btn size="sm" color="accent" round dense
                @click="props.expand = !props.expand"
                :icon="props.expand ? 'remove' : 'add'" />
        </q-td>
        <q-td v-for="col in props.cols" :key="col.name" :props="props">
            {{ col.value }}
        </q-td>
    </q-tr>
    <q-tr v-show="props.expand" :props="props">
        <q-td colspan="100%">
            <div class="text-left">This is {{ props.row.name }}.</div>
        </q-td>
    </q-tr>
''')

# ui.run()
```

## {func}`nicegui.ui.table` 显示和隐藏列

这里是一个示例，展示了如何在表格中显示和隐藏列。

```python
from nicegui import ui
from typing import Dict

columns = [
    {'name': 'name', 'label': 'Name', 'field': 'name', 'required': True, 'align': 'left'},
    {'name': 'age', 'label': 'Age', 'field': 'age', 'sortable': True},
]
rows = [
    {'name': 'Alice', 'age': 18},
    {'name': 'Bob', 'age': 21},
    {'name': 'Carol'},
]
table = ui.table(columns=columns, rows=rows, row_key='name')

def toggle(column: Dict, visible: bool) -> None:
    column['classes'] = '' if visible else 'hidden'
    column['headerClasses'] = '' if visible else 'hidden'
    table.update()

with ui.button(icon='menu'):
    with ui.menu(), ui.column().classes('gap-0 p-2'):
        for column in columns:
            ui.switch(column['label'], value=True, on_change=lambda e,
                      column=column: toggle(column, e.value))

# ui.run()
```

## {func}`nicegui.ui.table` 带有下拉选择的表格

这里是一个示例，展示了如何在表格中使用下拉选择。从作用域插槽发出重命名事件后，重命名函数会更新表格行。

```python
from nicegui import events, ui

columns = [
    {'name': 'name', 'label': 'Name', 'field': 'name'},
    {'name': 'age', 'label': 'Age', 'field': 'age'},
]
rows = [
    {'id': 0, 'name': 'Alice', 'age': 18},
    {'id': 1, 'name': 'Bob', 'age': 21},
    {'id': 2, 'name': 'Carol'},
]
name_options = ['Alice', 'Bob', 'Carol']

def rename(e: events.GenericEventArguments) -> None:
    for row in rows:
        if row['id'] == e.args['id']:
            row['name'] = e.args['name']
    ui.notify(f'Table.rows is now: {table.rows}')

table = ui.table(columns=columns, rows=rows).classes('w-full')
table.add_slot('body-cell-name', r'''
    <q-td key="name" :props="props">
        <q-select
            v-model="props.row.name"
            :options="''' + str(name_options) + r'''"
            @update:model-value="() => $parent.$emit('rename', props.row)"
        />
    </q-td>
''')
table.on('rename', rename)

# ui.run()
```

## 从Pandas DataFrame创建 {func}`nicegui.ui.table`

您可以使用`from_pandas`方法从Pandas DataFrame创建一个表格。这个方法接受一个Pandas DataFrame作为输入，并返回一个表格。

```python
import pandas as pd
from nicegui import ui

df = pd.DataFrame(data={'col1': [1, 2], 'col2': [3, 4]})
ui.table.from_pandas(df).classes('max-h-40')

# ui.run()
```

## {func}`nicegui.ui.table` 添加行

使用`add_rows(dict)`方法可以轻松添加新行。

```python
import os
import random
from nicegui import ui

def add():
    item = os.urandom(10 // 2).hex()
    table.add_rows({'id': item, 'count': random.randint(0, 100)})

ui.button('add', on_click=add)
columns = [
    {'name': 'id', 'label': 'ID', 'field': 'id'},
    {'name': 'count', 'label': 'Count', 'field': 'count'},
]
table = ui.table(columns=columns, rows=[], row_key='id').classes('w-full')

# ui.run()
```

## {func}`nicegui.ui.table` 自定义排序和格式化

您可以使用：前缀定义动态列属性。这样，您可以定义自定义排序和格式化函数。

以下示例允许按名称长度对名称列进行排序。年龄列被格式化以显示年龄（以年为单位）。

```python
from nicegui import ui

columns = [
    {
        'name': 'name',
        'label': 'Name',
        'field': 'name',
        'sortable': True,
        ':sort': '(a, b, rowA, rowB) => b.length - a.length',
    },
    {
        'name': 'age',
        'label': 'Age',
        'field': 'age',
        ':format': 'value => value + " years"',
    },
]
rows = [
    {'name': 'Alice', 'age': 18},
    {'name': 'Bob', 'age': 21},
    {'name': 'Carl', 'age': 42},
]
ui.table(columns=columns, rows=rows, row_key='name')

# ui.run()
```

## {func}`nicegui.ui.table` 切换全屏

您可以使用`toggle_fullscreen()`方法切换表格的全屏模式。

```python
from nicegui import ui

table = ui.table(
    columns=[{'name': 'name', 'label': 'Name', 'field': 'name'}],
    rows=[{'name': 'Alice'}, {'name': 'Bob'}, {'name': 'Carol'}],
).classes('w-full')

with table.add_slot('top-left'):
    def toggle() -> None:
        table.toggle_fullscreen()
        button.props('icon=fullscreen_exit' if table.is_fullscreen else 'icon=fullscreen')
    button = ui.button('Toggle fullscreen', icon='fullscreen', on_click=toggle).props('flat')

# ui.run()
```

## {func}`nicegui.ui.table` 表格分页

您可以提供一个整数或一个字典来定义分页。

该字典可以包含以下键：

- `rowsPerPage`: 每页的行数。
- `sortBy`: 要排序的列名。
- `descending`: 是否按降序排序。
- `page`: 当前页（从`1`开始）。

```python
from nicegui import ui

columns = [
    {'name': 'name', 'label': 'Name', 'field': 'name', 'required': True, 'align': 'left'},
    {'name': 'age', 'label': 'Age', 'field': 'age', 'sortable': True},
]
rows = [
    {'name': 'Elsa', 'age': 18},
    {'name': 'Oaken', 'age': 46},
    {'name': 'Hans', 'age': 20},
    {'name': 'Sven'},
    {'name': 'Olaf', 'age': 4},
    {'name': 'Anna', 'age': 17},
]
ui.table(columns=columns, rows=rows, pagination=3)
ui.table(columns=columns, rows=rows, pagination={'rowsPerPage': 4, 'sortBy': 'age', 'page': 2})

# ui.run()
```

## {func}`nicegui.ui.table` 处理分页变化

您可以使用 `on_pagination_change` 参数来处理分页变化。

```python
from nicegui import ui

ui.table(
    columns=[{'id': 'Name', 'label': 'Name', 'field': 'Name', 'align': 'left'}],
    rows=[{'Name': f'Person {i}'} for i in range(100)],
    pagination=3,
    on_pagination_change=lambda e: ui.notify(e.value),
)

# ui.run()
```

## {func}`nicegui.ui.table` 计算字段

您可以使用函数来计算列的值。该函数将行作为参数。有关更多信息，请参阅[Quasar文档](https://quasar.dev/vue-components/table#defining-the-columns)。

```python
from nicegui import ui

columns = [
    {'name': 'name', 'label': 'Name', 'field': 'name', 'align': 'left'},
    {'name': 'length', 'label': 'Length', ':field': 'row => row.name.length'},
]
rows = [
    {'name': 'Alice'},
    {'name': 'Bob'},
    {'name': 'Christopher'},
]
ui.table(columns=columns, rows=rows, row_key='name')

# ui.run()
```

## {func}`nicegui.ui.table` 条件格式化

您可以使用作用域插槽来有条件地格式化单元格的内容。有关body-cell插槽的更多信息，请[参阅Quasar文档](https://quasar.dev/vue-components/table#example--body-cell-slot)。

在这个演示中，我们使用`q-badge`以红色显示21岁以下人员的年龄。我们使用`body-cell-age`插槽将`q-badge`插入年龄列中。如果年龄在21岁以下，则q-badge的`":color"`属性设置为`"red"`，否则设置为`"green"`。`":"color"`属性前的冒号表示该值是一个JavaScript表达式。

```python
from nicegui import ui

columns = [
    {'name': 'name', 'label': 'Name', 'field': 'name'},
    {'name': 'age', 'label': 'Age', 'field': 'age'},
]
rows = [
    {'name': 'Alice', 'age': 18},
    {'name': 'Bob', 'age': 21},
    {'name': 'Carol', 'age': 42},
]
table = ui.table(columns=columns, rows=rows, row_key='name')
table.add_slot('body-cell-age', '''
    <q-td key="age" :props="props">
        <q-badge :color="props.value < 21 ? 'red' : 'green'">
            {{ props.value }}
        </q-badge>
    </q-td>
''')

# ui.run()
```

## {func}`nicegui.ui.table` 表格单元格中的链接

这里是一个演示，展示了如何将链接插入到表格单元格中。我们使用 `body-cell-link` 插槽将 `<a>` 标签插入到链接列中。

```python
from nicegui import ui

columns = [
    {'name': 'name', 'label': 'Name', 'field': 'name', 'align': 'left'},
    {'name': 'link', 'label': 'Link', 'field': 'link', 'align': 'left'},
]
rows = [
    {'name': 'Google', 'link': 'https://google.com'},
    {'name': 'Facebook', 'link': 'https://facebook.com'},
    {'name': 'Twitter', 'link': 'https://twitter.com'},
]
table = ui.table(columns=columns, rows=rows, row_key='name')
table.add_slot('body-cell-link', '''
    <q-td :props="props">
        <a :href="props.value">{{ props.value }}</a>
    </q-td>
''')

# ui.run()
```

## {func}`nicegui.ui.table` 类似砖石布局的表格

您可以使用`grid`属性将表格显示为类似砖石布局的网格。有关更多信息，请参阅[Quasar文档](https://quasar.dev/vue-components/table#grid-style)。

```python
from nicegui import ui

columns = [
    {'name': 'name', 'label': 'Name', 'field': 'name'},
    {'name': 'age', 'label': 'Age', 'field': 'age'},
]
rows = [
    {'name': 'Alice', 'age': 18},
    {'name': 'Bob', 'age': 21},
    {'name': 'Carol', 'age': 42},
]
table = ui.table(columns=columns, rows=rows, row_key='name').props('grid')
table.add_slot('item', r'''
    <q-card flat bordered :props="props" class="m-1">
        <q-card-section class="text-center">
            <strong>{{ props.row.name }}</strong>
        </q-card-section>
        <q-separator />
        <q-card-section class="text-center">
            <div>{{ props.row.age }} years</div>
        </q-card-section>
    </q-card>
''')

# ui.run()
```
