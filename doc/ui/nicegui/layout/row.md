# {func}`~nicegui.ui.row` 行元素

提供一个容器，其子元素按行排列。

`wrap`：是否换行内容（默认：`True`）

```python
from nicegui import ui

with ui.row():
    ui.label('label 1')
    ui.label('label 2')
    ui.label('label 3')

# ui.run()
```
