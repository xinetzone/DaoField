# {func}`~nicegui.ui.add_style` 向页面添加样式定义

此函数可用于将 CSS、SCSS 或 SASS 样式定义添加到 HTML 页面的头部。

- `content`：样式内容（字符串或文件路径）
- `indented`：内容是否缩进（SASS）或不缩进（SCSS/CSS）（默认：`False`）

```python
from nicegui import ui

ui.add_style('''
    .red {
        color: red;
    }
''')
ui.label('This is red with CSS.').classes('red')

# ui.run()
```

## {func}`~nicegui.ui.add_style` 使用 SCSS 定义样式

您也可以使用 SCSS 来定义样式。

```python
from nicegui import ui

ui.add_style('''
    .green {
        background-color: lightgreen;
        .blue {
            color: blue;
        }
    }
''')
with ui.element().classes('green'):
    ui.label('This is blue on green with SCSS.').classes('blue')

# ui.run()
```

## {func}`~nicegui.ui.add_style` 使用 SASS

您也可以通过将 `indented` 参数设置为 `True` 来使用缩进的 SASS 语法。

```python
from nicegui import ui

ui.add_style('''
    .yellow
        background-color: yellow
        .purple
            color: purple
''', indented=True)
with ui.element().classes('yellow'):
    ui.label('This is purple on yellow with SASS.').classes('purple')

# ui.run()
```
