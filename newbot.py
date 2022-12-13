#Imports
import requests
import json
import csv 
import pandas as pd
from colorama import init, Fore, Back, Style
import time 
import datetime
from urllib.parse import urlparse
import os
import glob
import argparse
import keyboard

#print_with_color needs
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
          
#links    
BASE_URL = "https://www.hatstopdrops.com"
ADD_TO_CART = "/ajax/api/JsonRPC/Commerce/?Commerce/[Checkout::addItemToCart]"
GET_CART = "/ajax/api/JsonRPC/CommerceV2/?CommerceV2/[Cart::read]&cart="

#delays/keywords
print_with_color('DELAYS ARE PRESET!', Fore.CYAN, Style.BRIGHT)    
keyword = input('ENTER KEYWORDS: ')
print_with_color('KEYWORDS ENTERED!', Fore.GREEN, Style.BRIGHT)
size = input('CHOOSE SIZE 1-12(1 = 6 7/8, 12 = 8 1/4): ')
print_with_color('SIZE ENTERED!', Fore.GREEN, Style.BRIGHT)
print('PRESS ENTER TO START!')
quantity = 1

#clicking enter to start
while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('ENTER'):  # if key 'q' is pressed 
            print_with_color('TASKS STARTED!', Fore.GREEN, Style.BRIGHT)
            break  # finishing the loop
    except:
        print_with_color('MUST PRESS ENTER!', Fore.RED, Style.BRIGHT)
        break # if user pressed a key other than the given key the loop will break
        
        
url = "https://cdn5.editmysite.com/app/store/api/v23/editor/users/125790784/sites/663566500595791167/products"


querystring = {"page":"1","per_page":"180","sort_by":"shop_all_order","sort_order":"asc","include":"images,media_files,discounts","preferred_item_order_ids":"775,915,807,806,783,782,778,774,760,752,741,720,719,702,688,645","excluded_fulfillment":"dine_in"}


payload = ""

    # Define the headers
headers = {
    "authority": "cdn5.editmysite.com",
    "accept": "application/json, text/plain, */*",
    "accept-language": "en-US,en;q=0.9",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}


   
while True:
    response = requests.request("GET", url, headers=headers, params=querystring)

        
    json_response = response.json()
        
        
    if 'data' in json_response:

        for item in json_response['data']:

               
            link = item['site_link']
            item['name']   
                
            if item['name'] == keyword:
                print_with_color("PRODUCT FOUND!", Fore.GREEN, Style.BRIGHT),
                break;
            
            else:
                print_with_color("PRODUCT NOT FOUND!", Fore.RED, Style.BRIGHT),
                time.sleep(0.35)
                    
            
            
    #carting
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
    url = 'https://www.hatstopdrops.com'
                                
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
    url1 = BASE_URL + "/" +  link
    path = urlparse(url1).path
    product_id = path.split("/")[3]

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
    
    headers = {
            "accept": "text/html,application/xhtml+xml,application/xml",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62"
        }
    
    response = requests.get('https://www.hatstopdrops.com/s/checkout', headers=headers)
    if response.status_code == 200:
        print_with_color("GOING TO CHECKOUT!", Fore.GREEN, Style.BRIGHT)
    else:
        print_with_color("FAILED TO GO TO CHECKOUT!", Fore.RED, Style.BRIGHT)
    
    headers["cookie"] = "; ".join([x.name + "=" + x.value for x in response.cookies])
    headers["content-type"] = "application/json"
    
    #apply phone number
    headers = {
            "accept": "text/html,application/xhtml+xml,application/xml",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62"
        }
    
    payload = {
            "phone":"+12085509662",
            "require_buyer_account":True,
            "site_id":"663566500595791167",
        }
        
    response = requests.post('https://www.hatstopdrops.com/app/accounts/v1/verification?lang=en', json=payload, headers=headers)
    headers["cookie"] = "; ".join([x.name + "=" + x.value for x in response.cookies])
    
    if response.status_code == 200:
        print_with_color("PHONE NUMBER SUCCESSFULLY SUBMITTED!", Fore.GREEN, Style.BRIGHT)
    else:
        print_with_color("FAILED TO SUBMIT PHONE NUMBER!", Fore.RED, Style.BRIGHT)
      
    #checking out as guest
    headers = {
            "accept": "text/html,application/xhtml+xml,application/xml",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62"
        }
    
    payload = {
            "id":0,
            "jsonrpc":"2.0",
            "method":"StoredPayment::checkoutAsGuest",
        }
        
    response = requests.post('https://www.hatstopdrops.com/ajax/api/JsonRPC/CommerceV2/?CommerceV2/[StoredPayment::checkoutAsGuest]', json=payload, headers=headers)
    
    #going to checkout
    headers = {
            "accept": "text/html,application/xhtml+xml,application/xml",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62"
        }
    
    email = 'tristanm10@outlook.com'
    payload = {
            "id":0,
            "jsonrpc":"2.0",
            "method":"Customer::patchEmail",
            "0": email
        }
        
    response = requests.post('https://www.hatstopdrops.com/ajax/api/JsonRPC/CommerceV2/?CommerceV2/[Customer::patchEmail]', json=payload, headers=headers)
    if response.status_code == 200:
        print_with_color("EMAIL SUCCESSFULLY SUBMITTED!", Fore.GREEN, Style.BRIGHT)
    else:
        print_with_color("FAILED TO SUBMIT EMAIL!", Fore.RED, Style.BRIGHT)

    
    
    url = "https://www.hatstopdrops.com/ajax/api/JsonRPC/CommerceV2/?CommerceV2/[Customer::patch]"

    # Set the request headers
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    # Set the request body
    data = {
        "id": 0,
        "jsonrpc": "2.0",
        "method": "Customer::patch",
        "params": [
            {
                "billing_address": {
                    "address_line_1": "1910 Ridge Way",
                    "administrative_district_level_1": "ID",
                    "country": "US",
                    "first_name": "tristan",
                    "last_name": "martinez",
                    "locality": "Middleton",
                    "postal_code": "83644",
                    "phone": {
                        "country_code": "1",
                        "national_number": "2085509662"
                    }
                },
                "shipping_address": {
                    "address_line_1": "1910 Ridge Way",
                    "administrative_district_level_1": "ID",
                    "country": "US",
                    "first_name": "tristan",
                    "last_name": "martinez",
                    "locality": "Middleton",
                    "postal_code": "83644",
                    "phone": {
                        "country_code": "1",
                        "national_number": "2085509662"
                    }
                }
            }
        ]
    }

    # Make the request
    response = requests.patch(url, headers=headers, json=data)
    
    
    # Check the response status code
    if response.status_code == 200:
        print_with_color("INFO SUCCESSFULLY SUBMITTED!", Fore.GREEN, Style.BRIGHT)
    else:
        print_with_color("FAILED TO SUBMIT INFO!", Fore.RED, Style.BRIGHT)
        
    url = "https://www.hatstopdrops.com/ajax/api/JsonRPC/CommerceV2/?CommerceV2/[ShippingRates::refresh]"

    # Set the request headers
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    # Set the request body
    data = {
        "id": 0,
        "jsonrpc": "2.0",
        "method": "ShippingRates::selectRate",
        "params": []
    }

    # Make the request
    response = requests.post(url, headers=headers, json=data)

    # Check the response status code
    if response.status_code == 200:
        print_with_color("REFRESHING SHIPPING RATES!", Fore.GREEN, Style.BRIGHT)
    else:
        print_with_color("FAILED TO REFRESH RATES!", Fore.RED, Style.BRIGHT)    

    url = "https://www.hatstopdrops.com/ajax/api/JsonRPC/CommerceV2/?ShippingRates::selectRate"

    # Set the request headers
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    # Set the request body
    data = {
        "id": 0,
        "jsonrpc": "2.0",
        "method": "ShippingRates::selectRate",
        "params": [
            "72dc3a8f67d995279b8f99392e92c740"
        ]
    }

    # Make the request
    response = requests.post(url, headers=headers, json=data)

    # Check the response status code
    if response.status_code == 200:
        print_with_color("SHIPPING RATE SUCCESSFULLY SUBMITTED!", Fore.GREEN, Style.BRIGHT)
    else:
        print_with_color("FAILED TO SUBMIT SHIPPINGRATE!", Fore.RED, Style.BRIGHT)
                
            
                
                
                
            
            
