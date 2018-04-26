### Redirected apps still create files sometimes

Currently, _Store Redirect_ depends on logcat to detect app process creation, so when _Store Redirect_ is later than app start or log output is later than app start, redirection will not take effect in time.

In order to completely solve this problem, we find a way that _inject the zygote process by replacing a shared library and "hook" a function that will be called when the app process is forked_. By this we can guarantee that the redirection will run before the app's own logic.

Since this solution needs to replace system files, we only provide Magisk modules for now.

#### Must read before use Magisk module

* Require Magisk v15+
* Before installation, **please make sure to confirm that you have learned how to remove the module from recovery**, otherwise, you will not be able to enter the system if your system is not compatible with it
* **Must to cooperate with _Storage Redirect_ 0.13.1+**, contact developer to  join the test
* **May not work if Xposed installed**, see below to learn how to check if it works
* If there is a problem, it is helpful for developers to provide the log since booting
* If you installed an old Magisk module (sr start), delete it yourself

#### Download

**Please be sure to read the instructions, otherwise, developers will blame you if you report any of the conditions that already mentioned**

[Magisk module v7 for arm](https://github.com/RikkaApps/StorageRedirect-assets/releases/download/assets/magisk-sr-native-inject-arm-v7.zip)

[Magisk module v7 for arm64](https://github.com/RikkaApps/StorageRedirect-assets/releases/download/assets/magisk-sr-native-inject-arm64-v7.zip)

#### How to check if it works

* During the boot process, check if there is log like `StorageRedirectInject: replaced com.android.internal.os.Zygote#nativeForkAndSpecialize` (you must connect your device to PC and use adb logcat to check this log, because it will be triggered during the very early progress of booting)
* When opening any app, check if there is log like  `StorageRedirectInject: nativeForkAndSpecialize called, uid=` (use anything that can read log is ok)
* Check if there are files such as _0.com.example_ (user.package_name) under `/data/misc/storage_redirect`