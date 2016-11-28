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
heredir = os.getcwd()
print heredir
newfile = downloads +'suitecrm modulebuilder TransEXT - Sheet5.csv'
newfile = downloads + 'Untitled spreadsheet - Sheet1 (1).csv' #'fields list WIP new Suitecrm - DB_productsRolotec.csv'
newfile = downloads + 'temp' #'fields list WIP new Suitecrm - DB_productsRolotec.csv'
newfile = downloads +  'fields list WIP new Suitecrm - Organizations.csv'


#newfile = heredir + '/fieldsin.csv'
import fileinput
newfile = 'newfields.txt'

lines = rpu_rp.CsvToLines(newfile)

typelable = 'addfin'
typelable = 'addfin'
typelable2 = 'tx'
typelablenew = 'tx'
modulename ='TransEXT'
modulename ='Organizations'
mnamelower = modulename.lower()
print '$dictionary[\'' + modulename + '\'] = array( \n\
        \'table\'=>\''+ mnamelower +'\',\n\
        \'audited\'=>true,\n\
                \'duplicate_merge\'=>true,\n\
                \'fields\'=>array (\n\
'
lablearray =[]
for l in lines:
##    print l
    if l[0] != 'ggggggg':
        floatprec =''
        prefix = '' #'org' # l[1] #l[2]
        fname = l[0].lower()#l[1]
        fullname = prefix + '_' + fname
        fullname = prefix + '' + fname
        fulldesc = 'bla'#l[3]
        ftype = prefix #'decimal' # fulldesc.split('(')[0]
        if prefix =='price':
            ftype = 'decimal'
            pass
        else:
            ftype = 'varchar'
##        print ftype
        newf = fullname
        dropdownname = 'language_list'
        defaultval = 'English'
        labelprefix = 'LBL_'
        print '\''+newf +'\''+ ' => array('
        print '\'name\' => ' +  '\''+newf +'\','
        print '\'vname\' => ' +  '\''+labelprefix+newf.upper() +'\','
        print '\'type\' => ' +  '\''+ ftype +'\','
        if ftype == 'decimal':
            floatval ='15'
            floatprec = '3'
            flen = '14'
            print '\'precision\' => ' +  '\''+ floatprec +'\','         
            print '\'len\' => ' +  '\''+ flen +'\','
        elif ftype =='varchar':
            flen = '40'
            print '\'len\' => ' +  '\''+ flen +'\','
        elif ftype == 'datetime':
            pass
        elif ftype == 'enum':
            flen ='66'
            print '\'len\' => ' +  '\''+ flen +'\','
            print '\'options\' => \'' + dropdownname + '\','
            print '\'default\' => \'' + defaultval + '\','
            pass
        else:
            flen =''
        print '),'
        lablearray.append('\''+labelprefix + newf.upper()  +'\''+ ' => \'' + newf.replace('_',' ') +'\',')

for  l in lablearray:
    print l
        #print '\'LBL_'+newf.upper()  +'\''+ ' => \'' + newf.replace('_',' ') +'\','
    ########################
    
print rpu_rp.catstring('simplefield.vardeftpl.txt')
