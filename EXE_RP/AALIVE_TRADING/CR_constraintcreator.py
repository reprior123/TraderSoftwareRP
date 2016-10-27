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
assetlist=['Equities','Commodities', 'Real Estate']
for a in assetlist:
    print a
    word='Knowledge'
    word='Experience' # use lables here
    
    question =  'rate the following 1=Expert '+word+', 2=Some'+word+', 3=No '+word
    print question
###############
def prepare_imp_file(filein,fileout):
    newlines =[]
    lines = rpu_rp.CsvToLines(filein)
    headerline =['Action', 'Quantity', 'Symbol', 'TimeInForce', 'SecType', 'OrderType', 'LmtPrice', 'Exchange', 'Currency', 'CUSIP', 'ISIN', '']
    headerline =['name', 'roloid', 'isin', 'sugarid', 'tradedcurr', 'assetclass','sector']
    newlines.append(headerline)
    for l in lines:
        newline =[]
        newlinebla =[]
        c=0
        for i in  headerline:
            newvar=locals()[i]
            if newvar=='isin':
                print newvar
            newline.append(newvar)
        newlines.append(newline)
    rpu_rp.WriteArrayToCsvfile(fileout,newlines)
#############
##prepare_imp_file(downloads+'bla.csv',downloads +'fileout.csv')
