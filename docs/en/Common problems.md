### Before start

If you still can't solve the problem, please contact us through in-app "Help and support".

### Issues with specific applications

* **Album is empty in "WeChat" app**

  If other redirected applications work properly, you may need to try to clear the data of "WeChat". (We have not yet been able to reproduce the problem)

### Specific device issues

* **Does not work on Huawei EMUI**

  EMUI presets log off, and "store redirects" rely on logcat for information. Please ask yourself how to enable log on EMUI.

### General problems

* **Redirection should not work**

  With the "log monitoring" function in the application, after the application to be redirected is started, the following log indicates that the redirect should work normally.

  If there is no log, please check if the log in "Developer Settings" is closed.

  ```
  Process started, pid= user= package= type=
  (omitted)
  /storage/emulated/0/Android/data/ rw,nosuid,nodev,noexec,noatime,fsuid=1023, fsgid=1023,gid=9997,multiuser,mask=7,derive_gid
  (omitted)
  ```

* **Redirected apps still generate files**

  Try [Enhance module](https://rikka.app/StorageRedirect/docs/en-US/?doc=enhanced)

* **Unable to find file in redirected app**

  1. Is the file not in _Standard folder_?

     The redirected app cannot access files not in _Standard folder_. See [About redirect](https://rikka.app/StorageRedirect/docs/en/?doc=About%20redirect) for detail.

  2. Is the redirect working abnormally?

     Check log, if the lines like `/mnt/runtime/write/emulated rw,nosuid,nodev,noexec,noatime,fsuid=1023,fsgid=1023,gid=9997,multiuser,mask=7,derive_gid` appears `gid= 1023` instead of `gid=9997` indicates that the redirection may start prematurely. Usually due to using the old Magisk module (before v12.1), please update to the latest version and delete the old one.

  3. Upgrade from Storage Redirection 0.9.0 Release (2018/01)?

     Due to changing operating principles, data of redirected app may need to be cleared.

* **Unable to open file from redirected app**

  This is due to a problem with the redirect app. See [About Redirect # Situations that affect the normal usage of redirected app](https://rikka.app/StorageRedirect/docs/en/?doc=About%20redirect) for detail.

* **Unable to share to redirected app**

  This is due to design issues with redirected app (and possibly the sharing app). See [About Redirect # Situations that affect the normal usage of redirected app](https://rikka.app/StorageRedirect/docs/en/?doc=About%20redirect) for detail.

  Please download our [Bridge](https://play.google.com/store/apps/details?id=moe.shizuku.bridge) app to use his "Forward share" feature to solve this problem. (You can also wait for us for other solution)