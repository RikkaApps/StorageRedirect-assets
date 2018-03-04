### Upgrade from 0.9.x (and earlier)

> In 0.11.0 and later version, we use a completely different method of implementation. The problem that hard-coded `/sdcard` cannot be redirected is solved, so some features have been modified.

* The _Block writing file_ feature is removed
 
  Since this feature is implemented with the help of Android system's appops, the settings you have made will not be disabled automatically.

  You'll need to use command `appops set <PACKAGE> WRITE_EXTERNAL_STORAGE allow` in shell to restore settings (or with other appops wrapper app such as [Rikka's App Ops app](https://play.google.com/store/apps/details?id=rikka.appops)), otherwise **the app may not work**.

* Default redirect target is modified

  New Default redirect target will be `/sdcard/Android/data/<package>/cache/sdcard`. You will need to delete /sdcard/Android/data/<package>/storage and /sdcard/Android/data/<package>/cache/storage manually.