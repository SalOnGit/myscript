#!/usr/bin/env python3

import datetime

def do_script ():
	now = datetime.datetime.now()
	return "Hello! {0}".format(now)

if __name__ == "__main__":
	print(do_script())
