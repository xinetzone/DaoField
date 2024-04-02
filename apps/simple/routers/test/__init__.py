"""NiceGUI 文档"""
from pathlib import Path
from nicegui import ui, APIRouter
from .utils import create_doc
from . import intro, text

ROOT = Path(__file__).parent
router = APIRouter(prefix='/test')

@router.page('/')
def page():
    with ui.header(elevated=True).style('background-color: #3874c8'):
        ui.label('等待')
    with ui.footer().style('background-color: #3874c8').classes('items-center justify-between'):
        with ui.tabs() as tabs:
            intro_tab = ui.tab('简介')
            text_tab = ui.tab('文本')
    with ui.tab_panels(tabs, value=intro_tab).classes('w-full'):
        with ui.tab_panel(intro_tab):
            intro.callback()
        with ui.tab_panel(text_tab):
            text.text_intro()
