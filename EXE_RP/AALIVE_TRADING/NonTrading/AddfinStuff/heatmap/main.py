# -*- coding: utf-8 -*-
################################
import os, sys, importlib,glob, csv, subprocess, datetime, shutil, time
from time import sleep, strftime, localtime
from datetime import datetime
titleself = (os.path.basename(__file__)).replace('.pyc','')
print titleself
###########
localtag = '_RP'
sys.path[0:0] = [((os.getcwd().replace('EXE','|')).split('|'))[0] + 'EXE' +localtag]
#########################################
import ENVdicts,rpu_rp 
nd ={}
nd = ENVdicts.ENVdicts(localtag)
for var in nd.keys():
##    print var
    locals()[var] = nd[var]
##################
global timedate_format, nextorderID, date, today,recentlimit, time_format,sym, symbol_list, symdict
moduleNames = ['rpu_rp'] #open(EXE +'importmodlist.txt').readlines()
for module in moduleNames:
    modulestripped = module.strip()
    if modulestripped != titleself:
##        print '...',modulestripped,'xxx',titleself
        my_module = importlib.import_module(modulestripped)
        pass
    else:
        print 'is self'
#####################
import urllib
import libxml2
import csv
import time
from pykml_gen import *
 
#Open csv file
inputfile = csv.reader(open('efacountryweight.csv','rb'),delimiter=',')
firstrow = inputfile.next()
 
# template for URL to grab geocode data
template = "http://maps.googleapis.com/maps/api/geocode/xml?address=%s&sensor=false"
 
weights = []
countries = []
 
hkml = kml_create('EFACountryWeights.kml')
 
for row in inputfile:
    country = row[0]
    print country
    if country != 'Other' and country != '':
        url = template %(country)
        url = url.replace(" ","+")
        time.sleep(0.5)
        stuff = libxml2.parseDoc(urllib.urlopen(url).read())
        lats = [node.content for node in stuff.xpathEval('//lat')]
        lngs = [node.content for node in stuff.xpathEval('//lng')]
        print lats[0]  # Grab first latitude (center of country)
        print lngs[0]  # Grab first longitude (center of country)
        countries.append(country)
        try:
            percent = round(100*float(row[1]),1)
            #print percent
        except:
            percent = 0
        weights.append(percent)
 
        # Create Placemark if weight is greater than 0.1%
        if percent > 0.1:
            #color = 'ffff0000' # Blue
            color = 'ff0000ff' # Red
            size =(percent**0.5)
            description = "Country weight in "+firstrow[0]+" on "+firstrow[1]
            kml_style(hkml, size, country,color)
            kml_placemark(hkml, country, percent, lngs[0], lats[0],description)
 
kml_close(hkml)
