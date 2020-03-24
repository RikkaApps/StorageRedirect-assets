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
  
## "Export isolated files" rules

> The following is "Export isolated files" rules. To create multiple rules, make multiple copies. If not please delete this paragraph.

### Export isolated files #1

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
