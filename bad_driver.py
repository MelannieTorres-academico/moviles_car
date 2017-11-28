import requests
import time

sleep_time=7
token="d168ccba-5a8d-40c5-a517-54d645a238e2"
fuel=60
kms=0
i=0
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
