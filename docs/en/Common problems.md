### Before start

Please **read other help articles**, which will help you understand the meaning of some of these terms.

If you still can't solve the problem, please contact us through in-app "Help and support".

### Issues with specific applications

* Album is empty in "WeChat" app

  If other redirected applications work properly, you may need to try to clear the data of "WeChat". (We have not yet been able to reproduce the problem)

### Common problems

* Redirected apps still generate files

  Try [Enhance module](https://rikka.app/StorageRedirect/docs/en-US/?doc=enhanced)

* Unable to find file in redirected app

  1. Is the file not in _Standard folder_?

     The redirected app cannot access files not in _Standard folder_. See [About redirect](https://rikka.app/StorageRedirect/docs/en/?doc=About%20redirect) for detail.

  2. Is the redirect working abnormally?

     Check log, if the lines like `/mnt/runtime/write/emulated rw,nosuid,nodev,noexec,noatime,fsuid=1023,fsgid=1023,gid=9997,multiuser,mask=7,derive_gid` appears `gid= 1023` instead of `gid=9997` indicates that the redirection may start prematurely. Usually due to using the old Magisk module (before v12.1), please update to the latest version and delete the old one.

  3. Upgrade from Storage Redirection 0.9.0 Release (2018/01)?

     Due to changing operating principles, data of redirected app may need to be cleared.

* Unable to open file from redirected app

  This is due to a problem with the redirect app. See [About Redirect # Situations that affect the normal usage of redirected app](https://rikka.app/StorageRedirect/docs/en/?doc=About%20redirect) for detail.

* Unable to share to redirected app

  This is due to design issues with redirected app (and possibly the sharing app). See [About Redirect # Situations that affect the normal usage of redirected app](https://rikka.app/StorageRedirect/docs/en/?doc=About%20redirect) for detail.

  Please download our [Bridge](https://play.google.com/store/apps/details?id=moe.shizuku.bridge) app to use his "Forward share" feature to solve this problem. (You can also wait for us for other solution)

### How do I know if the redirect works?

First, make sure you are using unoffical versions such as "cracked version" and "unlocked version".

Through the in-app "logcat" function, after the redirected app is opened, the following log indicates that the redirect works normally.

```
Process started, pid= user= package= type=
(omitted)
/storage/emulated/0/Android/data/ rw,nosuid,nodev,noexec,noatime,fsuid=1023,fsgid=1023,gid=9997,multiuser,mask=7,derive_gid
(omitted)
```