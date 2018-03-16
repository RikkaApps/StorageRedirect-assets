# 应用规则格式 (`rules/apps`)

## 文件格式

文件名应是以应用的包名为前缀，以 `.json` 为后缀名。如微信：`com.tencent.mm.json`

文件内容应是 JSON 标准格式，且使用 UTF-8 编码。

## JSON 格式 
|             |      | 类型           | 说明                                                                           |
| :---------- | :--- | :------------- | :----------------------------------------------------------------------------- |
| package     | 必选 | string         | 包名                                                                           |
| verified    | 可选 | bool           | 是否是“认证应用”（不会在非标准位置产生文件）                                 |
| recommended | 必选 | bool           | 是否推荐开启重定向，只有使用了系统 _下载管理器_ 和 _文档_ 的应用可能会产生问题 |
| description | 可选 | description    | 自定义说明文本，格式见下面说明                                                 |
| authors     | 必选 | string[]       | 作者                                                                           |
| observers   | 可选 | ObserverInfo[] | 链接功能，具体见下表                                                           |

* 不需要开启重定向的应用也可以提交，`verified` 为 true 即可。

### description 解释
以 `语言_地区` （如 `zh_CN`）为 key，内容为 value。

如果有 `"overwrite_default": true` 则不会显示默认文字，否则将会加在默认文字后面。

#### 解析过程
例子：
```
"description": {
	"zh_CN": "简体中文",
	"zh": "中文",
	"en": "当前语言不符合其他 key 时使用"
}
```
解析时，将进行三次匹配，第一次匹配与当前语言完全相同的，第二次只匹配语言而忽视地区，第三次匹配与当前语言相同的（如 `zh-TW` 在只有 `zh-CN` 会使用 `zh-CN`），仍找不到使用 `en`。

### ObserverInfo 解释
|                    |      | 类型   | 说明                                                          |
| :----------------- | :--- | :----- | :------------------------------------------------------------ |
| description        | 必选 | string | 类型，具体要求见下表                                          |
| source             | 必选 | string | 从这里，不必包含 `/Android/data/[package]/cache/sdcard`       |
| target             | 必选 | string | 到这里，具体要求见下表                                        |
| call\_media\_scan  | 可选 | bool   | 是否发送 MEDIA\_SCAN 广播。多媒体文件建议开启以触发媒体库更新 |
| add\_to\_downloads | 可选 | bool   | 是否添加到系统的下载管理器列表中。下载的类型建议开启该项      |
| mask               | 可选 | string | 正则表达式。匹配该正则表达式的文件才会被处理，不写则表示全部  |
| allow_child        | 可选 | bool   | 是否允许子文件夹                                              |

**链接功能以还原原本功能为目标**（比如原来有保存到相册的功能，重定向后会失效，需要通过链接还原该功能），**不可以有超越原本功能的行为**（比如把缓存的文件链接出来）

#### description 解释
| description        | 含义       | target               |
| :----------------- | :--------- | :------------------- |
| saved\_pictures    | 保存的图片 | Pictures/<app_name>  |
| saved\_photos      | 保存的照片 | Pictures/<app_name>  |
| saved\_videos      | 保存的视频 | Movies/<app_name>    |
| saved\_music       | 保存的音乐 | Music/<app_name>     |
| saved\_files       | 保存的文件 | Download/<app_name>  |
| downloaded\_pictures | 下载的图片 | Pictures/<app_name>  |
| downloaded\_videos   | 下载的视频 | Movies/<app_name>    |
| downloaded\_music    | 下载的音乐 | Music/<app_name>     |
| downloaded\_files    | 下载的文件 | Download/<app_name>  |
| app\_backup        | 应用的备份 | Documents/<app_name> |


* <app_name>为该应用常见英文称呼
* 该表作为指引，如有特殊情况 target 可稍作变通。如想增加 description 请先修改该表并提交 Pull requests。

## 应用规则样例分析

内容有所精简，仅供参考，请以实际需求为准编写规则：

（注释仅供分析使用，实际上 JSON 不支持双斜杠注释）

```json
{
  "package": "com.tencent.mm", // 应用包名
  "recommended": true, // 应用开启了重定向也不大影响正常使用，应当推荐
  "verified": false, // 应用会产生非标准的文件夹，因此不认证
  "description": { // 开启了重定向需要注意的操作和产生的负面效果
    "zh_CN": "<b>开启后请谨慎清理应用缓存，否则可能会造成聊天图片丢失！</b>",
    "zh": "<b>開啟後請謹慎清理程式緩存，否則可能會造成聊天圖片丟失！</b>",
    "en": "<b>Please do not clean up the application cache, otherwise the pictures in chats may lost.</b>"
  },
  "authors": [ // 作者们的名字都应保留，请勿随意删除覆盖
    "DEVELOPER", // `DEVELOPER` 是 Storage Redirect 开发者（Rikka（（
    "CubeSky",
    "Shane"
  ],
  "observers": [ // 重定向的链接规则，将不标准的文件位置移到标准的公共目录
    { // 这一项链接可以将不标准的图片保存位置移向标准的公共目录
      "call_media_scan": true, // 图片保存后应当通知系统扫描，否则图库会找不到
      "add_to_downloads": false, // 不是下载的文件
      "source": "tencent/MicroMsg/WeiXin", // 不标准的文件位置
      "target": "Pictures/WeChat", // 目标的目录，只能是标准的公共目录
      "description": "saved_pictures", // 保存的图片，格式看上表
      "allow_child": false // 不允许子文件夹
    },
    {
      "call_media_scan": true,
      "add_to_downloads": true, // 是下载的文件
      "source": "tencent/MicroMsg/Download",
      "target": "Download/WeChat",
      "description": "saved_files",
      "allow_child": false
    }
  ]
}
```