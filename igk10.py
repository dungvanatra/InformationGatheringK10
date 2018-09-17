#!/usr/bin/env python

from termcolor import colored
import requests
import  os
import  sys
import re


def banner():
		print(colored("""
    	*   **         *      	* *	  * * *
	*   *          *       *  *     *       *
	*   *          *     *    *     *       *
	*   *          *   *      *     *       *
	*   *          * *        *     *       *  1.0
	*   *   * * *  * *        *     *       * 
	*   *     *    *   *      *     *       *
  	*   * * * *    *     *    *       * * *
		Information Gathering Tool
	""", "red"))
def author():
	print(colored("Author: DuQuocDung-PhanThanhTruoc\n", "blue"))


def menu():
	print ("-"*80)
	print (colored("1. Whois Lookup\t\t\t\t11. Reserve IP Lookup", "green"))
	print (colored("2. DNS Lookup\t\t\t\t12. Subnet Lookup", "green"))
	print (colored("3. Zone Transfer + Cloudflare\t\t13. Robots.txt", "green"))
	print (colored("4. Port Scanner\t\t\t\t14. Comments", "green"))
	print (colored("5. Http Headers\t\t\t\t15. Meta Tag", "green"))
	print (colored("6. GeoIP Lookup", "green"))
	print (colored("7. Page Links", "green"))
	print (colored("8. Host Finder", "green"))
	print (colored("9. Find Shared DNS", "green"))
	print (colored("10. Host DNS Finder", "green"))
	print (colored("0. Quit", "green"))
	print ("-"*80)
	try:
		return int(raw_input("Choosen:"))
	except ValueError:
		print(colored("Enter wrong!", "red"))

def comments(url):
	r = requests.get(url)
	print (colored(url, "yellow"))
	raw_input(colored("continue!!!", "red"))
	comment =  re.findall("<!--(.*)-->", r.text)
	for c in comment:
		print (colored(c, "green"))

def metas(url):
	r = requests.get(url)
	print (colored(url, "yellow"))
	raw_input(colored("continue!!!", "red"))
	comment =  re.findall("<meta(.*)>", r.text)
	for c in comment:
		print (colored(c, "green"))

def main():
	while True:
		os.system("clear")
		banner()
		author()
		index = menu()
		if index == 1:
			domain = raw_input("Enter domain/ip:")
			url = "http://api.hackertarget.com/whois/?q=" + domain
			r = requests.get(url)
			print (colored(r.text, "yellow"))
		elif index == 2:
			domain = raw_input("Enter domain/ip:")
			url = "http://api.hackertarget.com/dnslookup/?q=" + domain
			r = requests.get(url)
			print (colored(r.text, "yellow"))
		elif index == 3:
			domain = raw_input("Enter domain/ip:")
			url = "http://api.hackertarget.com/zonetransfer/?q=" + domain
			r = requests.get(url)
			print (colored(r.text, "yellow"))
			if "cloudflare" in r.text:
				print (colored("Cloudflare Detected", "yellow"))
			else:
				print (colored("Cloudflare not Detected", "yellow"))
		elif index == 4:
			domain = raw_input("Enter domain/ip:")
			url = "http://api.hackertarget.com/nmap/?q=" + domain
			r = requests.get(url)
			print (colored(r.text, "yellow"))
		elif index == 5:
			domain = raw_input("Enter domain/ip:")
			url = "http://api.hackertarget.com/httpheaders/?q=" + domain
			r = requests.get(url)
			print  (colored(r.text, "yellow"))
		elif index == 6:
			domain = raw_input("Enter domain/ip:")
			url = "https://api.hackertarget.com/geoip/?q=" + domain
			r = requests.get(url)
			print  (colored(r.text, "yellow"))
		elif index == 7:
			domain = raw_input("Enter domain/ip:")
			url = "https://api.hackertarget.com/pagelinks/?q=" + domain
			r = requests.get(url)
			os.system("rm -rf urls")
			text  = r.text.split("\n")
			f = open("urls", "w")
			for t in text:
				print (colored(t, "yellow"))
				f.write(t + "\n")

		elif index == 8:
			domain = raw_input("Enter domain/ip:")
			url = "https://api.hackertarget.com/hostsearch/?q=" + domain
			r = requests.get(url)
			print (colored(r.text, "yellow"))
		elif index == 9:
			domain = raw_input("Enter domain/ip:")
			url = "https://api.hackertarget.com/findshareddns/?q=" + domain
			r = requests.get(url)
			print (colored(r.text, "yellow"))
		elif index == 10:
			domain = raw_input("Enter domain/ip:")
			url = "https://api.hackertarget.com/mtr/?q=" + domain
			r = requests.get(url)
			print (colored(r.text, "yellow"))
		elif index == 11:
			domain = raw_input("Enter domain/ip:")
			url = "https://api.hackertarget.com/reverseiplookup/?q=" + domain
			r = requests.get(url)
			print (colored(r.text, "yellow"))
		elif index == 12:
			domain = raw_input("Enter domain/ip:")
			url = "http://api.hackertarget.com/subnetcalc/?q=" + domain
			r = requests.get(url)
			print (colored(r.text, "yellow"))
		elif index == 13:
			try:
					domain = raw_input("Enter domain/ip:")
					url = "http://" + domain + "/robots.txt"
					print (colored(url, "blue"))
					r = requests.get(url)
					print (colored(r.text, "yellow"))
			except:
					print (colored("Failed!", "yellow"))
		elif index == 14:
			domain = raw_input("Enter domain/ip:")
			file = raw_input("Enter file name:")
			f = open(file, "r")
			urls = f.readlines()
			for u in urls:
				if domain in u:
					comments(u)
		elif index == 15:
			domain = raw_input("Enter domain/ip:")
			file = raw_input("Enter file name:")
			f = open(file, "r")
			urls = f.readlines()
			for u in urls:
				if domain in u:
					metas(u)	

		elif index == 0:
			print (colored("Have fun, thank you for using", "red"))	
			sys.exit()
		raw_input(colored("Press a key any to continue!", "red"))

if __name__ == '__main__':
	main()