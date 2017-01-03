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
newfile = downloads +  'newfile.csv'
#################
'''
calculations for the following:
timeband = inception_end - enception_start
number of busdays for timeband
timeband2 = dur_enddate - dur_startdate
'''

def makecheckf(fname):
    print ' '
    print 'protected function _' + fname +'check(){'
    print '     return (bool) $this->bean->checkf_pep_check;'
    print     '}'

    
#newfile = heredir + '/fieldsin.csv'
import fileinput
lines = rpu_rp.CsvToLines(newfile)
for l in lines:
    print l
typelable = 'addfin'
typelable2 = 'tx'
typelablenew = 'tx'
modulename ='TransEXT'
modulename ='Performance_mtd'
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
        prefix = 'bool' #l[2] #l[2]
        fname = l[0]#l[1]
        fullname = fname.lower().replace(' ','_') #prefix + '_' + fname
        fulldesc = 'bla'#l[3]
        ftype = prefix #'decimal' # fulldesc.split('(')[0]
        newf = fullname
        dropdownname = 'language_list'
        defaultval = 'English'
        labelprefix = 'LBL_CR_'
        print '\''+newf +'\''+ ' => ('
        print '\'name\' => ' +  '\''+newf +'\','
        print '\'vname\' => ' +  '\''+labelprefix+newf.upper() +'\','
        print '\'type\' => ' +  '\''+ ftype +'\','
        if ftype == 'float':
            floatval ='15'
            floatprec = '4'
            flen = '14'
            print '\'precision\' => ' +  '\''+ floatprec +'\','         
            print '\'len\' => ' +  '\''+ flen +'\','
        elif ftype =='varchar':
            flen = '40'
            print '\'len\' => ' +  '\''+ flen +'\','
        elif ftype == 'date':
            print '\'len\' => \'date\','
            print '\'audited\' => false,'
            print '\'reportable\' => true,'
        elif ftype == 'bool':
            print '\'required\' => false,'
            print '\'reportable\' => false,'
            print '\'massupdate\' => false,'
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

for  l in lines:
    b = str(l).replace('[','').replace(']','')
    print '\'valid\' =>(bool)$this->bean-> '+ b + ','
 





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
