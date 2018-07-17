### Behavior changes of redirected app

* Reading and writing files and folders other than _Standard folder_ will be redirected to their own redirected space.

  Each apps can be set whether its redirected target is in the data folder or the cache folder. If its redirected target is not specified, it will be same with the global settings, which default value is **"cache folder"**.

  - When redirecting to **the data folder** (the path format of data folder is generally `/sdcard/Android/data/<package_name>/sdcard`), redirected files and folders will not be deleted when clearing app cache. If you try to uninstall app, redirected space will be cleared.

  - When redirecting to **the cache folder** (the path format of cache folder is generally `/sdcard/Android/data/<package_name>/cache/sdcard`), redirected files and folders will be deleted when clearing app cache or uninstall app. If redirected app put its important data to non-standard folders, you may lose data with cache.

  For example, suppose you have an app named aaa (package: `example.aaa`) that actually writes (or reads) `/sdcard/Android/data/example.aaa/cache/sdcard` when it writes (or reads) `/sdcard/aaa/blbl.txt`, but not the files in _standard folders_.

* To avoid problems on some devices, from version 0.12.0, storage permission of redirected apps will be automatically granted when enabling redirect or start redirect service; from version 0.15.9, storage permission will be automatically granted when app starts

> _Standard folder_ refers to folders that Android will create by default, such as `Android`, `Pictures`, `Music` and so on. In future versions it is possible to specify separately for each application what is a standard folder.

### Redirected apps still generate files

Try [Enhance module](https://rikka.app/storage_redirect/docs/en-US/?doc=enhanced)

### Situations that affect the normal usage of redirected app

* The app uses system's _Download Manager_. If the downloaded file is saved outside of _Standard folder_, the app is not accessible to the file
* The app will not able to access files and folders outside of _standard folder_. App's feature such as send picture or send file will be affected of the file is not in _Standard folder_

### Note

* Redirected app will be force stopped when turning on redirecting
* Because files in `/sdcard` do not have a specific owner, files created by redirected app previously need to be deleted manually
* DO NOT revoke storage permission for redirected apps, or redirect will become invalid when grant storage permission runtime