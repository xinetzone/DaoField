# NiceGUI CSS 配置

## NiceGUI Tailwind CSS

[Tailwind CSS](https://tailwindcss.com/) 是用于快速构建自定义用户界面的 CSS 框架。NiceGUI 提供了一个流畅的、支持自动补全的界面，用于向 UI 元素添加 Tailwind 类。

您可以通过浏览 tailwind 属性的方法来发现可用的类。构建器模式允许您将多个类链接在一起（如`'Label A'`所示）。您也可以使用类列表调用 `tailwind` 属性（如`'Label B'`所示）。

尽管这与使用 `classes` 方法非常相似，但由于自动补全功能，对于 Tailwind 类来说更加方便。

最后但同样重要的是，您还可以预定义一个样式并将其应用于多个元素（`'Label C'` 和 `'Label D'`）。

请注意，有时 Tailwind 会被 Quasar 样式覆盖，例如当使用 `ui.button('Button').tailwind('bg-red-500')` 时。这是已知的限制，我们无法完全控制。但我们尝试提供解决方案，如 `color` 参数：`ui.button('Button', color='red-500')`。

```python
from nicegui import Tailwind, ui

ui.label('Label A').tailwind.font_weight('extrabold').text_color('blue-600').background_color('orange-200')
ui.label('Label B').tailwind('drop-shadow', 'font-bold', 'text-green-600')

red_style = Tailwind().text_color('red-600').font_weight('bold')
label_c = ui.label('Label C')
red_style.apply(label_c)
ui.label('Label D').tailwind(red_style)

# ui.run()
```

## NiceGUI Tailwind CSS 层

Tailwind CSS 的 `@layer` 指令允许您定义可以在 HTML 中使用的自定义类。NiceGUI 通过允许您将自定义类添加到组件层来支持这一功能。这样，您可以定义自己的类并在 UI 元素中使用它们。在下面的示例中，我们定义了一个自定义类 blue-box 并将其应用于两个标签。请注意，`style` 标签的类型是 `text/tailwindcss` 而不是 `text/css`。

```python
from nicegui import ui

ui.add_head_html('''
    <style type="text/tailwindcss">
        @layer components {
            .blue-box {
                @apply bg-blue-500 p-12 text-center shadow-lg rounded-lg text-white;
            }
        }
    </style>
''')

with ui.row():
    ui.label('Hello').classes('blue-box')
    ui.label('world').classes('blue-box')

# ui.run()
```
