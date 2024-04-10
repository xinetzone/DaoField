from fastapi import FastAPI
from nicegui import app as gui, ui, run
import requests
from datetime import datetime

async def handle_click():
    URL = 'https://httpbin.org/delay/1'
    response = await run.io_bound(requests.get, URL, timeout=3)
    ui.notify(f'Downloaded {len(response.content)} bytes')

@ui.page('/')
async def home():
    ui.button('Compute', on_click=handle_click)
    log = ui.log().classes('w-full').style()
    ui.button('Log time', on_click=lambda: log.push(datetime.now().strftime('%X.%f')[:-5]))

app = FastAPI()
ui.run_with(
    app,
    # mount_path='/gui',  # NOTE 如果你希望传递给 `@ui.page` 的路径位于根目录，这个可以省略
    storage_secret='在这里选择你的私人密钥',  # NOTE 设置密钥是可选的，但允许每个用户进行持久存储。
)
