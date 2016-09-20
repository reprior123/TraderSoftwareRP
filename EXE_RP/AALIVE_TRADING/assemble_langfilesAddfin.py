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
moduleNames = open('importmodlist.txt').readlines()
for module in moduleNames:
    modulestripped = module.strip()
    if modulestripped != titleself:
##        print '...',modulestripped,'xxx',titleself
        my_module = importlib.import_module(modulestripped)
        pass
    else:
        print 'is self'
######################
import Mod_TicksUtile, Mod_ibutiles
######################
from ib.ext.Contract import Contract  
from ib.opt import ibConnection, message
from ib.ext.Order import Order
from ib.opt import Connection, message   ##??
#############################
global  sym, symbol_list, symdict
########################################
date = today
modules = 'C:/GITHUB/addfin-latest/addfin-sugar/webroot/modules'
flist = glob.glob(modules +'/language/en*.php')
modulestoExclude = ['ModuleBuilder','Administration']
print flist
##dirlist = os.walk(modules)
dirlist = os.listdir(modules)
##dirlist = ['Leads']
print modules
alllines=[]
print downloads
for module in dirlist:
    print module
    langdir = modules + '/' + module + '/language/'
    engfile = langdir + 'en_us.lang.php'
    gerfile = langdir + 'de_de.lang.php'
    print gerfile
    gerlines = rpu_rp.TxtToLines(gerfile)
    englines = rpu_rp.TxtToLines(engfile)
    for lg in gerlines:
        lineout=[]
        if '=>' in str(lg):
            spline = lg.split('=>')
            labelger = spline[0].strip()
            gerword = spline[1].strip()
##            print labelger, module
            for l in englines:
                if '=>' in str(l):
                    spline = l.split('=>')
                    labeleng = spline[0].strip()
                    engword = spline[1].strip()
                    if labelger == labeleng:
                        lineout.append(labelger)
                        lineout.append(labeleng)
                        lineout.append(gerword)
                        lineout.append(engword)
                        lineout.append(module)
                        alllines.append(lineout)
##                        print labelger,labeleng,engword,gerword,module
rpu_rp.WriteArrayToCsvfile(downloads +'csvfileout.csv',alllines)
                                       
##    output =    rpu_rp.diff2files(engfile,gerfile,'changes')
##print output
'''
dloads = 'C:/Users/bob/Downloads/blount/'
xlsdir = dloads +'dirxls/'
def convertxls():
    flist = glob.glob(dloads +'*.xlsx')
    for f in flist:
##        rpu_rp.convertXLSXtoCSV(f)   
        print f
#####################
def convertname():
    flist = glob.glob(xlsdir +'wb*.xlsx')
    print flist
    for f in flist:
        newname = f.replace('C:/Users/bob/Downloads/blount','newst')
        rpu.convertXLSX(f,'txt')
        print newname
#####################
convertname()
##def convertname():
##    flist = glob.glob(dloads +'blo*.txt')
##    for f in flist:
##        newname = f.replace('C:/Users/bob/Downloads/blount\\blount','wbn')
##        os.system('cp ' +f+ ' ' + dloads + newname)
####        rpu_rp.convertXLSXtoCSV(f)
##        print newname
##        print f
#######################
##convertname()
'''

