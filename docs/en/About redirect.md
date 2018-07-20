### Behavior changes of redirected app

* Reading and writing files and folders other than _Standard folder_ will be redirected to "redirect target" folder.

  For example, suppose you have an app named aaa (package: `example.aaa`) that actually writes (or reads) _"redirect target" folder_ (default `Android/data/example.aaa/sdcard`) when it writes (or reads) `aaa/blbl.txt`, but not the files in _standard folders_.

* Files written outside the _Standard folder_ are managed by Android system
  * These files are accounted in storage usage
  * These files will be removed when clear app data (or cache, depends on "redirect target" folder setting) or uninstall app

> "Redirect target" folder can be customized, set globally in settings, or configured for a single app.

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
* To avoid problems on some devices, from version 0.12.0, storage permission of redirected apps will be automatically granted when enabling redirect or start redirect service; from version 0.15.9, storage permission will be automatically granted when app starts