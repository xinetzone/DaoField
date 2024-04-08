# `ui.html` HTML 元素

将任意 HTML 渲染到页面上，包装在指定的标签内。可以使用 Tailwind 进行样式设计。您还可以使用 `ui.add_head_html` 将 `html` 代码添加到文档的 `head` 中，以及使用 `ui.add_body_html` 将其添加到 `body` 中。

- `content`：要显示的 HTML 代码
- `tag`：包裹内容的 HTML 标签（默认：`"div"`）

```python
from nicegui import ui

ui.html('This is <strong>HTML</strong>.')

# ui.run()
```

## `ui.html` 生成内联元素

使用 `tag` 参数来生成除了 `div` 之外的其他元素。

```python
from nicegui import ui

ui.html('This is <u>emphasized</u>.', tag='em')

# ui.run()
```
