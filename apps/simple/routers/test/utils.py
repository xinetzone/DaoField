import inspect
from typing import Any, Callable
from nicegui import ui

def create_doc(func):
    """创建文档组件"""
    func_body = inspect.getsource(func) #.split(":\n")[-1]
    with ui.splitter(value=10).classes('w-full h-full') as splitter:
        with splitter.before:
            with ui.tabs().props('vertical').classes('w-full') as tabs:
                code = ui.tab('代码', icon='code')
                output = ui.tab('输出', icon='output')
        with splitter.after:
            with ui.tab_panels(tabs, value=code).props('vertical').classes('w-full'):
                with ui.tab_panel(code):
                    ui.code(func_body).classes('w-full') # 展示
                with ui.tab_panel(output):
                    func() # 执行
