# {func}`~nicegui.ui.pagination`

分页元素封装了 Quasar 的 [QPagination 组件](https://quasar.dev/vue-components/pagination)。

- `min`：最小页码
- `max`：最大页码
- `direction_links`：是否显示首页/末页链接
- `value`：初始页面（如果没有提供值，则默认为 min）
- `on_change`：值改变时要调用的回调函数

```python
from nicegui import ui

p = ui.pagination(1, 5, direction_links=True)
ui.label().bind_text_from(p, 'value', lambda v: f'Page {v}')

# ui.run()
```
