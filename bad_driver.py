import requests
import time

sleep_time=0
token="myToken"
fuel=60
kms=0
i=0

payload = {'token': token, 'fuel': fuel, 'kms': kms}
r = requests.post("http://localhost:8080", data=payload)
print(r.status_code)
print('{token:',token,', fuel:',fuel,', kms:',kms, '}')
fuel-=0.0833
kms+=1
time.sleep(sleep_time)

while (r.status_code==200):
    payload = {'token': token, 'fuel': fuel, 'kms': kms}
    r = requests.post("http://localhost:8080", data=payload)
    print(r.status_code)
    print('{token:',token,', fuel:',fuel,', kms:',kms, '}')

    if i>20 and i<30:
        fuel-=5
    else:
        fuel-=0.0833
        kms+=1

    if fuel<5:
        fuel+=40

    time.sleep(sleep_time)
    i+=1

print("Error: url responded with: ",r.status_code)
