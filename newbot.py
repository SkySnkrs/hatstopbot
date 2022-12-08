import requests
import json
import csv 
import requests
import pandas as pd
from colorama import init, Fore, Back, Style
import time 
import datetime
from urllib.parse import urlparse
import os
import glob
import argparse
import keyboard

# essential for Windows environment
init()
# all available foreground colors
FORES = [ Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE ]
# all available background colors
BACKS = [ Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE ]
# brightness values
BRIGHTNESS = [ Style.DIM, Style.NORMAL, Style.BRIGHT ]

def print_with_color(s, color=Fore.WHITE, brightness=Style.NORMAL, **kwargs):
    print(f"{brightness}{color}{s}{Style.RESET_ALL}", **kwargs)
BASE_URL = "https://www.hatstopdrops.com"
ADD_TO_CART = "/ajax/api/JsonRPC/Commerce/?Commerce/[Checkout::addItemToCart]"
GET_CART = "/ajax/api/JsonRPC/CommerceV2/?CommerceV2/[Cart::read]&cart="
CHECKOUT = "https://www.hatstopdrops.com/ajax/api/JsonRPC/Commerce/?Commerce/[Checkout::getCurrentOrder]"
CHECKEDOUT="https://www.hatstopdrops.com/ajax/api/JsonRPC/Commerce/?Commerce/[Order::checkout]"
VALIDATE="https://www.hatstopdrops.com/ajax/api/JsonRPC/CommerceV2/?CommerceV2/[Cart::validateCart]"

print_with_color('DELAYS ARE PRESET!', Fore.CYAN, Style.BRIGHT)    
keyword = input('ENTER KEYWORDS: ')
print_with_color('KEYWORDS ENTERED!', Fore.GREEN, Style.BRIGHT)
size = input('CHOOSE SIZE 1-12(1 = 6 7/8, 12 = 8 1/4): ')
print_with_color('SIZE ENTERED!', Fore.GREEN, Style.BRIGHT)
quantity = input('PRODUCT QUANTITY (1-9): ')
print_with_color('QUANTITY ENTERED!', Fore.GREEN, Style.BRIGHT)
print('PRESS ENTER TO START!')
while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('ENTER'):  # if key 'q' is pressed 
            print_with_color('TASKS STARTED!', Fore.GREEN, Style.BRIGHT)
            break  # finishing the loop
    except:
        print_with_color('MUST PRESS ENTER!', Fore.RED, Style.BRIGHT)
        break # if user pressed a key other than the given key the loop will break

url = "https://cdn5.editmysite.com/app/store/api/v23/editor/users/125790784/sites/663566500595791167/products"

res=[]
querystring = {
                "page":"1",
                "per_page":"180",
                "sort_by":"shop_all_order",
                "sort_order":"asc",
                "include":"images,media_files,discounts",
                "preferred_item_order_ids":"775,915,807,806,783,782,778,774,760,752,741,720,719,702,688,645",
                "excluded_fulfillment":"dine_in"}


headers = {
                "authority": "cdn5.editmysite.com",
                "accept": "application/json, text/plain, */*",
                "accept-language": "en-US,en;q=0.9",
                "dnt": "1",
                "if-none-match": "W/^\^1ed65ca36c0ca3f11addbf08cceee0ac^^",
                "origin": "https://www.hatstopdrops.com",
                "referer": "https://www.hatstopdrops.com/",
                "sec-ch-ua": "^\^Not?A_Brand^^;v=^\^8^^, ^\^Chromium^^;v=^\^108^^, ^\^Google",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "^\^Windows^^",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "cross-site",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
                        }

r = requests.request("GET", url, headers=headers, params=querystring)

data = r.json()
for p in data['data']:
    res.append(p)
         
df = pd.json_normalize(res)

df.to_csv('stock.csv')
    
csv_file = csv.reader(open('stock.csv', "r", encoding="utf8"), delimiter=",")                         
for row in csv_file:
        product_name = row[8]
while(keyword != product_name):        
    data = r.json()
    for p in data['data']:
        res.append(p)
         
    df = pd.json_normalize(res)

    df.to_csv('stock.csv')
    print_with_color('PRODUCT NOT FOUND!', Fore.RED, Style.BRIGHT)
    time.sleep(1)
        
    if keyword == product_name:
        break; 
    
       
                # input number you want to search
        
    csv_file = csv.reader(open('stock.csv', "r", encoding="utf8"), delimiter=",")

                            
    for row in csv_file:
        product_name = row[8]
        site_link = row[18]
        if keyword == product_name:  
            print_with_color("ITEM FOUND!", Fore.GREEN, Style.BRIGHT),
            size,
            quantity,
                
        
            """add_product_to_cart.

            adding product to //www.hatstopdrops.com cart using site_link

            Parameters
            ----------
            site_link : str
                site_link
            size : int
                size
            quantity : int
                quantity
            """
        
            # send first request as plain html to receive cookies 
            headers = {
                    "accept": "text/html,application/xhtml+xml,application/xml",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62"
                }
            response = requests.get(url, headers=headers)
            

                # prepare adding item to cart using cookie from previous request
                # and get product id from product url
            headers["cookie"] = "; ".join([x.name + "=" + x.value for x in response.cookies])
            headers["content-type"] = "application/json"

            payload = {
                    "id":0,
                    "jsonrpc":"2.0",
                    "method":"Checkout::addItemToCart",
                }

                # since product id is in url we have to extract it like this
            url1 = BASE_URL + "/" + site_link
            path = urlparse(url1).path
            product_id = path.split("/")[3]


            quantity = 1

            payload["params"] = [
                    product_id,
                    size,
                    quantity,
                    {},
                    [],
                    "0.00",
                    {"fulfillment_option":"shipping","store_location_uuid":"","is_no_contact_delivery_enabled":False,"set_primary_order":False,"delivery_address":None,"in_seat_delivery_notes":""},{"source":"0"}]
            
            url = BASE_URL + ADD_TO_CART
            response = requests.post(url, json=payload, headers=headers)
            cart_token = response.json()["result"]["data"]["token"]
            print_with_color("SUCCESSFULLY CARTED {}".format(url1), Fore.GREEN, Style.BRIGHT)

                # fetch cart to confirm product successfully added
            payload = {"id":0,"jsonrpc":"2.0","method":"Cart::read","params":[False]}
            
            url = BASE_URL + GET_CART + cart_token
            response = requests.get(url, json=payload, headers=headers)
            print("SIZE:",(size), "+", "QUANITY:",(quantity))
            print(response.json())
            