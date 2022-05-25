import requests
res = {'value': 'lol', 'next':''}

flag = ''

while(res["value"] != "end"):
    r = requests.get('http://10.10.169.100:3000/{}'.format(res["next"]))
    res = r.json()
    flag += res["value"]
    print(flag)