#!/bin/python3

import argparse


CVSS_first_level = {"AV": "Access Vector",
                    "AC": "Access Complexity",
                    "Au": "Authentication",
                    "C": "Confidentiality Impact",
                    "I": "Integrity Impact",
                    "A": "Availability Impact"
}


CVSS_second_level = {"AV":
                     {
                         "L":"Local access",
                         "A":"Adjacent network",
                         "N":"Network"
                     },
                     "AC":
                     {
                         "H":"High",
                         "M":"Medium",
                         "L":"Low"
                     },
                     "Au":
                     {
                         "N":"None",
                         "S":"Requires single instance",
                         "M":"Requires multiple instances"
                     },
                     "C":
                     {
                         "N":"None",
                         "P":"Partial",
                         "C":"Complete"
                     },
                     "I":
                     {
                         "N":"None",
                         "P":"Partial",
                         "C":"Complete"
                     },
                     "A":
                     {
                         "N":"None",
                         "P":"Partial",
                         "C":"Complete"
                     }
}

def parse(s):
    for e in s.split("/"):
        k,v = e.split(":")
        print("%s: %s" % (CVSS_first_level[k], CVSS_second_level[k][v]))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('cvss', help='CVSS to parse')
    args = parser.parse_args()
    parse(args.cvss)

    
