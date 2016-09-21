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
newfile = heredir + '/fieldsin.csv'
import fileinput

lines = rpu_rp.CsvToLines(newfile)

typelable = 'addfin'
typelable = 'addfin'
typelablenew = 'tx'
modulename ='TransEXT'
mnamelower = modulename.lower()
print '$dictionary[\'' + modulename + '\'] = array( \n\
        \'table\'=>\''+ mnamelower +'\',\n\
        \'audited\'=>true,\n\
                \'duplicate_merge\'=>true,\n\
                \'fields\'=>array (\n\
'
for l in lines: 
    if l[1] != typelable:
        newf = typelablenew +'_'+l[0]
        ftype = l[1]
        flen = l[2]
        if ftype == 'float':
            flen = l[2].split('.')[0]
            precision = l[2].split('.')[1]

        print '\''+newf +'\''+ '=> array('
        print '\'name\' => ' +  '\''+newf +'\','
        print '\'type\' => ' +  '\''+ ftype +'\','
##        size = precision =''
        if ftype == 'float':
            flen = '11'
            size = '20'
            print '\'size\' => ' +  '\''+ size +'\','
            print '\'precision\' => ' +  '\''+ precision +'\','
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

for l in lines:
    if l[1] != typelable:
        newf = typelablenew + '_'+l[0]
        print '\'LBL_DB_PROD_'+newf.upper()  +'\''+ ' => \'' + newf.replace('_',' ') +'\','
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
