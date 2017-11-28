import requests
import time

sleep_time=7
token="93642fb3-0877-469d-9205-0bbc19f33bc5"
fuel=60
kms=0
url="https://us-central1-bus-app-itesm.cloudfunctions.net/updateVehicleInfo"

payload = {'token': token, 'fuel': fuel, 'kilometers': kms}
r = requests.post(url, data=payload)
print(r.status_code)
print('{token:',token,', fuel:',fuel,', kilometers:',kms, '}')
fuel-=0.0833
kms+=1
time.sleep(sleep_time)

while (r.status_code==200):
    payload = {'token': token, 'fuel': fuel, 'kilometers': kms}
    r = requests.post(url, data=payload)
    print(r.status_code)
    print('{token:',token,', fuel:',fuel,', kilometers:',kms, '}')
    fuel-=0.0833
    kms+=1
    time.sleep(sleep_time)

    if fuel<5:
        fuel+=40

print("Error: url responded with: ",r.status_code)
