#!C:\\Python26\\python.exe
#-*- coding: ISO-8859-1 -*-

print "Content-type: text/html; ISO-8859-1"  

import Cookie
import os

print "Content-type: text/plain\n"

try:
    cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
    print cookie["session"].value
except (Cookie.CookieError, KeyError):
    print "session cookie not set!"
