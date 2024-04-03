from fastapi import FastAPI
from nicegui import ui

app = FastAPI()

@app.get('/api')
def read_root():
    return {'Hello': 'World'}

@ui.page('/')
def show():
    ui.label('Hello, FastAPI!')
    ui.button('click me', on_click=lambda: ui.notify('clicked'))
    ui.link('subpage', '/subpage')

@ui.page('/subpage')
def subpage():
    ui.label('Hello, subpage!')

ui.run_with(app,on_air=True)
