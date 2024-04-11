from nicegui import APIRouter, ui

router = APIRouter(prefix='/test')

@router.page('/')
def page():
    ui.label('This is content on /test')
    ui.link('Visit test', '/test')
    ui.link('Visit sub-test', '/test/sub-test')

@router.page('/sub-test')
def page():
    ui.label('This is content on /test/sub-test')
