MultipartPostHandler2
=====================

MultipartPostHandler for Python 2

OldPanda's Update
---
I modified this library to allow uploading file directly from an url. Please refer to **Example** below for basic usage. 

Usage
---   
Enables the use of multipart/form-data for posting forms

Inspirations   
---
###Upload files in python:   
[http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/146306](http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/146306)    
###urllib2_file:   
Fabien Seisen: <fabien@seisen.org>

###Example:

```
import MultipartPostHandler, urllib2
opener = urllib2.build_opener(MultipartPostHandler.MultipartPostHandler)
params = { "username" : "bob", "password" : "riviera",
            "file" : url }
opener.open("http://wwww.bobsite.com/upload/", params)
```

Further Example
---
The main function of this file is a sample which downloads a page and then uploads it to the W3C validator.

