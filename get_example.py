#!/usr/bin/env python

import sys, urllib2, base64
import xml.etree.ElementTree as ET

def main():
    jss_endpoint = ''
    request = urllib2.Request(jss_endpoint)
    request.add_header('Authorization', 'Basic ' + base64.b64encode('api_user:jamf1234'))
    request.add_header('Content-Type', 'text/xml')

    try:
        response = urllib2.urlopen(request, ET.tostring(POST_xml))
    except urllib2.URLError, e:
        print(e)
    # Print entire XML
    device_xml = ET.fromstring(response.read())
    print ET.tostring(device_xml)
    # Print specitic attribute
    #device_xml = ET.fromstring(response.read())
    #print device_xml.find('general/name').text
    # Print multiple attribute values
    #device_xml = ET.fromstring(response.read())
    #groups = device_xml.findall('mobile_device_groups/mobile_device_group')
    #for group in groups:
        #print group.find('name').text

if __name__ == '__main__':
    sys.exit(main())
