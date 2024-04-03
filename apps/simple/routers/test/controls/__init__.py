from pathlib import Path
from nicegui import ui
from . import button

ROOT = Path(__file__).parent

def callback():
    with ui.splitter(value=10).classes('w-full h-full') as splitter:
        with splitter.before:
            with ui.tabs().props('vertical').classes('w-full') as tabs:
                button_tab = ui.tab('按钮', icon='button')
        with splitter.after:
            with ui.tab_panels(tabs, value=button_tab).props('vertical').classes('w-full h-full'):
                with ui.tab_panel(button_tab):
                    button.callback()
                