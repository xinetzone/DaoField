# NiceGUI On Air

通过使用 `ui.run(on_air=True)`，你可以通过互联网与他人分享你的本地应用程序 &#129502;。

当访问在线URL时，所有库（如Vue、Quasar等）都从我们的CDN加载。因此，只有原始内容和事件需要由你的本地应用程序传输。即使您的应用程序的互联网连接很差（例如，在野外的移动机器人），这也使得它非常快。

通过设置 `on_air=True`，你将获得一个有效期为1小时的随机URL。如果你在 [https://on-air.nicegui.io](https://on-air.nicegui.io/) 注册，你可以设置组织和设备名称以获取固定URL：`https://on-air.nicegui.io/<my-org>/<my_device_name>`。然后，设备将通过一个独特的私有令牌进行识别，你可以使用该令牌代替布尔标志：`ui.run(on_air='<your token>')`。如果你 [赞助我们](https://github.com/sponsors/zauberzeug)，我们将启用多设备管理，并为每个设备提供内置的密码保护。

目前，On Air作为技术预览版提供，可以免费使用。我们将逐步提高稳定性，并通过使用统计、远程终端访问等功能扩展服务。请在 [GitHub](https://github.com/zauberzeug/nicegui/discussions)、[Reddit](https://www.reddit.com/r/nicegui/) 或 [Discord](https://discord.gg/TEpFeAaF4f) 上告诉我们您的反馈。

**数据隐私：** 我们非常重视您的隐私。NiceGUI On Air不会记录或存储任何中继数据的内容。
