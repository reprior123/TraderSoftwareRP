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
newfile = downloads +'Portfolio Figures - Copy of Sheet1.csv'
#newfile = heredir + '/fieldsin.csv'
import fileinput

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
def make_vardefs():
    for l in lines:
    ##    print l
        if l[0] != 'ggggggg':
            floatprec =''
            prefixoveride='price'
            prefix = l[0]#=''#'org' # l[1] #l[2]
            fname = l[1].replace(' ','_').replace('(','_').replace(')','').lower()#l[1]
            fullname = fname #prefix + '_' + fname
            fulldesc = 'bla'#l[3]
            ftype = prefix #'decimal' # fulldesc.split('(')[0]
            if prefixoveride =='price':
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
            lablearray.append('\''+labelprefix + newf.upper().replace('___','_')  +'\''+ ' => \'' + newf.replace('_',' ').replace('  ','') +'\',')

    for  l in lablearray:
        print l

def make_one_panel(modname):
    panelheader = ' \'lbl_editview_panel1\' =>'
    arraystart  ='array ('
    rowstart = '0 =>'
    row2start = '1 =>'

    newline='\n'
    colstart = '0 =>'
    fnameline =   '\'name\' => \'cvar___modified__\','
    
    flabelline = ' \'label\' => \'LBL_CVAR___MODIFIED__\','
    closearray = '),'

    fullpanel = panelheader + arraystart + rowstart + arraystart + colstart + arraystart + fnameline +flabelline
    linelist = [panelheader,arraystart,rowstart,arraystart,colstart,arraystart,fnameline,flabelline]
    fullstring = ''
    for r in linelist:
        fullstring += r
        fullstring += '\n'
        pass
    print fullstring
##for c in range(1,5):
make_one_panel('bla')

'''
              \'lbl_editview_panel1\' =>
      array (
        0 =>
        array (
          0 =>
          array (
            \'name\' => \'cvar___modified__\',
            \'label\' => \'LBL_CVAR___MODIFIED__\',
          ),
          1 =>
          array (
            'name' => 'cvar___normal_',
            'label' => 'LBL_CVAR___NORMAL_',
          ),
        ),
      ),
2 =>
        array (
          0 =>
          array (
            'name' => 'cdar___normal__',
            'label' => 'LBL_CDAR___NORMAL__',
          ),
          1 =>
          array (
            'name' => 'dar___normal__',
            'label' => 'LBL_DAR___NORMAL__',
          ),
        ),
        3 =>
'''

