# NiceGUI 通用事件

大多数 UI 元素都带有预定义的事件。例如，演示中的 "A" 这样的 `ui.button` 有一个 `on_click` 参数，它期望一个协程或函数。但是，您也可以使用 on 方法来注册一个通用事件处理器，就像 "B" 那样。这允许您为 JavaScript 和 Quasar 支持的任何事件注册处理器。

例如，即使 `ui.button` 没有 `on_mousemove` 参数，您也可以像 "C" 那样为 `mousemove` 事件注册处理器。有些事件，比如 mousemove，会非常频繁地触发。为了避免性能问题，您可以使用 throttle 参数，以便每 throttle 秒只调用一次处理器（"D"）。

通用事件处理器可以是同步的或异步的，并且可以选择性地接受 `GenericEventArguments` 作为参数（"E"）。您还可以指定应该将 JavaScript 或 Quasar 事件的哪些属性传递给处理器（"F"）。这可以减少需要在服务器和客户端之间传输的数据量。

在这里，您可以找到有关支持的事件的更多信息：

- <https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement#events> 适用于 HTML 元素
- <https://quasar.dev/vue-components> 适用于基于 Quasar 的元素（在单个组件页面上查看“Events”标签）

```python
from nicegui import ui

with ui.row():
    ui.button('A', on_click=lambda: ui.notify('You clicked the button A.'))
    ui.button('B').on('click', lambda: ui.notify('You clicked the button B.'))
with ui.row():
    ui.button('C').on('mousemove', lambda: ui.notify('You moved on button C.'))
    ui.button('D').on('mousemove', lambda: ui.notify('You moved on button D.'), throttle=0.5)
with ui.row():
    ui.button('E').on('mousedown', lambda e: ui.notify(e))
    ui.button('F').on('mousedown', lambda e: ui.notify(e), ['ctrlKey', 'shiftKey'])

# ui.run()
```

## NiceGUI 指定事件属性

一个字符串列表命名了 JavaScript 事件对象的属性：

```python
ui.button().on('click', handle_click, ['clientX', 'clientY'])
```

一个空列表请求没有属性：

```python
ui.button().on('click', handle_click, [])
```

值 `None` 表示所有属性（默认）：

```python
ui.button().on('click', handle_click, None)
```

如果事件像 QTable 的 `"row-click"`（evt, row, index）=> void 那样调用多个参数，您可以定义一个参数定义列表：

```python
ui.table(...).on('rowClick', handle_click, [[], ['name'], None])
```

在此示例中，`"row-click"` 事件将省略第一个 `evt` 参数的所有参数，仅发送 row 参数的 `"name"` 属性，并发送完整的 `index`。

如果检索到的事件参数列表长度为 1，则参数会自动解包。因此，您可以写：

```python
ui.button().on('click', lambda e: print(e.args['clientX'], flush=True))
```

而不是：

```python
ui.button().on('click', lambda e: print(e.args[0]['clientX'], flush=True))
```

请注意，默认情况下，会发送所有参数的所有可 JSON 序列化的属性。这样做是为了简化注册新事件和发现它们的属性。如果带宽有问题，应该将参数限制在服务器实际需要的内容上。

```python
from nicegui import ui

columns = [
    {'name': 'name', 'label': 'Name', 'field': 'name'},
    {'name': 'age', 'label': 'Age', 'field': 'age'},
]
rows = [
    {'name': 'Alice', 'age': 42},
    {'name': 'Bob', 'age': 23},
]
ui.table(columns, rows, 'name').on('rowClick', ui.notify, [[], ['name'], None])

# ui.run()
```

## NiceGUI 修饰符

您还可以包含[键修饰符](https://vuejs.org/guide/essentials/event-handling.html#key-modifiers%3E)（输入 "A" 中所示）、修饰符组合（输入 "B" 中所示）和[事件修饰符](https://vuejs.org/guide/essentials/event-handling.html#mouse-button-modifiers%3E)（输入 "C" 中所示）。

```python
from nicegui import ui

with ui.row():
    ui.input('A').classes('w-12').on('keydown.space', lambda: ui.notify('You pressed space.'))
    ui.input('B').classes('w-12').on('keydown.y.shift', lambda: ui.notify('You pressed Shift+Y'))
    ui.input('C').classes('w-12').on('keydown.once', lambda: ui.notify('You started typing.'))

# ui.run()
```

## NiceGUI 自定义事件

使用 `emitEvent(...)` 从 JavaScript 发出自定义事件非常简单，可以使用 `ui.on(...)` 进行监听。如果您希望在 JavaScript 中发生某事时调用 Python 代码，这可能会很有用。在这个例子中，我们正在监听浏览器标签页的 `visibilitychange` 事件。

```python
from nicegui import ui

tabwatch = ui.checkbox('Watch browser tab re-entering')
ui.on('tabvisible', lambda: ui.notify('Welcome back!') if tabwatch.value else None)
ui.add_head_html('''
    <script>
    document.addEventListener('visibilitychange', () => {
        if (document.visibilityState === 'visible') {
            emitEvent('tabvisible');
        }
    });
    </script>
''')

# ui.run()
```

## NiceGUI 纯 JavaScript 事件

您还可以使用 on 方法注册纯 JavaScript 事件处理器。如果您想在不向服务器发送任何数据的情况下调用 JavaScript 代码，这可能会很有用。在这个例子中，我们正在使用 `navigator.clipboard` API 将字符串复制到剪贴板。

```python
from nicegui import ui

ui.button('Copy to clipboard') \
    .on('click', js_handler='''() => {
        navigator.clipboard.writeText("Hello, NiceGUI!");
    }''')

# ui.run()
```
