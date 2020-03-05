#!/bin/python
from __future__ import print_function
import os
import sys
import pprint

from OPSI.Backend.BackendManager import BackendManager

backend = BackendManager()
clients = backend.host_getObjects(type="OpsiClient")

for client in clients:
  ak =  backend.getHardwareInformation_hash(client.id)
  seriennummer =  str(ak[u'COMPUTER_SYSTEM'][0][u'serialNumber'])
  modell = str(ak[u'COMPUTER_SYSTEM'][0][u'model'])
  pcname = str(ak[u'COMPUTER_SYSTEM'][0][u'name'])
  # network_dict no needed
  network_dict = {}
  print(pcname, end =";")
  print(modell, end =';')
  print(seriennummer, end =';')
  for networkcontroller in ak[u'NETWORK_CONTROLLER']:
    if (len(networkcontroller[u'vendorId'])) == 0:
      continue
    network_dict = {networkcontroller[u'model'], networkcontroller[u'macAddress']}
    print(networkcontroller[u'model'], end =';')
    print(networkcontroller[u'macAddress'], end =';')
  print('')
