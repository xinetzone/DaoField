from fastapi import FastAPI
from nicegui import app as gui, ui


@ui.page('/')
async def home():
    with ui.link(target='https://github.com/zauberzeug/nicegui'):
        ui.image('https://picsum.photos/id/41/640/360').classes('w-64')

app = FastAPI()
ui.run_with(
    app,
    # mount_path='/gui',  # NOTE 如果你希望传递给 `@ui.page` 的路径位于根目录，这个可以省略
    storage_secret='在这里选择你的私人密钥',  # NOTE 设置密钥是可选的，但允许每个用户进行持久存储。
)
