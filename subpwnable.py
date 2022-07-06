#!/usr/bin/env python3

import requests
import sys
import dns.resolver
import argparse

class bcolors:
	OK = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	RESET = '\033[0m'
	INFO = '\033[94m'

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--domain", help="Target a single domain", type=str)
parser.add_argument("-l", "--list", help="Target a list of domains", type=str)
args = parser.parse_args()

def Record(domain):
	list=[]
	try:
		result = dns.resolver.resolve(domain, 'CNAME')
		for record in result:
			CNAME = str(record)
			list.append(CNAME)
			return list
	except:
		print(bcolors.FAIL+"[!] "+bcolors.RESET+"No record found for "+ domain)
		pass

def sc(domain):
	for proto in ["http://","https://"]:
		try:
			url=proto+domain
			rq=requests.get(url)
			status_code=str(rq.status_code)
			if status_code == "404":
				print("["+bcolors.INFO+"Domain Available"+bcolors.RESET+"]"+domain+bcolors.INFO+' ==> '+bcolors.RESET+bcolors.INFO+status_code+bcolors.RESET)
			elif status_code == "302":
				print("["+bcolors.WARNING+"Redirect"+bcolors.RESET+"]"+domain+bcolors.INFO+' ==> '+bcolors.RESET+bcolors.WARNING+status_code+bcolors.RESET)
				req=requests.get(rq.url)
			else:
				print("["+bcolors.FAIL+"Domain Not Available"+bcolors.RESET+"]"+domain+bcolors.INFO+' ==> '+bcolors.RESET+bcolors.FAIL+status_code+bcolors.RESET)
		except:
			pass

def main():
	if args.domain:
		records=Record(args.domain)
		sc(args.domain)
		for CNAME in records:
			print(args.domain+bcolors.INFO+' CNAME '+bcolors.RESET+CNAME)

	elif args.list:
		sublist = open(args.list, encoding='utf-8')
		try:
			for sub in sublist:
				sub=sub.strip()
				sc(sub)
				records=Record(sub)
				if not records:
					pass
				else:
					for CNAME in records:
						print(sub+bcolors.INFO+' CNAME '+bcolors.RESET+CNAME)
		except Exception as e:
			print(e)
			pass

main()


