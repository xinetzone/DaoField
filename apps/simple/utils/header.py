from nicegui import app as gui, ui

def create_header():
    with ui.header(elevated=True, bordered=True).style('background-color: grey'): #.classes('items-center justify-between'):
        ui.link("主页", "/").classes("w3-yellow w3-button")
        ui.link("测试", "/test").classes("w3-yellow w3-button")
