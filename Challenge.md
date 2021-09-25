# Interoperability plug-test for smart meter’s local CII
Empower citizens to use their own energy data. Using the smartmeter's local interface for visualisation and automation

See https://hack.opendata.ch/project/783

# Introduction
Smart Meters currently being installed in Switzerland serve mainly to liberalize the electricity market, but they hardly deliver the promised energy savings because they do not yet provide customers with easy access to their data. StromVV §8a defines the characteristics of smart metering systems requiring a local customer interface (CII), which should allow customers to easily access their own consumption data. Unfortunately, these interfaces are not implemented uniformly by the manufacturers and are rolled out by distribution system operators (DSO) in different configurations. This makes it very difficult for the normal customer to get access to his data.

# Motivation
The easy and free access of consumption data is a crucial step in the energy transition and shall help to provide the following contribution
1. give customers transparency about their consumption in real time
1. change customer behavior in a sustainable way to save energy
1. create innovations that help customers to optimize their own consumption with self-generation (PV) and controllable consumers (car charging station, heat pump)

# Idea
Reading of different types of smart meter CII (DLMS, IDIS CII, DSMR-P1, MBUS), used by different DSO (EKZ, AEW, EWB, Romande Energie) by means of a metering data adapter which provides the data to the customer via a harmonized MQTT profile that can be used via an open visualization and automation. The customer can thus view the data at any time and also use it to align his own automation to optimized self-consumption. The MQTT topics should be standardized to provide interoperability between different smart meters and various applications.

# Data
The data from the different meters are sent via MBUS or DSMR to a adapter which converts the data into MQTT. Different meters are provided by the DSO. The MQTT stream is then integrated into OpenHab 3.0 and ioBroker.

# Tasks
* Setup of the metering systems
* Conversion of MBUS-DLMS/COSEM data into MQTT using the open-source library from gurux.fi
* Adaption of the DSMR-P1 Protocol to MQTT
* Documentation of the interoperable MQTT interface
* Integration of the smart meter data into ioBroker and OpenHab

## Previous work at Energy Hack Days 2020:
* [Read your own Smart Meter](https://hack.opendata.ch/project/466)
* [Unleashing the Swiss Smartmeter's CII](https://hack.opendata.ch/project/582)
* [DSMR-P1 Adapter "gPlug" from forumE.ch](https://forume.ch/t/kundenschnittstelle-der-intelligenten-messsysteme/938/9)
