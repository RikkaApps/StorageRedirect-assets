### Upgrade from 0.9.x (and earlier)

> In 0.11.0 and later version, we use a completely different method of implementation. The problem that hard-coded `/sdcard` cannot be redirected is solved, so some features have been modified.

* Default redirect target is modified

  You will need to delete `/sdcard/Android/data/<package>/storage` and `/sdcard/Android/data/<package>/cache/storage` manually.