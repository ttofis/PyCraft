"""
The PyCraft API.
Designed for easy access to the wide variety of Minecraft APIs.
You are allowed to use this in any of your projects provided you give credit.
See something you think you can contribute and make it better? Fork now and make a pull request!
Made by @ELChris414
"""
from __future__ import print_function

import json
import sys

"""
Sys is used to recognise the version of python, so anyone can use it with Python 2 or 3.
"""

if (sys.version_info >= (3, 0)):
	import urllib.request
	urlopen = urllib.request.urlopen
else:
	import urllib2
	urlopen = urllib2.urlopen
