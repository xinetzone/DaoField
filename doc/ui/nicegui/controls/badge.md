# `ui.badge` 徽章

包裹 Quasar 的[QBadge](https://quasar.dev/vue-components/badge)组件的徽章元素。

- `text`：文本字段的初始值
- `color`：组件的颜色名称（可以是 Quasar、Tailwind 或 CSS 颜色，也可以是 `None`，默认为 `"primary"`）
- `text_color`：文本颜色（可以是 Quasar、Tailwind 或 CSS 颜色，也可以是 `None`，默认为 `None`）
- `outline`：使用 `'outline'` 设计（只有彩色文本和边框）（默认为 `False`）

```python
from nicegui import ui

with ui.button('Click me!', on_click=lambda: badge.set_text(int(badge.text) + 1)):
    badge = ui.badge('0', color='red').props('floating')

# ui.run()
```
