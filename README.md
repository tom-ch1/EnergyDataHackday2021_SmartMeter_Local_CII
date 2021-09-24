# EnergyDataHackday2021_SmartMeter_Local_CII

# Infrastructure
## nuc
* hostname: hackday
* ip: 10

* hostname: hackday
* ip address: 10.19.103.106
credentials are not needed!
you can use the commandline client on the nuc: mosquitto_sub (subscribe) or mosquitto_pub (for publishing)
for instance:
mosquitto_sub -h localhost -t "#"
mosquitto_pub -h localhost -t "<your favorite topic>" -m "<your message>" (edited) 


## configuring mosquitto on the nuc
* create a user for mqtt (password: hackday)
```
mosquitto_passwd -c /etc/mosquitto/pwfile hackday
```
* add a listener to /etc/mosquitto/:
```
allow_anonymous true
listener 1883
password_file /etc/mosquitto/pwfile
```
* no credentials are needed, but you can use hackday/hackday if you like
