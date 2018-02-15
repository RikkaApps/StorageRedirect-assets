# 如何提交自己的规则

fork该仓库，新建`[package].json`文件，按照以下格式编辑。可一次编写多个应用，最后向我们打开一个 Pull requests 即可。


## json
|                   |    | 类型             | 说明                                         |
|:------------------|:---|:---------------|:-------------------------------------------|
| package           | 必选 | string         | 包名                                         |
| recommended       | 必选 | bool           | 是否推荐开启重定向                                  |
| need\_appops      | 可选 | bool           | 是否需要配合 appops 彻底禁止写入。只有当重定向后还会在其它位置产生文件才需要 |
| feature\_affected | 必选 | bool           | 是否影响应用的功能。**比如有发送文件类似的功能就肯定会被影响**          |
| reason            | 可选 | Reason         | 自定义说明文本，格式见下面说明                            |
| authors           | 必选 | string[]       | 作者                                         |
| observers         | 可选 | ObserverInfo[] | 链接功能，具体见下表                                 |

* 不需要开启重定向的应用也可以提交，`recommended` 与 `feature_affected` 同为 false 即可。
* 如果重定向会严重影响应用功能，不推荐开启并且将 `feature_affected` 设置为 true 。

### Reason (需要 0.8.1 以上）
以 `语言_地区` （如 `zh_CN`）为 key，内容为 value。

例子：
```
"reason": {
	"zh_CN": "简体中文",
	"zh": "中文",
	"default": "当前语言不符合其他 key 时使用"
}
```
解析时，将进行三次匹配，第一次匹配与当前语言完全相同的，第二次只匹配语言而忽视地区，第三次匹配与当前语言相同的（如 `zh-TW` 在只有 `zh-CN` 会使用 `zh-CN`），仍找不到使用 `en`。

如果不填写，根据 `recommended` 和 `feature_affected` 的不同会使用如下的内置文本：

| recommended | feature_affected | 结果                                               |
|-------------|------------------|----------------------------------------------------|
| true        | false            | 不影响该应用的功能。                               |
| true        | true             | 但是由于依赖扫描存储空间，一些非核心功能会被影响。 |
| false       | true             | 该应用的核心功能依赖扫描存储空间或写死了存储目录。 |
| false       | false            | 该应用没有非标准行为。                             |

### ObserverInfo 
|                  |    |类型  |说明                                                         |
|------------------|----|------|-------------------------------------------------------------|
|description       |必选|string|类型，具体要求见下表                                         |
|call\_media\_scan |可选|bool  |是否发送 MEDIA\_SCAN 广播。多媒体文件建议开启以触发媒体库更新|
|add\_to\_downloads|可选|bool  |是否添加到系统的下载管理器列表中。下载的类型建议开启该项     |
|mask              |可选|string|正则表达式。匹配该正则表达式的文件才会被处理，不写则表示全部 |
|source            |必选|string|从这里，不必包含 `/Android/data/[package]/storage`           |
|target            |必选|string|到这里，具体要求见下表                                       |

* **链接功能以还原原本功能为目标**（比如原来有保存到相册的功能，重定向后会失效，需要通过链接还原该功能），**不可以有超越原本功能的行为**（比如把缓存的文件链接出来）

#### description
|description       |含义      |target              |
|------------------|----------|--------------------|
|saved\_pictures   |保存的图片|Pictures/<app_name> |
|saved\_photos     |保存的照片|Pictures/<app_name> |
|saved\_videos     |保存的视频|Movies/<app_name>   |
|saved\_music      |保存的音乐|Music/<app_name>    |
|saved\_files      |保存的文件|Download/<app_name> |
|download\_pictures|下载的图片|Pictures/<app_name> |
|download\_videos  |下载的视频|Movies/<app_name>   |
|download\_music   |下载的音乐|Music/<app_name>    |
|download\_files   |下载的文件|Download/<app_name> |
|app\_backup       |应用的备份|Documents/<app_name>|


* <app_name>为该应用常见英文称呼
* 该表作为指引，如有特殊情况 target 可稍作变通。如想增加 description 请先修改该表并提交 Pull requests。
