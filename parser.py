import feedparser
import datetime
from sqlalchemy import create_engine, exc, insert
from Table import *

f = feedparser.parse('https://nvd.nist.gov/download/nvd-rss.xml')


class CVE(object):
    """CVE basic object"""
    
    def __init__(self, rss_entry):
        self.date = ""
        self.cveid = ""
        self.parse(rss_entry)

    def parse(self, entry):
        self.date = ""
        try:
            self.date = datetime.datetime.strptime(entry["updated"],"%Y-%m-%dT%H:%M:%SZ")
        except ValueError as e:
            print("invalid date:", e)

        self.cveid = entry["title"].split(" ")[0]


    def __repr__(self):
        return "%s: %s" % (str(self.date), self.cveid)
    
class BDD(object):
    """bdd object that will use SQLalchemy"""

    def __init__(self):
        pass

    def connect(self):
        try:
            engine = create_engine('mysql+pymysql://root:toor@localhost/vigilate')
        except exc.OperationalError as err2:
            exit("Can't create database : mysql %s" % err2)

    def add(self, cve):
        vulns = Vulns()
        insert(vulns.vulns).values(cveid=cve.cveid, date=cve.date)

    
if __name__ == "__main__":

    bdd = BDD()
    bdd.connect()

    c = CVE()
    for v in f["entries"]:
        c = CVE(v)
        print(c)
        bdd.add(c)
    
    

