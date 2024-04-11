# {func}`~nicegui.ui.aggrid` AG Grid

使用[AG Grid](https://www.ag-grid.com/)创建网格的元素。

可以使用`run_grid_method`和`run_column_method`方法与客户机上的AG Grid实例进行交互。

- `options`：AG Grid选项的字典
- `html_columns`：应该以HTML渲染的列的列表（默认：`[]`）
- `theme`：AG Grid主题（默认：`'balham'`）
- `auto_size_columns`：是否自动调整列宽以适应网格宽度（默认：`True`）

```python
from nicegui import ui

grid = ui.aggrid({
    'defaultColDef': {'flex': 1},
    'columnDefs': [
        {'headerName': 'Name', 'field': 'name'},
        {'headerName': 'Age', 'field': 'age'},
        {'headerName': 'Parent', 'field': 'parent', 'hide': True},
    ],
    'rowData': [
        {'name': 'Alice', 'age': 18, 'parent': 'David'},
        {'name': 'Bob', 'age': 21, 'parent': 'Eve'},
        {'name': 'Carol', 'age': 42, 'parent': 'Frank'},
    ],
    'rowSelection': 'multiple',
}).classes('max-h-40')

def update():
    grid.options['rowData'][0]['age'] += 1
    grid.update()

ui.button('Update', on_click=update)
ui.button('Select all', on_click=lambda: grid.run_grid_method('selectAll'))
ui.button('Show parent', on_click=lambda: grid.run_column_method('setColumnVisible', 'parent', True))

# ui.run()
```

## {func}`~nicegui.ui.aggrid` 选择 AG Grid 行

您可以在网格单元格中添加复选框，允许用户选择单个或多个行。

要获取当前选定的行，请使用`get_selected_rows`方法。此方法返回一个由字典组成的行列表。

如果`rowSelection`设置为`'single'`或者要获取第一个选定的行，您也可以使用`get_selected_row`方法。该方法返回一个单一行为字典，如果没有选定行则返回`None`。

有关更多信息，请参阅[AG Grid文档](https://www.ag-grid.com/javascript-data-grid/row-selection/#example-single-row-selection)。

```python
from nicegui import ui

grid = ui.aggrid({
    'columnDefs': [
        {'headerName': 'Name', 'field': 'name', 'checkboxSelection': True},
        {'headerName': 'Age', 'field': 'age'},
    ],
    'rowData': [
        {'name': 'Alice', 'age': 18},
        {'name': 'Bob', 'age': 21},
        {'name': 'Carol', 'age': 42},
    ],
    'rowSelection': 'multiple',
}).classes('max-h-40')

async def output_selected_rows():
    rows = await grid.get_selected_rows()
    if rows:
        for row in rows:
            ui.notify(f"{row['name']}, {row['age']}")
    else:
        ui.notify('No rows selected.')

async def output_selected_row():
    row = await grid.get_selected_row()
    if row:
        ui.notify(f"{row['name']}, {row['age']}")
    else:
        ui.notify('No row selected!')

ui.button('Output selected rows', on_click=output_selected_rows)
ui.button('Output selected row', on_click=output_selected_row)

# ui.run()
```

## {func}`~nicegui.ui.aggrid` 使用迷你过滤器过滤行

您可以在每列的标题中添加[迷你过滤器](https://ag-grid.com/javascript-data-grid/filter-set-mini-filter/)来过滤行。

注意`"agTextColumnFilter"`如何匹配单个字符，例如`"Alice"`和`"Carol"`中的`"a"`，而`"agNumberColumnFilter"`则匹配整个数字，例如`"18"`和`"21"`，但不包括`"1"`。

```python
from nicegui import ui

ui.aggrid({
    'columnDefs': [
        {'headerName': 'Name', 'field': 'name', 'filter': 'agTextColumnFilter', 'floatingFilter': True},
        {'headerName': 'Age', 'field': 'age', 'filter': 'agNumberColumnFilter', 'floatingFilter': True},
    ],
    'rowData': [
        {'name': 'Alice', 'age': 18},
        {'name': 'Bob', 'age': 21},
        {'name': 'Carol', 'age': 42},
    ],
}).classes('max-h-40')

# ui.run()
```

## {func}`~nicegui.ui.aggrid` AG Grid 带有条件单元格格式化

此演示展示了如何使用[`cellClassRules`](https://www.ag-grid.com/javascript-grid-cell-styles/#cell-class-rules)根据单元格的值有条件地格式化单元格。

```python
from nicegui import ui

ui.aggrid({
    'columnDefs': [
        {'headerName': 'Name', 'field': 'name'},
        {'headerName': 'Age', 'field': 'age', 'cellClassRules': {
            'bg-red-300': 'x < 21',
            'bg-green-300': 'x >= 21',
        }},
    ],
    'rowData': [
        {'name': 'Alice', 'age': 18},
        {'name': 'Bob', 'age': 21},
        {'name': 'Carol', 'age': 42},
    ],
})

# ui.run()
```

## 从 Pandas DataFrame 创建 {func}`~nicegui.ui.aggrid`

您可以使用`from_pandas`方法从Pandas DataFrame创建一个AG Grid。此方法接受一个Pandas DataFrame作为输入，并返回一个AG Grid。

```python
import pandas as pd
from nicegui import ui

df = pd.DataFrame(data={'col1': [1, 2], 'col2': [3, 4]})
ui.aggrid.from_pandas(df).classes('max-h-40')

# ui.run()
```

## {func}`~nicegui.ui.aggrid` 将列渲染为 HTML

您可以通过将列索引列表传递给`html_columns`参数来将列渲染为HTML。

```python
from nicegui import ui

ui.aggrid({
    'columnDefs': [
        {'headerName': 'Name', 'field': 'name'},
        {'headerName': 'URL', 'field': 'url'},
    ],
    'rowData': [
        {'name': 'Google', 'url': '<a href="https://google.com">https://google.com</a>'},
        {'name': 'Facebook', 'url': '<a href="https://facebook.com">https://facebook.com</a>'},
    ],
}, html_columns=[1])

# ui.run()
```

## {func}`~nicegui.ui.aggrid` 响应AG Grid事件

所有AG Grid事件都通过AG Grid全局监听器传递给NiceGUI。这些事件可以使用`.on()`方法进行订阅。

```python
from nicegui import ui

ui.aggrid({
    'columnDefs': [
        {'headerName': 'Name', 'field': 'name'},
        {'headerName': 'Age', 'field': 'age'},
    ],
    'rowData': [
        {'name': 'Alice', 'age': 18},
        {'name': 'Bob', 'age': 21},
        {'name': 'Carol', 'age': 42},
    ],
}).on('cellClicked', lambda event: ui.notify(f'Cell value: {event.args["value"]}'))

# ui.run()
```

## {func}`~nicegui.ui.aggrid` AG Grid中使用复杂对象

您可以通过用句点分隔字段名来在AG Grid中使用嵌套的复杂对象。（这就是为什么`rowData`中的键不允许包含句点的原因。）

```python
from nicegui import ui

ui.aggrid({
    'columnDefs': [
        {'headerName': 'First name', 'field': 'name.first'},
        {'headerName': 'Last name', 'field': 'name.last'},
        {'headerName': 'Age', 'field': 'age'}
    ],
    'rowData': [
        {'name': {'first': 'Alice', 'last': 'Adams'}, 'age': 18},
        {'name': {'first': 'Bob', 'last': 'Brown'}, 'age': 21},
        {'name': {'first': 'Carol', 'last': 'Clark'}, 'age': 42},
    ],
}).classes('max-h-40')

# ui.run()
```

## {func}`~nicegui.ui.aggrid` AG Grid 中使用动态行高

您可以通过将一个函数传递给`getRowHeight`参数来设置个别行的高度。

```python
from nicegui import ui

ui.aggrid({
    'columnDefs': [{'field': 'name'}, {'field': 'age'}],
    'rowData': [
        {'name': 'Alice', 'age': '18'},
        {'name': 'Bob', 'age': '21'},
        {'name': 'Carol', 'age': '42'},
    ],
    ':getRowHeight': 'params => params.data.age > 35 ? 50 : 25',
}).classes('max-h-40')

# ui.run()
```

## {func}`~nicegui.ui.aggrid` 运行行方法

您可以使用`run_row_method`方法在个别行上运行方法。此方法接受行`ID`、方法名称和方法参数作为参数。行`ID`可以是行索引（作为字符串）或`getRowId`函数的值。

以下演示展示了如何使用它来更新单元格值。请注意，当值更新时，行选择会被保留。如果使用`update`方法更新网格，情况将不会如此。

```python
from nicegui import ui

grid = ui.aggrid({
    'columnDefs': [
        {'field': 'name', 'checkboxSelection': True},
        {'field': 'age'},
    ],
    'rowData': [
        {'name': 'Alice', 'age': 18},
        {'name': 'Bob', 'age': 21},
        {'name': 'Carol', 'age': 42},
    ],
    ':getRowId': '(params) => params.data.name',
})
ui.button('Update',
          on_click=lambda: grid.run_row_method('Alice', 'setDataValue', 'age', 99))

# ui.run()
```

## {func}`~nicegui.ui.aggrid` 过滤返回值

您可以通过传递定义JavaScript函数的字符串来过滤方法调用的返回值。此演示运行了网格方法`"getDisplayedRowAtIndex"`并返回结果的`"data"`属性。

```python
from nicegui import ui

grid = ui.aggrid({
    'columnDefs': [{'field': 'name'}],
    'rowData': [{'name': 'Alice'}, {'name': 'Bob'}],
})

async def get_first_name() -> None:
    row = await grid.run_grid_method('(g) => g.getDisplayedRowAtIndex(0).data')
    ui.notify(row['name'])

ui.button('Get First Name', on_click=get_first_name)

# ui.run()
```
