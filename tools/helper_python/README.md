# Storage Redirect 规则助手
- - - -
## 这是什么？
协助 Storage Redirect 规则贡献者管理最新版本的规则，可以从旧版本规则中迁移过来，根据当前各应用规则和手动编辑的列表合成一个已认证的清真应用列表，亦可以用于将普通用户通过应用内向导提交的应用规则批量下载到本地（仍需要人工检查导入）。

## 环境需求
1. Windows/Linux/mac OS
2. Python 3+
3. Git（可选）

## 开始使用
确保你准备好以上的基本环境后，并将本目录内的所有内容保存至本地（也可以通过 `git clone` 本仓库）。

本助手用到了 PyGithub 开源项目来访问 GitHub 接口，使用前需要执行下述命令安装库：

```
pip install PyGithub
```

完成后执行 `py main.py`可以看到助手返回的帮助信息，建议通过本页面代替助手内置的帮助文本了解使用，这会让你更快速地找到你想要的功能。

## 功能使用
### 生成已认证的应用列表
每次编辑完应用规则后，都应该重新生成一次已认证的应用规则，Storage Redirect 为确保效率从 `verified_apps.json` 中获取列表。

假设在 `D:\Projects` 内 clone 了 StorageRedirect-assets 仓库，规则位置应为 `D:\Projects\StorageRedirect-assets\rules`。

以上假设下执行下述命令即可生成已认证应用列表：
```
py main.py --make-verified-list=D:\Projects\StorageRedirect-assets\rules
```

助手则会生成 `verified_apps.output.json`，这个文件只是临时的列表，不可提交到仓库，且不应直接用于覆盖原来的文件，这会导致手动编辑加入的应用不包含在内。

#### 自动合并新生成的已认证应用列表（推荐）
助手新增了一个参数 `--merge-verified-list` 可以在生成完毕后自动合并两份列表（仅负责去重不会自动删除，若有原有已认证应用列表有必要的改动，请在合并后再修改）

### 从旧版本配置转换升级
从旧版本配置转换升级到最新版本，可以使用助手进行批量转换。

假设旧版本的应用规则仓库存放于 `D:\Projects\StorageRedirect-rules` （所有应用 `.json` 配置所在的位置），则执行下述命令来转换升级：
```
py main.py --convert=D:\Projects\StorageRedirect-rules
```

助手会在指定目录内生成 output 文件夹，并输出转换结果。

### 从 GitHub 仓库 Issues 中下载自动生成的规则
通过 GitHub API 批量下载仓库中由 Storage Redirect 规则提交向导生成的 Issues，并提取 JSON 输出保存下来，保存的内容仍需人工检查、补充完整信息才可导入所有规则中。

假设 GitHub 用户名和密码分别是 `example` 和 `123456` ，通过执行下述命令可以登入 API 开始下载：
```
py main.py --download-from-issues -g example+123456
```

输出结果会保存至命令运行所在目录的 output 文件夹中。

> 注意：`-g`（`--login-github`）用于传入 GitHub 的登录信息，更多用法请查阅下面的部分。

### 关闭 GitHub 仓库已被导入的自动生成规则
导入完毕规则后，可以通过 `--close-issues-if-existing=RULES_PATH` 命令关闭那些已被导入的规则。

假设 GitHub 用户名和密码分别是 `example` 和 `123456` ，通过执行下述命令可以登入 API 进行自动关闭：
```
py main.py --close-issues-if-existing=./rules -g example+123456
```

输出结果会直接显示到屏幕中。

> 注意：`-g`（`--login-github`）用于传入 GitHub 的登录信息，更多用法请查阅下面的部分。

## 更多参数
### GitHub 登录

`-g`（`--login-github`）用于传入 GitHub 的登录信息，可以使用 Access Token 或用户密码来登录。

当使用用户名和密码来登录时，使用 `+` 半角加号来连接用户名和密码：
```
-g example+123456
```

当使用 Access Token 时，直接接在后面：
```
-g abcdefgh1234567
```

## 有建议、遇到问题？
你可以以“[Helper]”为标题开头创建 GitHub Issues 反馈建议或问题。