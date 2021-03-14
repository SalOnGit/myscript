#!/usr/bin/env python3

import datetime
import os

def do_script ():
	now = datetime.datetime.now()
	return "Hello! {0}".format(now)

def application(env, start_response):
	strt_response('200 OK', [{'Content-Type','text/html'}])
	return[do_script()]

if __name__ == "__main__":
	if 'REQUEST_URI' in os.environ:
		print("Contetn-type: text/html\n\n")
	print(do_script())
