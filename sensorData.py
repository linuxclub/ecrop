#!/usr/bin/env python
import MySQLdb 
db = MySQLdb.connect("localhost", "sensor", "redhat123", "ecrop")
curs=db.cursor()
