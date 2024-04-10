# {func}`~nicegui.ui.column` 列元素

提供子元素按列排列的容器。

`wrap`：是否换行内容（默认：`False`）

```python
from nicegui import ui

with ui.column():
    ui.label('label 1')
    ui.label('label 2')
    ui.label('label 3')

# ui.run()
```

## {func}`~nicegui.ui.column` Masonry 或 Pinterest 风格布局

要创建 Masonry/Pinterest 风格布局，不能使用常规的 `ui.column`。但是可以通过几个 TailwindCSS 类来实现。

```python
from nicegui import ui

with ui.element('div').classes('columns-3 w-full gap-2'):
    for i, height in enumerate([50, 50, 50, 150, 100, 50]):
        tailwind = f'mb-2 p-2 h-[{height}px] bg-blue-100 break-inside-avoid'
        with ui.card().classes(tailwind):
            ui.label(f'Card #{i+1}')

# ui.run()
```
