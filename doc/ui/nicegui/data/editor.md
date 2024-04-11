# {func}`~nicegui.ui.editor` 编辑器

基于Quasar的[QEditor](https://quasar.dev/vue-components/editor)组件的一个所见即所得编辑器。值是一个包含格式化文本的HTML代码字符串。

- `value`: 初始值
- `on_change`: 值改变时调用的回调函数

```python
from nicegui import ui

editor = ui.editor(placeholder='Type something here')
ui.markdown().bind_content_from(editor, 'value',
                                backward=lambda v: f'HTML code:\n```\n{v}\n```')

# ui.run()
```
