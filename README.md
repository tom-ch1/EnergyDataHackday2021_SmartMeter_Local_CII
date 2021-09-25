# Interoperability plug-test for smart meter’s local CII
Empower citizens to use their own energy data. Using the smartmeter's local interface for visualisation and automation

See [Challenge.md](Challenge.md)

See also repo smartmeter-datacollector here:
https://github.com/scs/smartmeter-datacollector

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

![Architecture](Architecture.jpeg "Architecture diagram")

## Smartmeters and Adapters
### EKZ (Brand / Model)
* Brand: Landis+Gyr
* Model: [E450](https://www.landisgyr.ch/product/landisgyr-e450/)
* Adapter: [MBUS to USB adapter](https://www.empro.ch/en/products/interfaces/zeta-usb-interfaces/m-bus-slave/)
* Configuration:
  * The MBUS to USB Adapter connects the Smartmeter to a [Raspberry Pi](https://www.raspberrypi.org/
  * On the Raspberry Pi, the [smartmeter-datacollector](https://github.com/scs/smartmeter-datacollector) software retrieve data from the smart meter and publishes them to the mosquitto MQTT Broker that runs on the NUC.

### AEW (Brand / Model)
* Brand: Landis+Gyr
* Model: [E450](https://www.landisgyr.ch/product/landisgyr-e450/)
* Adapter: [MBUS to USB adapter](https://www.empro.ch/en/products/interfaces/zeta-usb-interfaces/m-bus-slave/)
* Configuration:
  * The MBUS to USB Adapter connects the Smartmeter to the NUC
  * On the NUC, the [smartmeter-datacollector](https://github.com/scs/smartmeter-datacollector) software was installed to retrieve data from the smart meter and publishe them to the mosquitto MQTT Broker.

### ewb (Brand / Model)
* Brand: Semax Honeywell Elster
* Model: [AS3000](https://semax.ch/as3000/) mit [AM540 Kommunikationsmodul](https://semax.ch/en/am540/)
* Adapter: gPlug (https://forume.ch/t/kundenschnittstelle-der-intelligenten-messsysteme/938/9)
* Configuration:
  * the gPlug reads the smart meter data and publishes it to an MQTT Broker
  * For that to work, you have to configure the [gPlug's Tasmota Software](https://tasmota.github.io/docs/P1-Smart-Meter/):
    * WLAN to connect to
    * MQTT Broker to connect to

### Romande Energie (Brand / Model)
* Brand: ISKRA
* Model: AM550
* Adapter: gPlug (https://forume.ch/t/kundenschnittstelle-der-intelligenten-messsysteme/938/9)
* Configuration:
  * the gPlug reads the meter data and publishes it to an MQTT Broker
  * For that to work, you have to configure the [gPlug's Tasmota Software](https://tasmota.github.io/docs/P1-Smart-Meter/):
    * WLAN to connect to
    * MQTT Broker to connect to

## [Raspberry Pi](https://www.raspberrypi.org/)
* install the [smartmeter-datacollector image](https://github.com/scs/smartmeter-datacollector/releases)
* Setup MQTT Bridge to transfer the messages to our main MQTT Broker on the NUC

## [gPlug (P1 Smart Meter)](https://tasmota.github.io/docs/P1-Smart-Meter/)
* some assembly required (not shown here)
* plug it into the smart meter P1 port
* connect to the WiFi access point that it makes (SSID: Tasmota....XXXX)
* in the configuration page (that pops up) configure access to your home WiFi
* 'save' and it reboots
* connect to the "new" IP on your home WiFi (http://<whatever>/) to access the Tasmota configuration page
* configure the MQTT host and topic and other Tasmota options
* 'save'

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

# Team
![Team](Team.jpg "Open Energy Data Hackday team")


![Report](018_interoperability-plug-test-for-smart-meter.pdf "Open Energy Data Hackday report")


