from pathlib import Path
from nicegui import ui
from ..utils import create_doc

ROOT = Path(__file__).parent

def create():
    from nicegui import ui

    ui.button('Click me!', on_click=lambda: ui.notify('You clicked me!'))

    # ui.run()

def create2():
    from nicegui import ui

    with ui.row():
        ui.button('demo', icon='history')
        ui.button(icon='thumb_up')
        with ui.button():
            ui.label('sub-elements')
            ui.image('https://picsum.photos/id/377/640/360') \
                .classes('rounded-full w-16 h-16 ml-4')

    # ui.run()

def create3():
    from nicegui import ui

    @ui.page('/')
    async def index():
        b = ui.button('Step')
        await b.clicked()
        ui.label('One')
        await b.clicked()
        ui.label('Two')
        await b.clicked()
        ui.label('Three')

    # ui.run()

def create4():
    import httpx
    from contextlib import contextmanager
    from nicegui import ui

    @contextmanager
    def disable(button: ui.button):
        button.disable()
        try:
            yield
        finally:
            button.enable()

    async def get_slow_response(button: ui.button) -> None:
        with disable(button):
            async with httpx.AsyncClient() as client:
                response = await client.get('https://httpbin.org/delay/1', timeout=5)
                ui.notify(f'Response code: {response.status_code}')

    ui.button('Get slow response', on_click=lambda e: get_slow_response(e.sender))

    # ui.run()

def create5():
    from nicegui import ui

    class ToggleButton(ui.button):

        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)
            self._state = False
            self.on('click', self.toggle)

        def toggle(self) -> None:
            """Toggle the button state."""
            self._state = not self._state
            self.update()

        def update(self) -> None:
            self.props(f'color={"green" if self._state else "red"}')
            super().update()

    ToggleButton('Toggle me')

    # ui.run()

def callback():
    ui.markdown("""
    # 按钮

    这个元素是基于Quasar的[QBtn](https://quasar.dev/vue-components/button)组件。

    `color` 参数接受 Quasar 颜色，Tailwind颜色，或者 CSS 颜色。如果使用 Quasar 颜色，按钮将根据 Quasar 主题进行样式设置，包括文本的颜色。注意，有些颜色如"红色"既是 Quasar 颜色也是 CSS 颜色。在这种情况下，将使用 Quasar 颜色。

    - `text`：按钮的标签
    - `on_click`：当按钮被按下时调用的回调函数
    - `color`：按钮的颜色（可以是 Quasar、Tailwind 或 CSS 颜色，也可以是 `None`，默认为 `'primary'`）
    - `icon`：要在按钮上显示的图标的名称（默认为 `None`）
    """)
    create_doc(create)
    ui.markdown("""
    ## 图标

    为按钮添加图标。
    """)
    create_doc(create2)
    ui.markdown("""
    ## 等待按钮点击
    有时候，在继续执行之前等待按钮点击是很方便的。
    """)
    create_doc(create3)
    ui.markdown("""
    ## 使用上下文管理器禁用按钮
    这里展示了一个上下文管理器，它可以用来在异步进程期间禁用按钮。
    """)
    create_doc(create4)
    ui.markdown("""
    ## 自定义切换按钮
    就像所有其他元素一样，你可以实现自己的子类，并加入专门的逻辑。比如这个具有内部布尔状态的红/绿切换按钮。
    """)
    create_doc(create5)
