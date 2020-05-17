import requests as r

a = open("list.txt").read().split('\n')
b = open("result.txt", "a+")

print("Checking for SPF Record.......")

for domain in a:
    if (domain == ""):
        continue
    headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
            }

    url = "https://www.kitterman.com/spf/getspf2.py"

    values = {
            "serial": "fred12",
            "domain": domain
            }

    p = r.post(url, data=values, headers=headers)

    html = p.text

    print("Checking for ===> "+domain)

    if ("No valid" in html):
        print("SPF not Found For ===> "+domain)
        b.write(domain+'\n')
    else:
        print("SPF Record Are published For: "+domain)

print("Script Finished Thank You")
