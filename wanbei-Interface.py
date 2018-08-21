#!/usr/bin/env python
# -- coding: utf-8 --

import requests
import json

url = 'http://app.test.gc.xf.io/login/v1'
user = {
  "mobile": "17611111111",
  "password": "111111",
  "type": 1
}

r = requests.post(url, json = user)

rUser = r.text
print rUser
#a = json.loads(rUser)
#print a["data"]["token"]



class requestsBody():

  def __init__(self):
    pass

  def test1(self, rBody, vlaue1):
    loadsBody = json.loads(rBody)
    return loadsBody[(vlaue1)]

  def test2(self, rBody, vlaue1, vlaue2):
    loadsBody = json.loads(rBody)
    return loadsBody[(vlaue1)][(vlaue2)]

  def test3(self, rBody, vlaue1, vlaue2, vlaue3):
    loadsBody = json.loads(rBody)
    return loadsBody[(vlaue1)][(vlaue2)][(vlaue3)]

  def test4(self, rBody, vlaue1, vlaue2, vlaue3, vlaue4):
    loadsBody = json.loads(rBody)
    return loadsBody[(vlaue1)][(vlaue2)][(vlaue3)][(vlaue4)]

textBody = requestsBody()
print textBody.test2(rUser, "data", "token")





