### Why do we need a link?

After the redirecting is turned on, useful files that were originally saved outside of _Standard folder_ (eg this app saves images in `/sdcard/blbl/saved_images`) will be saved in `/sdcard/Android/data/<package>/cache/sdcard/blbl/1.jpg`.

System's media storage or other applications will not scan this path, so these files need to be made available in the _Standard folder_ via link functions (eg `/sdcard/Pictures/example/1.jpg`).

### behavior

* This is a hard link
* When deleting external files (such as `/sdcard/Picture/example/1.jpg`), internal files will always be deleted (such as `/sdcard/Android/data/example/cache/sdcard/blbl/saved_images/1.jpg`)
* Only when the application is running, deleting the internal file will result in external files being deleted simultaneously (before Android 8.0, non-primary user applications will be regarded as always running)
* When clearing cache or data through the system, the application isn’t running, so there is no risk of losing files while performing these actions.