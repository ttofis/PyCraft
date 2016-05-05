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
import base64

"""
Sys is used to recognise the version of python, so anyone can use it with Python 2 or 3.
"""

if (sys.version_info >= (3, 0)):
	import urllib.request
	def urlopen(link):
		return urllib.request.urlopen(link).read().decode("utf-8")
else:
	import urllib2
	def urlopen(link):
		return urllib2.urlopen(link).read()


"""
In this case, we do not need to use a class as already we are using pycraft. and the function that we want. No information needed.
"""
def getUUID(username):
	"""
	It returns the UUID value of the specified username as a string
	"""
	return json.loads(urlopen("https://api.mojang.com/users/profiles/minecraft/" + username)).get("id")

def getNameHistory(username):
	"""
	It returns a JSON tree of all the name changes that are found for the given username
	You might want to use something like json.loads(pycraft.getNameHistory(*username that you want*))[*information that you want*]
	"""
	return urlopen("https://api.mojang.com/user/profiles/" + getUUID(username) + "/names")

def getMojangServerStatus():
	"""
	It returns a JSON tree of all the Mojang Server Statuses
	You might want to use something like json.loads(pycraft.getMojangServerStatus())[*information that you want*]
	Or you can use the next function which gives more precise information
	"""
	return urlopen("https://status.mojang.com/check")

def getSpecificMojangServerStatus(server):
	"""
	It is given a string with the server name and it outputs the status of that server
	"""
	if (server == "minecraft.net"):
		serverID = 0
	elif (server == "session.minecraft.net"):
		serverID = 1
	elif (server == "account.mojang.com"):
		serverID = 2
	elif (server == "auth.mojang.com"):
		serverID = 3
	elif (server == "skins.minecraft.net"):
		serverID = 4
	elif (server == "authserver.mojang.com"):
		serverID = 5
	elif (server == "sessionserver.mojang.com"):
		serverID = 6
	elif (server == "api.mojang.com"):
		serverID = 7
	elif (server == "textures.minecraft.net"):
		serverID = 8
	elif (server == "mojang.com"):
		serverID = 9
	else:
		raise TypeError("That Server doesn't exist!")
	return json.loads(getMojangServerStatus())[serverID][server]

def getProfile(username):
	"""
	It returns a JSON tree of all information about the given UUID's profile.
	You might want to use something like json.loads(pycraft.getProfile(*username that you want*))[*information that you want*]
	Or you can use the next functions which give more precise information
	"""
	return urlopen("https://sessionserver.mojang.com/session/minecraft/profile/" + getUUID(username))

def getProfileValue(username):
	"""
	It returns a JSON tree of all information about the given UUID's profile value. That includes profileId, profileName, skin and cape (if existant)
	You might want to use something like json.loads(pycraft.getProfileValue(*username that you want*))[*information that you want*]
	Or you can use the next functions which give more precise information
	"""
	return base64.b64decode(json.loads(getProfile(username))["properties"][0]["value"]).decode("utf-8")