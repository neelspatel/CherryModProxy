#!/usr/bin/python

#imports
import os
import re

#import for additions
import scripts, banner, popup

#regex to split:
SPLIT = re.compile ('(?P<head>.*<\s*HEAD[^<]*>)(?P<pre>.*<\s*BODY[^<]*>)(?P<post>.*)', re.IGNORECASE | re.MULTILINE | re.DOTALL)

#the three parts are:
#  1) head - opening html and head tags
#  2) pre  - content of head tag, closing of head tag, opening of body tag
#  3) post - content of body tag, closing of body tag, closing of html tag

#tries to split everything up
def get(arg, host):
	try:
		split = SPLIT.match(arg)
		head = split.group('head')
		pre = split.group('pre')
		post = split.group('post')	

		#print "Head: \033[32m\033[1m" + head + "\033[0m\033[0m\n\n"
		#print "Pre: \033[32m\033[1m" + pre + "\033[0m\033[0m\n\n"
		#print "Post: \033[32m\033[1m" + post + "\033[0m\033[0m\n\n"
		
		print "Inserted"
		#mod.write(head + scripts.get("this")  + pre + banner.get("this") + popup.get(body) + post)
		if "amazon" in host:
			return head + scripts.get(arg) + pre + banner.get(arg) + popup.get(arg) + post
		else:
			return head + scripts.get(arg) + pre + banner.get(arg) + post
	except:
		print "\033[32m\033[1m" + "didn't work" + "\033[0m\033[0m\n\n"
		#print arg
		return arg