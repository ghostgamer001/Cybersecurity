#like gobuster
import requests

#fd= input("Enter wordlist file: ")
f= open("sample.txt", 'r')

for i in f.readlines():
    url="http://192.168.1.1"
    response= requests.get(url)
    print("{} and {}".format(i, response.status_code))

f.close()
