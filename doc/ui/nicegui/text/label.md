# `ui.label` 标签

显示一些文本。

- `text`：标签的内容

```python
from nicegui import ui

ui.label('some label')

ui.run()
```

## 根据内容改变 `ui.label` 外观

您可以重写 `_handle_text_change` 方法，根据标签的内容来更新其他属性。这种技术也适用于[绑定](../binding/index)，如下所示的示例中所示。

```python
from nicegui import ui

class status_label(ui.label):
    def _handle_text_change(self, text: str) -> None:
        super()._handle_text_change(text)
        if text == 'ok':
            self.classes(replace='text-positive')
        else:
            self.classes(replace='text-negative')

model = {'status': 'error'}
status_label().bind_text_from(model, 'status')
ui.switch(on_change=lambda e: model.update(status='ok' if e.value else 'error'))

ui.run()
```
