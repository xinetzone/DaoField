from pathlib import Path
from nicegui import ui
from . import label

ROOT = Path(__file__).parent

def text_intro():
    with ui.splitter(value=5).classes('w-full h-full') as splitter:
        with splitter.before:
            with ui.tabs().props('vertical').classes('w-full') as tabs:
                label_tab = ui.tab('标签', icon='label')
                alarm = ui.tab('Alarms', icon='alarm')
                movie = ui.tab('Movies', icon='movie')
        with splitter.after:
            with ui.tab_panels(tabs, value=label_tab) \
                    .props('vertical').classes('w-full h-full'):
                with ui.tab_panel(label_tab):
                    label.callback()
                with ui.tab_panel(alarm):
                    ui.label('Alarms').classes('text-h4')
                    ui.label('Content of alarms')
                with ui.tab_panel(movie):
                    ui.label('Movies').classes('text-h4')
                    ui.label('Content of movies')
