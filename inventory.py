#!/bin/python
from __future__ import print_function
import os
import sys
import pprint

from OPSI.Backend.BackendManager import BackendManager

backend = BackendManager()
clients = backend.host_getObjects(type="OpsiClient")

for client in clients:
  # checking 1
  test_list = ['w10adminvm','admin-pc','adminvm']
  res = [ele for ele in test_list if(ele in client.id)] 
  if res:
    continue
  
  ak =  backend.getHardwareInformation_hash(client.id)
  #print(ak)
  #exit
  # Checking 2
  try:
    seriennummer = (str(ak[u'CHASSIS'][0][u'serialNumber']))
  except:
    seriennummer =  'not available'
    pass

  try:
    modell = (str(ak[u'COMPUTER_SYSTEM'][0][u'model']))
  except:
    modell = 'not available'
    pass

  # network_dict no needed
  network_dict = {}
  print(client.id, end =";")
  print(modell, end =';')
  print(seriennummer, end =';')
  
#  for networkcontroller in ak[u'NETWORK_CONTROLLER']:
  try:
    for networkcontroller in ak[u'NETWORK_CONTROLLER']:
      #print (str(ak[u'NETWORK_CONTROLLER']))
      #exit
      if (len(networkcontroller[u'vendorId'])) == 0:
        continue
      #network_dict = {networkcontroller[u'model'], networkcontroller[u'macAddress']}
      print(networkcontroller[u'model'], end =';')
      print(networkcontroller[u'macAddress'], end =';')
  except:
    print('No NetworkController found', end =';')
    pass
  print('')
