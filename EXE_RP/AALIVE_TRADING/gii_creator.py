import os, sys
localtag = '_RP'
sys.path[0:0] = [((os.getcwd().replace('EXE','|')).split('|'))[0] + 'EXE' +localtag]
#########################################
import ENVdicts
nd ={}
nd = ENVdicts.ENVdicts(localtag)
for var in nd.keys():
##    print var
    locals()[var] = nd[var]
##################

#TicksUtile, RP_Snapshot,
import glob, csv, subprocess, datetime, shutil, time
from time import sleep, strftime, localtime
from datetime import datetime
import ctypes
################
import imaplib, time, email
####################
import rpu_rp
####################
yesterday = '20151218'
date =  yesterday # today
#####################3
##########    pivot = rpInd.gatherline(sym,'pivot')###    R1 = rpInd.gatherline(sym,'R1')#####    S1 = rpInd.gatherline(sym,'S1')
######    print S1,R1,pivot
    ##do the same for weekly by adding dur to variables and create a weekly  from dailys..
##    find pivots, find fibbo retraces on recnt moves[rangebars,hi,lo]
##    read spots from file
##    calculate two roundies
##    calculate 10 handles off high of day,lowday,openday,yestclose,prevhourhilow
#############################################
######need to create and add labels...
##then create tpl files
webroot='c:/HIGHVOL/highvol/webroot/'
 
stepnum='1'
outfile = 'step'+stepnum +'bla.tpl.php'
templatemodelfile = 'templatestep.tpl.php'
labelsfile =webroot +'custom/Extension/application/Ext/Language/en_us.CR_ComplianceCenter.php'


def extract_lbltags(filein):
    lines = rpu_rp.CsvToLines(filein)
    for l in lines:
##        print l
        ["$app_strings['LBL_CR_NO'] = 'No';"]
        
        lsplit=str(l).split('\'')
        if len(lsplit) >3:
            tag=lsplit[1]
            text=lsplit[3]
            print tag
            print text
        
        pass
    pass
extract_lbltags(labelsfile)
###########################
##["$app_strings['LBL_CR_NO'] = 'No';"]
##<p><b>{$APP.LBL_CR_ASSETS}:</b><br><br>   line for questionheader
##nextline is the questiontag

fieldname found 
#:$app_strings['LBL_CR_UP_TO'] = 'Up to';
def lookup_lable(lable,filein):
    lines = rpu_rp.CsvToLines(filein)
    for l in lines:
        if lable == l[2]:
            print l[4]
lable= 'LBL_CR_UP_TO'
lookup_lable(lable,labelsfile)

###############
def prepare_imp_file(filein,fileout):
    newlines =[]
    lines = rpu_rp.CsvToLines(filein)
    headerline =['Action', 'Quantity', 'Symbol', 'TimeInForce', 'SecType', 'OrderType', 'LmtPrice', 'Exchange', 'Currency', 'CUSIP', 'ISIN', '']
    headerline =['name', 'roloid', 'isin', 'sugarid', 'tradedcurr', 'assetclass','sector']
    headerline =['module','resultmodule','QorA','QuestionNum','AnswerNum','AnswerScore','ScoreMethod','PrivateORGRelevant','QAType','QtextID','	English','German','French','notes']
    newlines.append(headerline)
    for l in lines:
##        print l
        newline =[]
        newlinebla =[]
        isin = l[1]
        c=0
        for i in  headerline:           
            locals()[i] = l[c]
            if locals()[i] == 'Q' and c==2:
                print i,locals()[i]
##                print l
                qtextid = l[9]
                print qtextid
                newvar=locals()[i]
                newline.append(newvar)
            c+=1
        newlines.append(newline)
        
    rpu_rp.WriteArrayToCsvfile(fileout,newlines)
#############
##prepare_imp_file(downloads+'GII Questions and scoring - Questions.csv',downloads +'fileoutgii.csv')
