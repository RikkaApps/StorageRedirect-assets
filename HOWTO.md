# 如何提交自己的规则

## json
| |类型|解释|
|--|--|--|
|package|string|包名|
|recommended|bool|是否推荐开启|
|need\_appops|bool|是否需要配合 appops 彻底禁止写入|
|feature\_affected|bool|是否影响应用的功能|
|authors|string[]|作者|
|observers|ObserverInfo[]|ObserverInfo|

### ObserverInfo 
| |类型|解释|
|--|--|--|
|mode|int|模式, 0=移动文件 1=挂载，对于会影响应用功能的请选择挂载|
|call\_media\_scan|bool|是否发送 MEDIA\_SACN 广播|
|add\_to\_downloads|bool|是否加入加入下载并发送通知|
|mask|string|匹配该正则表达式的文件才会被处理，不写则表示全部|
|source|string|从这里，不必包含 `/Android/data/[package]/storage`|
|target|string|到这里|
