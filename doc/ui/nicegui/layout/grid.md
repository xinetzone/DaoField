# {func}`~nicegui.ui.grid` 网格元素

提供一个容器，其子元素按网格排列。

- `rows`：网格中的行数，或包含 `grid-template-rows` CSS 属性的字符串（例如 `'auto 1fr'`）
- `columns`：网格中的列数，或包含 `grid-template-columns` CSS 属性的字符串（例如 `'auto 1fr'`）

```python
from nicegui import ui

with ui.grid(columns=2):
    ui.label('Name:')
    ui.label('Tom')

    ui.label('Age:')
    ui.label('42')

    ui.label('Height:')
    ui.label('1.80m')

# ui.run()
```

## 自定义网格布局

此演示展示了如何通过传递包含 `grid-template-columns` CSS 属性的字符串来创建自定义网格布局。您可以使用任何有效的 CSS 尺寸，如 `'auto'`、`'1fr'`、`'80px'` 等。

- `'auto'` 会使列宽与其内容一样宽。
- `'1fr'` 或 `'2fr'` 会使相应的列填充剩余空间，比例为 1:2。
- `'80px'` 会使列宽为 80 像素。

```python
from nicegui import ui

with ui.grid(columns='auto 80px 1fr 2fr').classes('w-full gap-0'):
    for _ in range(3):
        ui.label('auto').classes('border p-1')
        ui.label('80px').classes('border p-1')
        ui.label('1fr').classes('border p-1')
        ui.label('2fr').classes('border p-1')

# ui.run()
```

## 跨越多列的单元格

此演示展示了如何使单元格跨越多列。

请注意，Tailwind 没有用于[跨越 15 列的](https://tailwindcss.com/docs/grid-column)类，但我们可以方括号内设置[任意值](https://tailwindcss.com/docs/grid-column#arbitrary-values)。或者，您可以使用相应的 CSS 定义：`.style('grid-column: span 15 / span 15')`。

```python
from nicegui import ui

with ui.grid(columns=16).classes('w-full gap-0'):
    ui.label('full').classes('col-span-full border p-1')
    ui.label('8').classes('col-span-8 border p-1')
    ui.label('8').classes('col-span-8 border p-1')
    ui.label('12').classes('col-span-12 border p-1')
    ui.label('4').classes('col-span-4 border p-1')
    ui.label('15').classes('col-[span_15] border p-1')
    ui.label('1').classes('col-span-1 border p-1')

# ui.run()
```
