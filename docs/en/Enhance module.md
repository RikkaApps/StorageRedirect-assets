### Enhance module

The enhance module includes the following features:

* Guarantee _Storage Redirect_ starts early than normal apps during boot stage
* Guarantee redirected app\'s logic runs later than redirect
* Monitor file access in public storage

#### Precautions

* **Must to cooperate with _Storage Redirect_ 0.15.0+**
* Try to disable (delete) it if you have any problem
* If there is a problem, it is helpful for developers to provide the log since booting
* (Magisk module) Before installation, **please make sure to confirm that you have learned how to remove the module when system can't start**, otherwise, you will not be able to enter the system if your system is not compatible with it
* (Magisk module) Require Magisk v15+
* (Magisk module) If you installed an old Magisk module, delete it


#### Known issues

* May not work if Xposed installed
* MTP, adb and even all apps will not be able to access storage after _soft reboot_ (abnormal reboot), **just reboot if you have this problem**

#### Download

**Please be sure to read the instructions, otherwise, developers will blame you if you report any of the conditions that already mentioned**

_Since this solution needs to replace system files, we only provide Magisk modules for now._

[Magisk module v12 for arm](https://github.com/RikkaApps/StorageRedirect-assets/releases/download/assets/magisk-sr-native-inject-arm-v12.zip)

[Magisk module v12 for arm64](https://github.com/RikkaApps/StorageRedirect-assets/releases/download/assets/magisk-sr-native-inject-arm64-v12.zip)

#### How to check if it works

* During the boot process, check if there is log like `StorageRedirectInject: replaced com.android.internal.os.Zygote#nativeForkAndSpecialize` (you must connect your device to PC and use adb logcat to check this log, because it will be triggered during the very early progress of booting)
* When opening any app, check if there is log like  `StorageRedirectInject: nativeForkAndSpecialize called, uid=` (use anything that can read log is ok)
* Check if there are files such as _0.com.example_ (user.package_name) under `/data/misc/storage_redirect`