## Why we need "Share Helper"?

After redirected, redirected apps cannot know the actual position of files in external storage. When they share files in a very old way that use an absolute file path (`file uri`), receivers will be mislead to a nonexistent file.

"Share Helper" can help you convert these absolute file path to a better `content uri`. When receivers try to access shared files, Storage Redirect will deliver the correct data to them.

## When should we use it? How to use it?

If you found some redirected apps cannot share any files to other applications, you can try to share files to **Share Helper** (Enable it at Storage Redirect Settings first), then choose your actual target receiver app.

## What is Direct Share?

It's a system feature from Android 6.0. It recommends frequent share targets in **Android System's Share Chooser**. When enabling Direct Share for Share Helper, you can choose what receiver apps to pin and order them in Storage Redirect Settings. Finally, you can convert absolute file uri sharing quickly.