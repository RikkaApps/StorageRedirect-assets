---
name: Submit new rules / 提交新规则
about: Submit new rules and share your recommendation for apps

---

## Basic information / 基本信息

> The following content is divided into required and optional. 
  Please delete content in parentheses after finishing the form. 
  If you know how to write rules in JSON format, recommended to submit 
  rules by pull request.
> 以下内容分为必填和选填，填写完毕好请记得删去括号内容，
  如了解如何使用 JSON 格式编写规则建议，建议使用 Pull Request 向我们提交规则。

- Application package name / 应用包名：
  
  (Required 必填)
  
  
- Application title / 应用标题：
  
  (Required. Fill in app's display name / 必填，填入应用显示名称)
  
  
- Application version / 应用版本：
  
  (Optional. Fill in rules fits which version of app /
  尽量填写，填入规则适用的应用版本，如能提供官方何时更新版本更好)


- If application exists non-standard file writing behavior / 应用是否存在不规范的文件写入情况：
  
  (Required. If application produces files out of Android standard's public folders and 
  its private data folders, it exists non-standard file writing behavior.
  For example, saving pictures into tencent/wechat but not Pictures/WeChat)
  （必填，如果应用在 Android 规范的公共目录及自己的私有数据目录以外产生文件，
  则存在不规范的文件写入，如 “在 tencent/wechat 下保存图片而不是 Pictures/WeChat”）
  
  
- If application works normally when redirected / 重定向后应用能否继续正常工作：
  
  (Required. Working normally means major functions in app won't be broken. If existing 
  some functions not working, please tell us in the following description)
  （必填，正常工作即应用内的主要功能正常，若存在小部分功能无法使用，请在下面的说明中注明）
  
  
- What should be noticed when redirected / 重定向注意事项：
  
  (Optional. It will produce description by if existing bad behavior and if working 
  normally when redirected if you leave blank here.)
  （选填，留空则根据是否存在不规范行为和能否在重定向后正常工作生成说明）
  
  
## Links suggestion / 链接建议

> The following content is what information is required for submitting one link. 
  If you want to create multiple links suggestions, please copy multiple copies. 
  If you have no suggestion, please delete this section.
> 以下内容为提交一条链接需要的信息，如需创建多条链接建议，请复制多份。如果没有建议，请删除这个章节。

### Link 1 / 链接 1

- What files need to be linked out / 有什么文件需要链接到外面： 
  For example, saved pictures / songs / videos / files. 例如，保存的图片/音乐/视频/文件。
  
  (Required. If you want to link more than one folders, please create other links.)
  （必填，如果你想链接多个文件夹，请创建另外的链接。）
  
  
- Which folder will they be saved into / 文件将会被存在哪一个文件夹中：
  
  (Required. Relative position of folders in redirect target)
  （必填，重定向空间内的文件夹相对位置）
  
  
- Where should they be saved into / 文件应当被存在哪里：

  (Required. For example, "Pictures/Twitter")
  （必填，例如 “Pictures/Weibo”）
  
  
- Filter regular expression / 过滤正则表达式：

  (Optional. Learn more by reading help in this repository)
  （选填，要了解更多请通过阅读本仓库中的帮助）
  
  
- Should show a notification when created / 当创建时是否需要显示通知：

  (Required. If you want to open files in other applications at once, 
  recommended to turn it on)
  （必填，当你想要马上在其它应用中打开文件，建议打开这项）
  
  
- If they are multimedia files / 它们是多媒体文件吗：

  (Required. When it sets to true, media storage will be notified when 
  files are created)
  （必须，当它被设定为真时，媒体存储会被通知文件的创建）
