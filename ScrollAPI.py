#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ES_Scroll.py
#  
#  Copyright 2018 raja <raja@raja-Inspiron-N5110>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import requests,re,string,json


def main(args):
	
	resp=requests.post('http://localhost:9200/netflow-2018.02.20/_search?pretty=true&size=100&scroll=5m')
	#Scroll = re.findall(b'"_scroll_id" : .*"',resp.content)
	resp  =json.loads(resp.content)
	#print (resp)
	sid = resp['_scroll_id']
	print (sid)
	"""
	ScrollID = Scroll[0]
	ScrollID = string.replace(ScrollID,'"_scroll_id" : "', "")
	ScrollID = string.replace(ScrollID,'"', "")
	print (ScrollID)
	if   (sid==ScrollID):
		print ("Hi")
	"""
	while(True): # continue this loop until hits become zero
		headers = {
		'Content-Type': 'application/json',
		}

		data = '\n{\n    "scroll" : "1m", \n    "scroll_id" : "'+sid+'" \n}'

		response = requests.post('http://localhost:9200/_search/scroll', headers=headers, data=data)
		response  =json.loads(response.content)
		print (type(response['hits']['hits']))
		if not (response['hits']['hits']):
			break;
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
