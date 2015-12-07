#!/bin/python3

import argparse


CVSS_first_level = {"AV": ("Access Vector", "This vulnerability can be accessed via %s."),
                    "AC": ("Access Complexity", "The complexity of exploiting this vulnerability is %s."),
                    "Au": ("Authentication", "This vulnerability %s authentification to be exploited."),
                    "C": ("Confidentiality Impact", "This vulnerability lead to %s confidentiality impact."),
                    "I": ("Integrity Impact", "This vulnerability lead to %s integrity impact."),
                    "A": ("Availability Impact", "This vulnerability lead to %s availability impact.")
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
                         "N":"Requires no",
                         "S":"Requires single instance",
                         "M":"Requires multiple instances"
                     },
                     "C":
                     {
                         "N":"No",
                         "P":"Partial",
                         "C":"Complete"
                     },
                     "I":
                     {
                         "N":"No",
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
        print("%s:" % CVSS_first_level[k][0])
        print(CVSS_first_level[k][1] % CVSS_second_level[k][v].lower())
        print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('cvss', help='CVSS to parse')
    args = parser.parse_args()
    parse(args.cvss)

    
