#!/usr/bin/env python3
#-*- coding: UTF-8 -*-

import sys
import argparse
import base64
import requests

def get_wave(fname):
	with open(fname) as infile:
		file = infile.read()
	return base64.b64encode(file)

def generateModel(args):
	print('Building model %s with options %s : %s'%(args.wakeword, args.gender, args.age))
	wavSample1 = get_wave(args.wakeword+"/0.wav").decode()
	wavSample2 = get_wave(args.wakeword+"/1.wav").decode()
	wavSample3 = get_wave(args.wakeword+"/2.wav").decode()
	wakeModel = args.wakeword + '/' + args.wakeword + ".pmdl"

	data = {
		"name": args.wakeword,
		"language": args.lang,
		"age_group": args.age,
		"gender": args.gender,
		"microphone": "MyCustomMic",
		"token": args.token,
		"voice_samples": [
			{"wave": wavSample1},
			{"wave": wavSample2},
			{"wave": wavSample3}
				]
			}

	response = requests.post(endpoint, json=data)
	if response.ok:
		with open(wakeModel, "w") as outfile:
			outfile.write(response.content)
		print("Saved model to '%s'." %wakeModel)
	else:
		print("Request failed.")
		print(response.text)

if __name__ == "__main__":
	parser = argparse.ArgumentParser(prog='Snowboy Trainer', formatter_class=argparse.RawTextHelpFormatter)
	parser.add_argument('--token', help='Your snowboy.kitt.ai token', type=str, default=None)
	parser.add_argument('--lang', help='Wakeword language (fr, en, de, es ...)', type=str, default='fr')
	parser.add_argument('--gender', help='Male: M or Female: F', type=str, default='M')
	parser.add_argument('--age', help='Age used for training : \n'
															'0 : 0_9 \n'
															'10 : 10_19 \n'
															'20 : 20_29 \n'
															'30 : 30_39 \n'
															'40 : 40_49 \n'
															'50 : 50_59 \n'
															'60 : 60+'
															, type=str, default='3')
	parser.add_argument('--wakeword', help='key/folder for wakeword to train (no special characters)', type=str, default=None)
	args = parser.parse_args()

	if not args.token or not args.wakeword:
		parser.print_help(sys.stderr)
		sys.exit(1)

	generateModel(args)
