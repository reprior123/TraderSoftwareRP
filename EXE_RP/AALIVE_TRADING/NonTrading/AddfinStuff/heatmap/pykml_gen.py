######### -*- coding: utf-8 -*-
########################################
########import os, sys, importlib,glob, csv, subprocess, datetime, shutil, time
########from time import sleep, strftime, localtime
########from datetime import datetime
########titleself = (os.path.basename(__file__)).replace('.pyc','')
########print titleself
###################
########localtag = '_RP'
########sys.path[0:0] = [((os.getcwd().replace('EXE','|')).split('|'))[0] + 'EXE' +localtag]
#################################################
########import ENVdicts,rpu_rp 
########nd ={}
########nd = ENVdicts.ENVdicts(localtag)
########for var in nd.keys():
##########    print var
########    locals()[var] = nd[var]
##########################
########global timedate_format, nextorderID, date, today,recentlimit, time_format,sym, symbol_list, symdict
########moduleNames = ['rpu_rp'] #open(EXE +'importmodlist.txt').readlines()
########for module in moduleNames:
########    modulestripped = module.strip()
########    if modulestripped != titleself:
##########        print '...',modulestripped,'xxx',titleself
########        my_module = importlib.import_module(modulestripped)
########        pass
########    else:
########        print 'is self'
#############################
from __future__ import print_function
 
def kml_create(fname):
    hkml = open(fname, 'w')
    print("""<kml xmlns=\"http://www.opengis.net/kml/2.2\">
    <Document> """,file=hkml)
    return hkml
 
def kml_folder_start(hkml,folder):
    print("""<Folder>
    <name>"""+folder+"""</name>""", file=hkml)
 
def kml_folder_stop(hkml):
    print("""</Folder>""", file=hkml)
 
def kml_close(hkml):
    print("""</Document>
</kml>""", file=hkml)
    hkml.close()
 
def kml_style(hkml,size,name,color):
    print("""<Style id="sn_target_"""+name+"""">
        <IconStyle>
            <color>"""+color+"""</color>
            <scale>"""+str(size)+"""</scale>
            <Icon>
                <href>http://maps.google.com/mapfiles/kml/shapes/shaded_dot.png</href>
            </Icon>
        </IconStyle>
        <LabelStyle>
            <scale>1.0</scale>
        </LabelStyle>
        <ListStyle>
        </ListStyle>
    </Style>""", file=hkml)
 
def kml_placemark(hkml, name, percent, lon, lat, desc = 'Portfolio Weights'):
    print("""<Placemark>
        <name>"""+name,str(percent)+"%"+"""</name>
        <styleUrl>#sn_target_"""+name+"""</styleUrl>
                <description>
                 <![CDATA[
                 <p>"""+name,str(percent)+"%"+"""</p>
                 <p>"""+desc+"""</p>
                 ]]>
                </description>
        <Point>
            <coordinates>"""+lon+""","""+lat+"""</coordinates>
        </Point>
    </Placemark>""", file=hkml)
