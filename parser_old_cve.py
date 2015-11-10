#!/bin/python3

import argparse
import xml.etree.ElementTree as etree

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='xml database of cve')
    args = parser.parse_args()
    
    cvelist = []
    
    tree = etree.parse(args.filename)
    root = tree.getroot()
    for vuln in root.findall('{http://www.icasi.org/CVRF/schema/vuln/1.1}Vulnerability'):
        CVE = {}
        for e in vuln:
            if "Title" in str(e):
                CVE["title"] = e.text
        cvelist.append(CVE)

    print(cvelist)
