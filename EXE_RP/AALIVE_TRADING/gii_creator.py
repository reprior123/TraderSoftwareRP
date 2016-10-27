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
locationtag='GITHIGHVOL'
webroot='c:/' +locationtag + '/highvol/webroot/'
tplarea= webroot+'modules/CR_GII/tpls/investor_workflow/'
stepnum='4'
tplfile = tplarea +'step-'+stepnum+'.tpl'
outfile = 'step'+stepnum +'bla.tpl.php'
templatemodelfile = 'templatestep.tpl.php'
labelsfile =webroot +'custom/Extension/application/Ext/Language/en_us.CR_ComplianceCenter.php'
##C:\GITHUB\addfin-latest\addfin-sugar\webroot\
def extract_lbltags(filein,mode,search):
    lines = rpu_rp.CsvToLines(filein)
    tag=text=''
    for l in lines:
##        print l
##        ["$app_strings['LBL_CR_NO'] = 'No';"]       
        lsplit=str(l).split('\'')
        if len(lsplit) >3:
            tag=lsplit[1]
            text=lsplit[3]
        if mode == 'all':
            print tag, '>>>',text
            pass
        else:
            if search == tag:
                print tag, text
                pass
            else:
                pass
mode='search'
mode='all'
lable= 'LBL_CR_UP_TO'
lable='LBL_CR_SURROUNDINGS'
search = lable
extract_lbltags(labelsfile,mode,search)
###########################
def revise_tpl_file(filein,mode,search,replacer):
    lines = rpu_rp.TxtToLines(filein)
    tag=text=''
    for l in lines:
##        print l
        lsplit=str(l).split('\'')
        if len(lsplit) >3:
            tag=lsplit[1]
            text=lsplit[3]
        if mode == 'all':
            print tag, '>>>',text
            pass
        elif mode == 'replace':
            tag1=search
            tag2=replacer
            newl = str(l).replace(tag1,tag2)
            print newl
            pass
        elif mode == 'grep':
            tag1=search
            tag2=replacer
            newl = str(l).replace(tag1,tag2)
            if search in str(l) or replacer in str(l):
                print l
            pass
        else:
            pass
mode='replace'
mode='grep'
search = lable
search = 'radio'
search = '<'
replacer ='LBL'
##search = 'LBL_CR_INVESTOR_PROFILE'
replacer ='LBL_CR_INVESTOR_PROFILE.NEW'
for c in range(1,9):
    stepnum=str(c)
    print '>>>>>>>>>>>      ',stepnum, '     >>>>>>>>>'
    tplfile = tplarea +'step-'+stepnum+'.tpl'
    revise_tpl_file(tplfile,mode,search,replacer)
######################






















##["$app_strings['LBL_CR_NO'] = 'No';"]
##<p><b>{$APP.LBL_CR_ASSETS}:</b><br><br>   line for questionheader
##nextline is the questiontag
##fieldname found 
#:$app_strings['LBL_CR_UP_TO'] = 'Up to';
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
