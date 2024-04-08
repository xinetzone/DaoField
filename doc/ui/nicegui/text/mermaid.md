# `ui.mermaid` Mermaid 图表

渲染使用受 Markdown 启发的 [Mermaid 语言](https://mermaid.js.org/)编写的图表和图形。通过向 `ui.markdown` 元素提供扩展字符串 `'mermaid'`，也可以在 Markdown 元素中使用 mermaid 语法。

`content`：要显示的 Mermaid 内容

```python
from nicegui import ui

ui.mermaid('''
graph LR;
    A --> B;
    A --> C;
''')

# ui.run()
```

## `ui.mermaid` 处理 Mermaid 错误

您可以通过监听 `error` 事件来处理错误。事件参数包含属性 `hash`、`message`、`str` 以及一个带有额外信息的错误对象。

```python
from nicegui import ui

ui.mermaid('''
graph LR;
    A --> B;
    A -> C;
''').on('error', lambda e: print(e.args['message']))

# ui.run()
```
