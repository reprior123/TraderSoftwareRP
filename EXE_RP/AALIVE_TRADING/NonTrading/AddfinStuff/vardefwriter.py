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
#############################
global  sym, symbol_list, symdict
########################################
import fileinput

lines = rpu_rp.CsvToLines('vardefsin.csv')

typelable = 'addfin'
typelablenew = 'rolo'
for l in lines:
    if l[1] == typelable:
        newf = typelablenew +'_'+l[0]
        print '\''+newf +'\''+ '=> array('
        print '\'name\' => ' +  '\''+newf +'\','
        print '\'type\' => ' +  '\''+'varchar' +'\','
        print '\'vname\' => ' +  '\'LBL_DB_PROD_'+newf.upper() +'\','
        print '\'len\' => ' +  '\''+'35' +'\','
        print '),'

for l in lines:
    if l[1] == typelable:
        newf = typelablenew + '_'+l[0]
        print '\'LBL_DB_PROD_'+newf.upper()  +'\''+ ' => \'' + newf.replace('_',' ') +'\','
        #print '\'LBL_'+newf.upper()  +'\''+ ' => \'' + newf.replace('_',' ') +'\','
