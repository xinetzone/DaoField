# NiceGUI 样式设计

NiceGUI 使用 [Quasar 框架](https://quasar.dev/) 1.0 版本，因此具有其全部设计能力。每个 NiceGUI 元素都提供了 `props` 方法，其内容会[传递给 Quasar 组件](https://justpy.io/quasar_tutorial/introduction/#props-of-quasar-components)：请查看 [Quasar 文档](https://quasar.dev/vue-components/button#design)以获取所有样式属性。带有前导 : 的属性可以包含在客户端求值的 JavaScript 表达式。您还可以使用 `classes` 方法应用 [Tailwind CSS](https://tailwindcss.com/) 实用类。

如果您确实需要应用 CSS，您可以使用 `style` 方法。这里的分隔符是 `;` 而不是空格。

这三个函数还提供了 `remove` 和 `replace` 参数，以防在特定样式中不需要预定义的外观。

```python
from nicegui import ui

ui.radio(['x', 'y', 'z'], value='x').props('inline color=green')
ui.button(icon='touch_app').props('outline round').classes('shadow-lg')
ui.label('Stylish!').style('color: #6E93D6; font-size: 200%; font-weight: 300')

# ui.run()
```

## 尝试样式化 NiceGUI 元素！

尝试一下 Tailwind CSS 类、Quasar 属性和 CSS 样式如何影响 NiceGUI 元素。

从可用的元素中选择一个，并开始对其进行样式设计！

```python
from nicegui import ui

element = ui.button('element')
element.classes('

')

element.props('

')

element.style('

')

ui.run()
```
