# {func}`~nicegui.ui.video` 视频

显示视频。

- `src`: 视频源的URL或本地文件路径
- `controls`: 是否显示视频控制，如播放、暂停和音量（默认值：`True`）
- `autoplay`: 是否自动开始播放视频（默认值：`False`）
- `muted`: 视频是否应初始为静音状态（默认值：`False`）
- `loop`: 视频是否应该循环播放（默认值：`False`）

查看[事件列表](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video#events)，您可以使用通用事件订阅`on()`进行订阅。

```python
from nicegui import ui

v = ui.video('https://test-videos.co.uk/vids/bigbuckbunny/mp4/h264/360/Big_Buck_Bunny_360_10s_1MB.mp4')
v.on('ended', lambda _: ui.notify('Video playback completed'))

# ui.run()
```
## {func}`~nicegui.ui.video` 控制视频元素

此演示展示了如何以编程方式播放、暂停和查找。

```python
from nicegui import ui

v = ui.video('https://test-videos.co.uk/vids/bigbuckbunny/mp4/h264/360/Big_Buck_Bunny_360_10s_1MB.mp4')
ui.button('Play', on_click=v.play)
ui.button('Pause', on_click=v.pause)
ui.button('Jump to 0:05', on_click=lambda: v.seek(5))

# ui.run()
```
