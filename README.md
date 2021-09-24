# Interoperability plug-test for smart meter’s local CII
Empower citizens to use their own energy data. Using the smartmeter's local interface for visualisation and automation

See [Challenge.md](Challenge.md)

# Goal
Provide a unified and open API for all types of Smartmeters

# Idea
1. Read different types of smart meter CII (DLMS, IDIS CII, DSMR-P1, MBUS), used by different DSO (EKZ, AEW, EWB, Romande Energie) by means of a hardware metering data adapter and publish the data "as is" to an MQTT Broker
2. design a harmonized MQTT profile that can be used via an open visualization and automation.
3. implement an MQTT client that subscribes to the "raw" Smartmeter topics, translate the messages to the harmonized MQTT profile and publish them to the MQTT Broker.

The customer can thus use the data for further processing, visualisation or automation. As the MQTT topics are standardized, the customer does not need to care about the type of Smartmeter or DSO, it just works!

# Hardware Infrastructure
* here should be a picture of our Smartmeters, adapters, NUC, and Raspberry Pi
* Additionally, a schemaric of the HW setup could be provided

# Component Setup

## Smartmeters and Adapters
### EKZ (Brand / Model)
* type of adapter, configuration, how connected to what?

### AEW (Brand / Model)
* type of adapter, configuration, how connected to what?

### ewb (Brand / Model)
* type of adapter, configuration, how connected to what?

### Romande Energie (Brand / Model)
* type of adapter, configuration, how connected to what?

## [NUC](https://www.intel.com/content/www/us/en/products/details/nuc.html)
* install ubuntu
* hostname: hackday
* ip address: 192.168.1.100
* credentials:
  * hackday / hackday

### configuring mosquitto on the nuc
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

you can use the commandline client on the nuc: mosquitto_sub (subscribe) or mosquitto_pub (for publishing)
for instance:
```
mosquitto_sub -h localhost -t "#"
mosquitto_pub -h localhost -t "<your favorite topic>" -m "<your message>" (edited) 
```
## Raspberry Pi
