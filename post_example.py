#!/usr/bin/env python

import sys, urllib2, base64
import xml.etree.ElementTree as ET

def main():
    jss_endpoint = ''
    request = urllib2.Request(jss_endpoint)
    request.add_header('Authorization', 'Basic ' + base64.b64encode('api_user:jamf1234'))
    request.add_header('Content-Type', 'text/xml')
    request.get_method = lambda: 'POST'

    # Using XML string
    POST_xml = '''<mobile_device>
                    <general>
                        <name>Test Device 1</name>
                        <wifi_mac_address>ab:cd:ef:12:34:56</wifi_mac_address>
                        <serial_number>SN123456789</serial_number>
                        <asset_tag>00001</asset_tag>
                    </general>
                </mobile_device>'''

    # Building XML using ElementTree functions
    #POST_xml = ET.Element('mobile_device')
    #general_elem = ET.SubElement(POST_xml, 'general')
    #ET.SubElement(general_elem, 'name').text = 'Test Device 1')
    #ET.SubElement(general_elem, 'mac_address').text = 'ab:cd:ef:12:34:56')
    #ET.SubElement(general_elem, 'serial_number').text = 'SN123456789')
    #ET.SubElement(general_elem, 'asset_tag').text = '00001')

    try:
        response = urllib2.urlopen(request, POST_xml)
        #response = urllib2.urlopen(request, ET.tostring(POST_xml))
    except urllib2.URLError, e:
        print(e)

if __name__ == '__main__':
    sys.exit(main())
