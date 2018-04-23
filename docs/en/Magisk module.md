### Redirected apps still create files sometimes

Currently, _Store Redirect_ depends on logcat to detect app process creation, so when _Store Redirect_ is later than app start or log output is later than app start, redirection will not take effect in time.

In order to completely solve this problem, we find a way that _inject the zygote process by replacing a shared library and "hook" a function that will be called when the app process is forked_. By this we can guarantee that the redirection will run before the app's own logic.

Since this solution needs to replace system files, we only provide Magisk modules for now.

#### Requirement

* Require Magisk v15+
* **Need to cooperate with _Storage Redirect_ 0.13.0+**, contact the developer to join the test
* **Before installation, please make sure to confirm that you have learned how to remove the module from recovery, otherwise you will not be able to enter the system if you cannot use it**
* If there is a problem, it is helpful for developers to provide the log since booting
* If you installed an old Magisk module (sr start), delete it yourself

#### Download

**Please be sure to read the instructions, otherwise, developers will blame you if you report any of the conditions that already mentioned**

[Magisk module for arm](https://github.com/RikkaApps/StorageRedirect-assets/releases/download/assets/magisk-sr-native-inject-arm.zip)

[Magisk module for arm64](https://github.com/RikkaApps/StorageRedirect-assets/releases/download/assets/magisk-sr-native-inject-arm64.zip)