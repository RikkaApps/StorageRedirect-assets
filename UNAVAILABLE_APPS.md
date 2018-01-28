# [虾米音乐 (xiami music)](#fm.xiami.main)
  
**分析：**

经过反编译，在 API 23 以上，
虾米使用 `context.getExternalFilesDirs` 的结果的 `/Android` 前面的内容作为存储空间位置，
会和 `Environment.getExternalStorageDirectory()` 的结果进行比较，如果不一样就认为不可用。
  
由于重定向之后的存储空间位置在只截取 `/Android` 前内容时会是真实存储空间位置，会和 
`Environment.getExternalStorageDirectory()` 结果不同，因此会认为存储空间不可用。
