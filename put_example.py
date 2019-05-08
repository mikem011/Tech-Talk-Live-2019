#!/usr/bin/env python

import sys, urllib2, base64
import xml.etree.ElementTree as ET

def main():
    jss_endpoint = ''
    request = urllib2.Request(jss_endpoint)
    request.add_header('Authorization', 'Basic ' + base64.b64encode('api_user:jamf1234'))
    request.add_header('Content-Type', 'text/xml')
    request.get_method = lambda: 'PUT'

    # Building XML using ElementTree functions
    PUT_xml = ET.Element('mobile_device')
    general_elem = ET.SubElement(PUT_xml, 'general')
    ET.SubElement(general_elem, 'name').text = 'Test Device 2')

    try:
        response = urllib2.urlopen(request, ET.tostring(PUT_xml))
    except urllib2.URLError, e:
        print(e)

if __name__ == '__main__':
    sys.exit(main())
