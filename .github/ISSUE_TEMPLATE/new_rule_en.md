---
name: Submit a new rule
about: Submit a new rule for an app
---

## Basic information

> If you know how to write rule in JSON format, we recommend using Pull Request to submit rules to us.

- Application Id (package name): 

  Required.
  
- Display name of the app:
  
  Required.

- Application version:
  
  Optional.

- Is the app abuses storage:
  
  Required.

- It the app works after isolation / Notes:
  
  Required. If there are some functions not work after isolation or there are special notes, please explain.

- Recommendations for "Accessible folders":
  
  Optional. If the app has the function of sending pictures, you can suggest setting the picture folders as accessible folders.
  
## "Export isolated files" rules

> The following is "Export isolated files" rules. To create multiple rules, make multiple copies. If not please delete this paragraph.

### Export isolated files 01

- File type:

  Required. Such as "Saved images".
  
- Source folder (Where are the files):
  
  Required. A folder located in isolated storage. Such as "example/images".
  
- Target folder (Where they should be):

  Required. Such as "Pictures/Example".
  
- Regular expression for file name:
  
  Optional. Only files that match the regular expression will be exported.

- Whether to show notifications:

  Required. For scenario such as downloading files.
  
- Whether to notify Media Store:

  Required. For scenario such as saving images.

## "Access folders from other apps" rule

> The following is "Access folders from other apps" rules. If you need to create multiple rules, please make multiple copies. If not please delete the paragraph.

### Access folders from other apps 01

- What problem was solved:

  Required.

- Source app (Who created the file):

  Required.

- Folder list:

  Required.