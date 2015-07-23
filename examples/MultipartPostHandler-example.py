#!/usr/bin/python
"""
  The main function of this file is a sample which downloads a page and
  then uploads it to the W3C validator.
"""

def main_url_test():
    """Url test
    """
    import tempfile, sys, os, urllib2, MultipartPostHandler

    validatorURL = "http://validator.w3.org/check"
    opener = urllib2.build_opener(MultipartPostHandler.MultipartPostHandler)

    def validateFile(url):
        # temp = tempfile.mkstemp(suffix=".html")
        # os.write(temp[0], opener.open(url).read())
        params = { "ss" : "0",            # show source
            "doctype" : "Inline", 
            "uri" : url }
        print(opener.open(validatorURL, params).read())
        # os.remove(temp[1])

    if len(sys.argv[1:]) > 0:
        for arg in sys.argv[1:]:
            validateFile(arg)
    else:
        validateFile("http://www.google.com")


if __name__=="__main__":
    main_url_test()
