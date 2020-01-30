#!/usr/bin/env python3
#-*- coding: UTF-8 -*-

import sys, os
import argparse
import time
import json
import urllib

import urllib.request
requestUrl = urllib.request
parseUrl = urllib.parse
from http.cookiejar import CookieJar, LWPCookieJar

try:
	reload(sys)
	sys.setdefaultencoding('utf-8')
except:
	pass

class rhasspyBatcher():
	def __init__(self, params):
		self._version = 0.5

		self.debugLevel = params.debug if params.debug > 0 else False

		self.debug(3, '--addr: %s'%params.addr)
		self.debug(3, '--port: %s'%params.port)
		self.debug(3, '--json: %s'%params.json)
		self.debug(3, '--sentence: %s'%params.sentence)
		self.debug(3, '--intent: %s'%params.intent)
		self.debug(3, '--debug: %s'%params.debug)

		self.addr = params.addr
		self.port = params.port

		self._urlHost = self.addr+':'+self.port
		self._reqHdl = None

		self.matched = 0
		self.unmatched = 0
		self.tested = 0

		self.connected = False
		if self.connect() == True:
			self.debug(1, "__Rhasspy connected__")
			self.connected = True
			if (params.json != ''):
				self.testJsonFile(params.json)
			if (params.sentence != ''):
				self.testSentence(params.sentence, params.intent)
	#
	def connect(self):
		answer = self.request('GET', self._urlHost, '/api/version')
		self.debug(1, 'answer connect: %s'%answer)
		if answer[0] == 200 : return True
		return False
	#
	def testJsonFile(self, jsonPath, showResult=True):
		if not os.path.exists(jsonPath):
			return False

		try:
			batchJson = json.load(open(jsonPath, 'rb'), encoding='utf-8')
			for query in batchJson:
				self.debug(3, 'batch test: %s | %s'%(query, batchJson[query]))
				try:
					result = self.testQuery(query)
					self.showResult(result, batchJson[query], query)
				except Exception as e:
					print('Batch test ERROR: ', e)
					break
				time.sleep(0.3)
		except:
			return False

		if showResult:
			self.showTotalResult()
	#
	def testSentence(self, query, matchIntent=''):
		result = self.testQuery(query)
		self.showResult(result, matchIntent, query)
		time.sleep(0.3)
	#


	def testQuery(self, inputQuery):
		inputQuery = inputQuery.lower()
		answer = self.request('POST', self._urlHost, '/api/text-to-intent?nohass=true', inputQuery)
		self.debug(6, "testQuery:answer %s"%answer)
		return answer
	#
	def showResult(self, nluInference, matchIntent='', query='', showOnlyUnmatched=False):
		self.tested += 1
		displayResult = ''
		showThis = True

		intentInput = nluInference
		intent = intentInput['intent']
		confidence = intent['confidence']
		intentName = intent['name']

		entities = nluInference['entities']
		slots = nluInference['slots']

		#no intent found:
		if intentName == '':
			displayResult = '[UNFOUND     ]'
			self.unmatched += 1
			if matchIntent:
				displayResult += ' should match: %s | query: %s'%(matchIntent, query)
			print(displayResult)
			return False

		if matchIntent != '':
			if matchIntent == intentName:
				if showOnlyUnmatched: showThis = False
				self.matched += 1
				displayResult += '[     MATCHED] %s | query: %s'%(matchIntent, query)
			else:
				self.unmatched += 1
				displayResult += '[---UNMATCHED] %s should: %s | query: %s'%(intentName, matchIntent, query)
		else:
			displayResult += '[       FOUND] %s | query: %s'%(intentName, query)

		displayResult += ' | confidence:%s'%round(confidence, 2)

		if showThis:
			displaySlotResult = ''
			for slot in slots:
				slotName = slot
				slotValue = slots[slot]
				displaySlotResult += ' | %s : %s'%(slotName, slotValue)
			if len(slots) == 0:
				displaySlotResult = 'No slot found'
			displayResult += ' | Slots: %s'%displaySlotResult
			print(displayResult)
	#
	def showTotalResult(self):
		print('matched: %s | unmatched: %s | total: %s'%(self.matched, self.unmatched, self.tested))
	#
	def request(self, method, host, path='', jsonString=None, postinfo=None): #standard function handling all get/post request
		if self._reqHdl == None:
			self._reqHdl = requestUrl.build_opener()
			self._reqHdl.addheaders = [
						('User-agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:51.0) Gecko/20100101 Firefox/51.0'),
						('Connection', 'keep-alive'),
						('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'),
						('Upgrade-Insecure-Requests', 1)
					]

		url = host+path
		self.debug(5, 'request: %s method: %s postinfo: %s'%(url, method, postinfo))

		if method == 'GET':
			try:
				answer = self._reqHdl.open(url, timeout = 3)
			except:
				return ["404", None]
		else:
			if jsonString != None:
				jsonBytes = jsonString.encode()
				req = urllib.request.Request(url, data=jsonBytes, headers={'Content-Type': 'application/json'})
				answer = self._reqHdl.open(req)

			if postinfo != None:
				data = parseUrl.urlencode(postinfo)
				data.encode()
				answer = self._reqHdl.open(url, data, timeout = 5)

		if jsonString != None:
			self.debug(5, 'request info: %s'%answer.info())
			result = json.load(answer)
			return result

		return [answer.getcode(), answer.read()]
	#
	def debug(self, level, text):
		if self.debugLevel >= level:
			print("--debug:", text)
	#
	#
#

if __name__ == "__main__":
	parser = argparse.ArgumentParser(prog='Rhasspy Batch Tester')

	parser.add_argument('--addr', help='http://IP adress of Rhasspy', type=str)
	parser.add_argument('--port', help='Port of Rhasspy', type=str, default='12101')
	parser.add_argument('--json', help='json file path (see documentation)', type=str, default='')
	parser.add_argument('--sentence', help='A sentence to test', type=str, default='')
	parser.add_argument('--intent', help='The intent Name that should match --sentence', type=str, default='')
	parser.add_argument('--debug', help='debug level', type=int, default=0)
	args = parser.parse_args()

	rhasspy = rhasspyBatcher(args)
