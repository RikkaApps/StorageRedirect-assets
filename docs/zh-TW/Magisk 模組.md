### 被重新導向的程式仍不時建立文件

目前，_儲存重新導向_ 依靠 logcat 來獲知應用進程創建，因此當 _儲存重新導向_ 晚於程式啟動或 log 輸出晚於程式啟動，重新導向便不能及時生效。

為了徹底解決該問題，我們找到一種 _通過替換一個共享庫注入 zygote 進程並 "hook" 一個會在 fork 出程式進程時被調用的函數_ 的方案。藉此我們可以保證重新導向一定會在程式本身邏輯前執行。

由於該方案需要替換系統檔案，我們暫時只提供 Magisk 模組。

#### Magisk 模組使用前須知

* **必須配合 _儲存重新導向_ 0.14.0 版本或以上使用**，否則部分應用會無法啟動，聯絡開發者加入內部測試
* 需要使用 Magisk v15+
* 安裝前**請務必確認已經了解如何從 recovery 刪除模組**，否則如果系統與其不相容，將會無法進入系統
* 如果出現問題，提供開機以來的 log 給開發者會很有幫助
* 如果安裝了舊的 Magisk 模組 (sr starter)，請自行刪除

#### 已知問題

* 如果使用 Xposed 可能會無效
* _軟重啟_（非正常重啟）會導致 MTP，adb 甚至全部程式無法讀取儲存空間，**此時正常重啟即可**

#### 下載

**請確定已閱讀說明，否則如果出現已經提到的情況，開發者會責怪你**

[Magisk 模組 v9 for arm](https://github.com/RikkaApps/StorageRedirect-assets/releases/download/assets/magisk-sr-native-inject-arm-v9.zip)

[Magisk 模組 v9 for arm64](https://github.com/RikkaApps/StorageRedirect-assets/releases/download/assets/magisk-sr-native-inject-arm64-v9.zip)

#### 如何確認已經起作用

* 開機過程中，觀察有沒有 `StorageRedirectInject: replaced com.android.internal.os.Zygote#nativeForkAndSpecialize` 的 log（由於會在非常早期的啟動過程中被觸發，必須連接電腦使用 adb 才可能看到）
* 當開啟任意程式時，觀察是否有如 `StorageRedirectInject: nativeForkAndSpecialize called, uid=` 的 log（任何可以讀 log 的東西都可以）
* 檢查 `/data/misc/storage_redirect` 下有沒有如 _0.com.example_ (user.package_name) 這樣的文件
