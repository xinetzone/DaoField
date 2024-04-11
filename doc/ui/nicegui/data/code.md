# {func}`~nicegu.ui.code` 代码

这个元素显示一个带有语法高亮的代码块。

- `content`: 要显示的代码
- `language`: 代码的语言（默认：`"python"`）

```python
from nicegui import ui

ui.code('''
    from nicegui import ui
    
    ui.label('Code inception!')
        
    ui.run()
''').classes('w-full')

# ui.run()
```
