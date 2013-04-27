import re

def get(arg):

	try:
		result = arg[(arg.index("<h1>"))+4:]
		result = result[:(result.index("</h1>"))]

		return result
	except:
		return ""