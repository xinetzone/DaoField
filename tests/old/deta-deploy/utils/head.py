from nicegui import app as gui, ui

def add_head_html():
    ui.add_head_html('''
    <link href="https://xinetzone.github.io/w3css/4/w3.css" rel="stylesheet" />
    <link href="https://xinetzone.github.io/Font-Awesome/css/all.css" rel="stylesheet" />
    <link href="https://xinetzone.github.io/xinet-css/tabs.css" rel="stylesheet" />
    ''')