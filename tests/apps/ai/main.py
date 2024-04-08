from fastapi import FastAPI
from nicegui import app as gui, ui

@ui.page('/')
def show():
    ui.label('Hello, FastAPI!')

    # NOTE 深色模式将为每个用户在标签页和服务器重启之间保持持久
    ui.dark_mode().bind_value(gui.storage.user, 'dark_mode')
    ui.checkbox('dark mode').bind_value(gui.storage.user, 'dark_mode')

app = FastAPI()
ui.run_with(
    app,
    mount_path='/gui',  # NOTE 如果你希望传递给 `@ui.page` 的路径位于根目录，这个可以省略
    storage_secret='在这里选择你的私人密钥',  # NOTE 设置密钥是可选的，但允许每个用户进行持久存储。
)
