#!/bin/python3
import requests
from platform import system
import os
from multiprocessing.dummy import Pool as ThreadPool
def twohundred():
	print('000000000000000000000000000000000000000000000000000000000')
	print('0000 These Directories Or Files Hava 200 Status_code 0000')
	print('000000000000000000000000000000000000000000000000000000000')
def other():
	print('00000000000000000000000000000000000000000000000000000000000')
	print('0000 These Directories Or Files Have Other Status_code 0000')
	print('00000000000000000000000000000000000000000000000000000000000')
def cleanscreen():
	if system() == 'Linux':
		os.system('clear')
	elif system() == 'Windows':
		os.system('cls')
def dirlist():
	path = input('Enter Your File Path :::: > ')
	dirs = []
	dirslist = open(path)
	for i in dirslist:
		i = i.splitlines()
		dirs.append(i[0])
	return dirs
def link():
	fullurl = []
	url = input('Enter Your Url :::: > ')
	for path in dirlist():
		lol = url+'/' + path
		fullurl.append(lol)
	return fullurl
status200 = []
otherstatus = []
def checkdir(urls):			
	try:
		req = requests.get(urls)
		print(urls + ' (' + str(req.status_code) +')')
		if req.status_code != 404:
			if req.status_code == 200:
				status200.append(urls + ' (' + str(req.status_code) +')')
			else:
				otherstatus.append(urls + ' (' + str(req.status_code) +')')
	except:
		pass
def main():
	try:
		global other
		cleanscreen()
		dictory = link()
		pool = ThreadPool(100)
		pool.map(checkdir , dictory)
		pool.close()
		pool.join()
		cleanscreen()
		twohundred()
		for two in status200:
			print(two)
		other()
		for other in otherstatus:
			print(other)
	except KeyboardInterrupt:
		print("KeyboardInterrupt")

if __name__ == '__main__':
	main()