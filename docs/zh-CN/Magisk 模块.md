### 被重定向的应用仍不时创建文件

目前，_存储重定向_ 依靠 logcat 来获知应用进程创建，因此当 _存储重定向_ 晚于应用启动或 log 输出晚于应用启动，重定向便不能及时生效。

为了彻底解决该问题，我们找到一种 _通过替换一个共享库注入 zygote 进程并 "hook" 一个会在 fork 出应用进程时被调用的函数_ 的方案。借此我们可以保证重定向一定会在应用本身逻辑前运行。

由于该方案需要替换系统文件，我们暂时只提供 Magisk 模块。

#### Magisk 模块使用前须知

* **必须配合 _存储重定向_ 0.14.0 版本或以上使用**，否则部分应用会无法启动，联系开发者加入内部测试
* 需要使用 Magisk v15+
* 安装前**请务必确认已经了解如何从 recovery 删除模块**，否则如果系统与其不兼容，将会无法进入系统
* 如果出现问题，提供开机以来的 log 给开发者会很有帮助
* 如果安装了旧的 Magisk 模块 (sr starter)，请自行删除

#### 已知问题

* 如果使用 Xposed 可能会无效
* _软重启_（非正常重启）会导致 MTP，adb 甚至全部应用无法访问存储，**此时正常重启即可**

#### 下载

**请确定已阅读说明，否则如果出现已经提到的情况，开发者会责怪你**

[Magisk 模块 v10 for arm](https://github.com/RikkaApps/StorageRedirect-assets/releases/download/assets/magisk-sr-native-inject-arm-v10.zip)

[Magisk 模块 v10 for arm64](https://github.com/RikkaApps/StorageRedirect-assets/releases/download/assets/magisk-sr-native-inject-arm64-v10.zip)

#### 如何确认已经起作用

* 开机过程中，观察有没有 `StorageRedirectInject: replaced com.android.internal.os.Zygote#nativeForkAndSpecialize` 的 log（由于会在非常早期的启动过程中被触发，必须连接电脑使用 adb 才可能看到）
* 当开启任意应用时，观察是否有如 `StorageRedirectInject: nativeForkAndSpecialize called, uid=` 的 log（任何可以读 log 的东西都可以）
* 检查 `/data/misc/storage_redirect` 下有没有如 _0.com.example_ (user.package_name) 这样的文件
