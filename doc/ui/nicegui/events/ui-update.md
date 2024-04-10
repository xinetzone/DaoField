# NiceGUI UI 更新

NiceGUI 尝试自动将 UI 元素的状态与客户端同步，例如当标签文本、输入值或元素的样式/类/属性发生更改时。在其他情况下，您可以显式调用` element.update()` 或 `ui.update(*elements)` 进行更新。演示代码展示了针对 `ui.echart` 的两种方法，其中很难自动检测选项字典中的变化。

```python
from nicegui import ui
from random import random

chart = ui.echart({
    'xAxis': {'type': 'value'},
    'yAxis': {'type': 'value'},
    'series': [{'type': 'line', 'data': [[0, 0], [1, 1]]}],
})

def add():
    chart.options['series'][0]['data'].append([random(), random()])
    chart.update()

def clear():
    chart.options['series'][0]['data'].clear()
    ui.update(chart)

with ui.row():
    ui.button('Add', on_click=add)
    ui.button('Clear', on_click=clear)

# ui.run()
```
