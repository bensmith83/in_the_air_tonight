# -*- coding: utf-8 -*-
from bluepy.btle import Scanner, DefaultDelegate, BTLEManagementError

#Define colors # colors shamelessly borrowed form the dude that wrote the VandyVape vuln
def Red(skk): print("\033[91m {}\033[00m" .format(skk)) 
def Green(skk): print("\033[92m {}\033[00m" .format(skk))
def Yellow(skk): print("\033[93m {}\033[00m" .format(skk)) 

SCAN_TIMEOUT = 10.0

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            #Red("Discovered device: %s, %s" % (dev.addr, dev.rssi))
            pass
        elif isNewData:
            #print("New Data from device: %s, %s" % (dev.addr, dev.rssi))
            pass

def scan_devices():
    scanner = Scanner().withDelegate(ScanDelegate())
    try:
        devices = scanner.scan(SCAN_TIMEOUT)
    except BTLEManagementError:
        print("[WARNING] Permission to use HCI not available. rerun script with sudo or as root")
        return
    for dev in devices:
        for (adtype, desc, value) in dev.getScanData():
            if adtype == 0x03 or adtype == 0x16:
                trace_value = ":".join("{:02x}".format(ord(c)) for c in value)
                #value is stringified and these bytes are reversed at this point
                if value.find("6ffd") == 0 or value.find("6FFD") == 0:
                    if len(value) == 22*2:
                        Green("[+] Discovered Covid19 Contact Tracing Packet from {} ({}) with value: {} and metadata: {}".format(dev.addr, dev.rssi, value[4:-8], value[-8:]))
                    else:
                        Green("[+] Discovered Covid19 nonstandard Contact Tracing Packet from {} ({}) with value: {}".format(dev.addr, dev.rssi, value[4:]))
                    Yellow("[-] Adtype: {:02x}, desc: {}, value: {}".format(adtype, desc, value))

def main():
    Red("[*] scanning for BLE contact tracing packets")
    while(True):
        scan_devices()


