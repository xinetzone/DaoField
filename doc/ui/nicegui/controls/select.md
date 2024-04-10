# {func}`~nicegui.ui.select` 下拉选择

这个元素是基于Quasar的[QSelect](https://quasar.dev/vue-components/select)组件。

`options` 可以指定为值的列表，或者作为映射值到标签的字典。在操作选项后，调用 `update()` 来更新UI中的选项。

如果 `with_input` 为 `True`，则会显示一个输入字段来过滤选项。

如果 `new_value_mode` 不为 `None`，则意味着 `with_input=True`，用户可以在输入字段中输入新值。有关详细信息，请参见 [Quasar 的文档](https://quasar.dev/vue-components/select#the-new-value-mode-prop)。请注意，当通过编程方式设置 `value` 属性时，此模式无效。

您可以使用 `validation` 参数定义验证规则的字典，例如 `{'Too long!': lambda value: len(value) < 3}`。第一个失败的规则的键将显示为错误消息。或者，您可以传递一个返回可选错误消息的可调用对象。要禁用每次值更改时的自动验证，您可以使用 `without_auto_validation` 方法。

- `options`：一个列表 `['value1', ...]` 或字典 `{'value1':'label1', ...}` 指定选项
- `label`：显示在选择上方的标签
- `value`：初始值
- `on_change`：选择改变时执行的回调函数
- `with_input`：是否显示输入字段来过滤选项
- `new_value_mode`：处理用户输入的新值（默认为None，即不允许新值）
- `multiple`：是否允许多选
- `clearable`：是否添加一个按钮来清除选择
- `validation`：验证规则的字典或返回可选错误消息的可调用对象
- `key_generator`：用于生成新值字典键的回调函数或迭代器

```python
from nicegui import ui

select1 = ui.select([1, 2, 3], value=1)
select2 = ui.select({1: 'One', 2: 'Two', 3: 'Three'}).bind_value(select1, 'value')

# ui.run()
```

## {func}`~nicegui.ui.select` 边输入边搜索

您可以激活 `with_input` 以获取带有自动补全功能的文本输入。您在输入时，选项将被过滤。

```python
from nicegui import ui

continents = [
    'Asia',
    'Africa',
    'Antarctica',
    'Europe',
    'Oceania',
    'North America',
    'South America',
]
ui.select(options=continents, with_input=True,
          on_change=lambda e: ui.notify(e.value)).classes('w-40')

# ui.run()
```

## {func}`~nicegui.ui.select` 多选

您可以激活 `multiple` 以允许选择多个项目。

```python
from nicegui import ui

names = ['Alice', 'Bob', 'Carol']
ui.select(names, multiple=True, value=names[:2], label='comma-separated') \
    .classes('w-64')
ui.select(names, multiple=True, value=names[:2], label='with chips') \
    .classes('w-64').props('use-chips')

# ui.run()
```

## {func}`~nicegui.ui.select` 更新选项

选项可以通过 `options` 属性进行更改。但之后您还需要调用 `update()` 以使更改生效。`set_options` 是一个快捷方式，可以同时完成这两个操作，并且对于 `lambda` 函数来说效果很好。

```python
from nicegui import ui

select = ui.select([1, 2, 3], value=1)
with ui.row():
    ui.button('4, 5, 6', on_click=lambda: select.set_options([4, 5, 6], value=4))
    ui.button('1, 2, 3', on_click=lambda: select.set_options([1, 2, 3], value=1))

# ui.run()
```
