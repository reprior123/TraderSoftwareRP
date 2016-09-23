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

#newfile = heredir + '/fieldsin.csv'
import fileinput

lines = rpu_rp.CsvToLines(newfile)

typelable = 'addfin'
typelable = 'addfin'
typelable2 = 'tx'
typelablenew = 'tx'
modulename ='TransEXT'
mnamelower = modulename.lower()
print '$dictionary[\'' + modulename + '\'] = array( \n\
        \'table\'=>\''+ mnamelower +'\',\n\
        \'audited\'=>true,\n\
                \'duplicate_merge\'=>true,\n\
                \'fields\'=>array (\n\
'
lablearray =[]
for l in lines: 
    if l[0] != 'ggggggg':
        floatprec =''
        prefix = l[2]
        fname = l[1]
        fullname = prefix + '_' + fname
        fulldesc = l[3]
        ftype = fulldesc.split('(')[0]
        if ftype == 'float':
            floatval ='15'
            floatprec = '4'
            flen='19'
            pass
        elif ftype =='varchar':
            flen = '40'
            pass
        elif ftype == 'integer':
            flen ='9'
            pass
        else:
            flen =''
##        floatarea = (fulldesc.split('(')[1])
##        if len(floatarea) > 1 or ftype !='date':
##            if len(floatarea.split('.')) >1 :
##                floatval = floatarea.split('.')[0]
##                floatprec = floatarea.split('.')[1]
##            else:
##                floatval = '1'
##                floatprec = '0'
##        else:
##            floatval = '1'
##            floatprec = '0'            

##        if len(ftype) > 1 :
##            print 'bigger'
##            precision = (fulldesc.split('(')[1]).split('.')[1].replace(')','')
##        else:
##            precision = '1'
##        
        newf = fullname

##        if ftype == 'float':
####            flen = l[2].split('.')[0]
####            precision = l[2].split('.')[1]

        print '\''+newf +'\''+ '=> array('
        print '\'name\' => ' +  '\''+newf +'\','
        print '\'type\' => ' +  '\''+ ftype +'\','
##        size = precision =''
        if ftype == 'float':
            flen = '11'
            size = '20'
            print '\'size\' => ' +  '\''+ size +'\','
            print '\'precision\' => ' +  '\''+ floatprec +'\','
        print '\'vname\' => ' +  '\'LBL_DB_PROD_'+newf.upper() +'\','
        print '\'len\' => ' +  '\''+ flen +'\','


        print '\'required\' => false,'
        print '\'massupdate\' => 0,'
        print '\'comments\' => \'\','
        print '\'importable\' => \'true\','
        print '\'duplicate_merge\' => \'disabled\','
        print '\'audited\' => false,'
        print '\'reportable\' => true,'

        print '),'
        lablearray.append('\'LBL_DB_PROD_'+newf.upper()  +'\''+ ' => \'' + newf.replace('_',' ') +'\',')
        
for  l in lablearray:
    print l
        #print '\'LBL_'+newf.upper()  +'\''+ ' => \'' + newf.replace('_',' ') +'\','
'''
 'lng' =>
  array (
    'required' => true,
    'name' => 'lng',
    'vname' => 'LBL_LNG',
    'type' => 'float',
    'massupdate' => 0,
    'comments' => '',
    'help' => 'Longitude',
    'importable' => 'true',
    'duplicate_merge' => 'disabled',
    'duplicate_merge_dom_value' => '0',
    'audited' => false,
    'reportable' => true,
    'len' => '11',
    'size' => '20',
    'precision' => '8',

    'required' => false,
    'name' => 'document_id_c',
    'vname' => '',
    'type' => 'id',
    'massupdate' => 0,
    'no_default' => false,
    'comments' => '',
    'help' => '',
    'importable' => 'true',
    'duplicate_merge' => 'disabled',
    'duplicate_merge_dom_value' => 0,
    'audited' => false,
    'reportable' => false,
    'unified_search' => false,
    'merge_filter' => 'disabled',
'''
