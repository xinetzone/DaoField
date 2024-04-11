# {func}`nicegui.ui.json_editor` JSON 编辑器

`JSONEditor` 是一个使用 [JSONEditor](https://github.com/josdejong/svelte-jsoneditor) 创建JSON编辑器的元素。通过更改`properties`属性，可以将更新推送到编辑器。数据发生变化后，调用`update`方法刷新编辑器。

- `properties`: JSONEditor 属性的字典
- `on_select`: 当某些内容被选中时调用的回调函数
- `on_change`: 当内容发生变化时调用的回调函数

```python
from nicegui import ui

json = {
    'array': [1, 2, 3],
    'boolean': True,
    'color': '#82b92c',
    None: None,
    'number': 123,
    'object': {
        'a': 'b',
        'c': 'd',
    },
    'time': 1575599819000,
    'string': 'Hello World',
}
ui.json_editor({'content': {'json': json}},
               on_select=lambda e: ui.notify(f'Select: {e}'),
               on_change=lambda e: ui.notify(f'Change: {e}'))

# ui.run()
```

## {func}`nicegui.ui.json_editor` `run_editor_method`

你可以使用`run_editor_method`方法来运行JSONEditor实例的方法。这个示例展示了如何展开和折叠所有节点，以及如何获取当前数据。

在方法名 `"expand"` 前面的冒号 `":"` 表示值 `"path => true"` 是一个JavaScript表达式，它在传递给方法之前会在客户端进行求值。

```python
from nicegui import ui

json = {
    'Name': 'Alice',
    'Age': 42,
    'Address': {
        'Street': 'Main Street',
        'City': 'Wonderland',
    },
}
editor = ui.json_editor({'content': {'json': json}})

ui.button('Expand', on_click=lambda: editor.run_editor_method(':expand', 'path => true'))
ui.button('Collapse', on_click=lambda: editor.run_editor_method(':expand', 'path => false'))
ui.button('Readonly', on_click=lambda: editor.run_editor_method('updateProps', {'readOnly': True}))

async def get_data() -> None:
    data = await editor.run_editor_method('get')
    ui.notify(data)
ui.button('Get Data', on_click=get_data)

# ui.run()
```
