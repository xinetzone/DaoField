# {func}`~nicegui.ui.audio` 音频

显示一个音频播放器。

- `src`: 音频源的URL或本地文件路径
- `controls`: 是否显示音频控制，如播放、暂停和音量（默认值：`True`）
- `autoplay`: 是否自动开始播放音频（默认值：`False`）
- `muted`: 音频是否应初始为静音状态（默认值：`False`）
- `loop`: 音频是否应该循环播放（默认值：`False`）

查看[事件列表](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/audio#events)，您可以使用通用事件订阅`on()`进行订阅。

```python
from nicegui import ui

a = ui.audio('https://cdn.pixabay.com/download/audio/2022/02/22/audio_d1718ab41b.mp3')
a.on('ended', lambda _: ui.notify('Audio playback completed'))

ui.button(on_click=lambda: a.props('muted'), icon='volume_off').props('outline')
ui.button(on_click=lambda: a.props(remove='muted'), icon='volume_up').props('outline')

# ui.run()
```

## {func}`~nicegui.ui.audio` 控制音频元素

此演示展示了如何以编程方式播放、暂停和查找。

```python
from nicegui import ui

a = ui.audio('https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3')
ui.button('Play', on_click=a.play)
ui.button('Pause', on_click=a.pause)
ui.button('Jump to 0:30', on_click=lambda: a.seek(30))

# ui.run()
```
