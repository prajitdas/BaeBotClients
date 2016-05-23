'''
Created on May 21,2016
@author: Prajit Kumar Das
Usage: python configureKikBot.py username api_key
'''
import json
import requests
import logging
import sys
import time
from pprint import pprint
logging.basicConfig(filename='kikBot.log',level=logging.DEBUG)

def doTask(username,api_key):
	resultDict = requests.post(
				  'https://api.kik.com/v1/config',
				  auth=(username,api_key),
				  headers={
				  'Content-Type': 'application/json'
				  },
				  data=json.dumps({
								  "webhook": "https://8831000c.ngrok.io/umbcbae/kik_webhook/1234",
								  "features": {
								  "manuallySendReadReceipts": False,
								  "receiveReadReceipts": False,
								  "receiveDeliveryReceipts": False,
								  "receiveIsTyping": False
								  }
								  })
				  ).json()
	pprint(resultDict)
	logging.debug('At '+str(time.time())+' got response: '+json.dumps(resultDict))

def main(argv):
	if len(sys.argv) != 3:
		sys.stderr.write('Usage: python getKikBotConfiguration.py username api_key\n')
		sys.exit(1)
	
	username = sys.argv[1]
	api_key = sys.argv[2]
		
	startTime = time.time()
	doTask(username,api_key)
	executionTime = str((time.time()-startTime)*1000)
	logging.debug('Execution time was: '+executionTime+' ms')

if __name__ == "__main__":
	sys.exit(main(sys.argv))
