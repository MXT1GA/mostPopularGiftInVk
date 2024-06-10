import requests
from token_profile import *
import sqlite3
        
class Api_vk():
    def __init__(self, token_vk, user_id):
        self.token_vk = token_vk
        self.user_id = user_id
        self.vvers = 5.199
    def __getGifts(self):
        getgifts = requests.get(f'https://api.vk.com/method/gifts.get?access_token={self.token_vk}&user_id={self.user_id}&v={self.vvers}')
        return getgifts
    def show_gifts(self):
        gifts = []
        try:
            for i in self.__getGifts().json()["response"]["items"]:
                gifts.append(i["gift"]["id"])
        except:
            print(self.__getGifts().json())
        gifts.sort()
        return gifts

class Get_members():
    def __init__(self, group_id, count, token_vk):
        self.token_vk = token_vk
        self.group_id = group_id
        self.vvers = 5.199
        self.count = count
    def __getMembers(self):
        getUsers = requests.get(f'https://api.vk.com/method/groups.getMembers?access_token={self.token_vk}&group_id={self.group_id}&count={self.count}&v={self.vvers}')
        return getUsers
    def show_members(self):
        members = []
        try:
            for i in self.__getMembers().json()["response"]["items"]:
                members.append(i)
        except:
            print(self.__getMembers().json())
        members.sort()
        return members

class GetterGifts():
    def __init__(self):
        self.token_vk = token
        self.group_id = groupId
        self.count = count
    def __getallgifts(self):
        for i in Get_members(groupId, count, token).show_members():
            with open("dbgifts.txt", "a") as f:
                for value in Api_vk(token, i).show_gifts():
                  print(value)
                  f.write(str(value) + "\n")
    def run_code(self):
        self.__getallgifts()

a = GetterGifts()
a.run_code()

    
#print(Api_vk(token, 1).show_gifts())
#print(Get_members(91050183, 10, token).show_members())
