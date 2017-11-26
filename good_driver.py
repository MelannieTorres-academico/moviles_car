import requests
import time

sleep_time=0
token="myToken"
fuel=60
kms=0

payload = {'token': token, 'fuel': fuel, 'kms': kms}
r = requests.post("http://www.sopitas.com/", data=payload)
print(r.status_code)
print('{token:',token,', fuel:',fuel,', kms:',kms, '}')
fuel-=0.0833
kms+=1
time.sleep(sleep_time)

while (r.status_code==200):
    payload = {'token': token, 'fuel': fuel, 'kms': kms}
    r = requests.post("http://www.sopitas.com/", data=payload)
    print(r.status_code)
    print('{token:',token,', fuel:',fuel,', kms:',kms, '}')
    fuel-=0.0833
    kms+=1
    time.sleep(sleep_time)

    if fuel<5:
        fuel+=40

print("Error: url responded with: ",r.status_code)
