# in_the_air_tonight
a short but sweet COVID19 Contact Tracing BLE packet detector
## what
COVID19 Contact Tracing implemented by google and apple
* https://covid19-static.cdn-apple.com/applications/covid19/current/static/contact-tracing/pdf/ExposureNotification-BluetoothSpecificationv1.2.pdf
* https://blog.google/documents/58/Contact_Tracing_-_Bluetooth_Specification_v1.1_RYGZbKW.pdf
### web bluetooth?! web bluetooth.
Check out scan.html for a cheap hack of the google chrome web bluetooth advertisement scan example code. You too can now scan for Contact Tracing packets via a web page.

|![Web Bluetooth Screenshot](img/webbluetooth.png)|
-

## why
i want to see them! do analysis, find vulnz.
## where
i'm running on a raspberry pi. should work on any linux box with a BT adapter.
## will work?
i don't know. it matches the spec. i haven't seen one in the wild yet
![the spec](img/contact_tracing_packet_payload.png)
## how run?

build a whl file for easier install:

sh build.sh 

Then, on each system where you would like to install, just send the .whl file and run:

pip install dist/in_the_air_tonight-1.0.0-py2.py3-none-any.whl

You can then just run the command 'in-the-air-tonight' via command-line. e.g.

root@JWL:~# in-the-air-tonight
 
 [*] scanning for BLE contact tracing packets


## how test?
use NRF Connect app to add an advertiser with settings like this:

![NRF Connect](img/nrf_connect_covid19.png)
