### Enhance module

The enhance module includes the following features:

* Guarantee _Storage Redirect_ starts early than normal apps during boot stage
* Guarantee redirected app\'s logic runs later than redirect
* Monitor file access in public storage (only monitors _open_ call in _libc_ from app processes)

#### Precautions

* **Must to cooperate with _Storage Redirect_ 0.15.0+**
* Try to disable (delete) it if you have any problem
* If there is a problem, it is helpful for developers to provide the log since booting
* (Magisk module) Before installation, **please make sure to confirm that you have learned how to remove the module when system can't start**, otherwise, you will not be able to enter the system if your system is not compatible with it
* (Magisk module) Require Magisk v15+
* (Magisk module) If you installed an old Magisk module, delete it

#### The difference between v12 and v12.1

V12.1 changes the policy so that the _Storage Redirect core service_ is started after the emulated storage is available and decrypted, instead of v12 during the boot process.

The benefit is that there will be no problem that all apps unable to access the storage (only appears on some devices).

But the downside is that it starts later. For devices that have encryption enabled and the decryption process is performed after the boot is completed (usually due to enable accessibility apps), if decryption (unlocking for the first time) is too late, it may cause the redirected accessibility apps or IME apps (and apps support Direct boot) unable to use. If you need to use the input method to unlock, do not enable redirect for this input method.

#### Download

**Please be sure to read the instructions, otherwise, developers will blame you if you report any of the conditions that already mentioned**

_Since this solution needs to replace system files, we only provide Magisk modules for now._

[Magisk module v12 for arm](https://github.com/RikkaApps/StorageRedirect-assets/releases/download/assets/magisk-sr-native-inject-arm-v12.zip)

[Magisk module v12 for arm64](https://github.com/RikkaApps/StorageRedirect-assets/releases/download/assets/magisk-sr-native-inject-arm64-v12.zip)

[Magisk module v12.1 for arm](https://github.com/RikkaApps/StorageRedirect-assets/releases/download/assets/magisk-sr-native-inject-arm-v12.1.zip)

[Magisk module v12.1 for arm64](https://github.com/RikkaApps/StorageRedirect-assets/releases/download/assets/magisk-sr-native-inject-arm64-v12.1.zip)

#### How to check if it works

* During the boot process, check if there is log like `StorageRedirectInject: replaced com.android.internal.os.Zygote#nativeForkAndSpecialize` (you must connect your device to PC and use adb logcat to check this log, because it will be triggered during the very early progress of booting)
* When opening any app, check if there is log like  `StorageRedirectInject: nativeForkAndSpecialize called, uid=` (use anything that can read log is ok)
* Check if there are files such as _0.com.example_ (user.package_name) under `/data/misc/storage_redirect`