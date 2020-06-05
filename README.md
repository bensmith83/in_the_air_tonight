# in_the_air_tonight
a short but sweet COVID19 Contact Tracing BLE packet detector
## what
COVID19 Contact Tracing implemented by google and apple TODO: add linkz
## why
i want to see them! do analysis, find vulnz.
## where
i'm running on a raspberry pi. should work on any linux box with a BT adapter.
## will work?
i don't know. it matches the spec. i haven't seen one in the wild yet
## how run?
run it. it's really simple right now, just 
`sudo python3 in_the_air_tonight.py`
and output will appear on your screen. pip install bluepy, also.
## how test?
use NRF Connect app to add an advertiser with settings like this:

![NRF Connect](img/nrf_connect_covid19.png)
