# `ui.link` + `ui.link_target` 链接

要在页面内跳转到特定位置，您可以使用 `ui.link_target("name")` 放置可链接锚点，并使用 `ui.link(target="#name")` 进行链接。

## `ui.link` 创建超链接

- `text`：显示文本
- `target`：页面函数、同一页面上的 NiceGUI 元素或从基本 URL 开始的绝对 URL 或相对路径的字符串
- `new_tab`：在新标签页中打开链接（默认：`False`）

```python
from nicegui import ui

ui.link('NiceGUI on GitHub', 'https://github.com/zauberzeug/nicegui')

# ui.run()
```

## `ui.link_target` 页面导航

要在页面内跳转到特定位置，您可以使用 `ui.link_target('target_name')` 放置可链接锚点，或者直接将 NiceGUI 元素作为链接目标传递。

```python
from nicegui import ui

navigation = ui.row()
ui.link_target('target_A')
ui.label(
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit, '
    'sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
)
label_B = ui.label(
    'Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. '
    'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. '
    'Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
)
with navigation:
    ui.link('Goto A', '#target_A')
    ui.link('Goto B', label_B)

# ui.run()
```

## `ui.link` 链接到其他页面 

您可以通过将链接目标提供为路径或函数引用来链接到其他页面。

```python
from nicegui import ui

@ui.page('/some_other_page')
def my_page():
    ui.label('This is another page')

ui.label('Go to other page')
ui.link('... with path', '/some_other_page')
ui.link('... with function reference', my_page)

# ui.run()
```

## `ui.link` 链接图像和其他元素

通过将元素嵌套在链接内部，您可以使整个元素可点击。这适用于所有元素，但对于非交互式元素（如 [`ui.image`](https://nicegui.io/documentation/image)、[`ui.avatar`](https://nicegui.io/documentation/image) 等）最为有用。

```python
from nicegui import ui

with ui.link(target='https://github.com/zauberzeug/nicegui'):
    ui.image('https://picsum.photos/id/41/640/360').classes('w-64')

# ui.run()
```
