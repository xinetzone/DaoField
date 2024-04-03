"""NiceGUI 文档"""
from pathlib import Path
from nicegui import ui, APIRouter

ROOT = Path(__file__).parent
router = APIRouter(prefix='/test')

@router.page('/')
def page():
    ui.label("测试")
