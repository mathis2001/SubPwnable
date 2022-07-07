#!/usr/bin/env python3

import requests
import sys
import dns.resolver
import argparse
from prettytable import PrettyTable

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
		sc(args.domain)
		records=Record(args.domain)
		if not records:
			print(bcolors.FAIL+"[!] "+bcolors.RESET+"No record found for "+args.domain)
		else:
			for CNAME in records:
				print(args.domain+bcolors.INFO+' CNAME '+bcolors.RESET+CNAME)

	elif args.list:
		sublist = open(args.list, encoding='utf-8')
		try:
			for sub in sublist:
				sc(sub.strip())
			sublist.close()	
			
			print(bcolors.INFO+"\n[*] "+bcolors.RESET+"CNAME records:\n")

			sublist = open(args.list, encoding='utf-8')
			t=PrettyTable(['Domain','CNAME','Record'])
			for sub in sublist:
				records=Record(sub.strip())
				if not records:
					t.add_row([sub,bcolors.INFO+'CNAME'+bcolors.RESET,bcolors.FAIL+'None'+bcolors.RESET])
					pass
				else:
					for CNAME in records:
						t.add_row([sub,bcolors.INFO+'CNAME'+bcolors.RESET,CNAME])
			print(t)

		except:
			pass


try:
	main()
except Exception as e:
	print(e)
except KeyboardInterrupt:
	print(bcolors.FAIL+"[!] "+bcolors.RESET+"Script canceled.")

