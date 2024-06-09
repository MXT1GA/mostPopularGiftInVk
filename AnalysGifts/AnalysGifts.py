import requests
from token_profile import *

class ListGifts():
    def __init__(self, list_gifts):
        self.list_gifts = []
    def add_to_list(self, gift):
        self.list_gifts.append(gift)

class User():
    def __init__(self, userid, vivsble_gifts):
        self.userid = userid
        self.visible_gifts = False
    def reutrn_visible(self):
        return self.visible_gifts

class Api_vk():
    def __init__(self, token_vk, user_id):
        self.token_vk = token_vk
        self.user_id = user_id
        self.vvers = 5.199
    def __getGifts(self):
        getgifts = requests.get(f'https://api.vk.com/method/gifts.get?access_token={self.token_vk}&user_id={self.user_id}&v={self.vvers}')
        return getgifts
    def show_gifts(self):
        return self.__getGifts()

class Gift():
    def __init__(self, gift_id):
        self.gift_id = gift_id
    def return_gift_massive(self):
        Api_vk(token, 19).show_gifts().json()["response"]["items"]
        
