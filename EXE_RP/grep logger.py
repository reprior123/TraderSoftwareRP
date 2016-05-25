# -*- coding: utf-8 -*-
import os, sys, glob, csv, subprocess, datetime, shutil, subprocess, time
#########################################
path = os.getcwd() + '/'
rootpath = ((path.replace('EXE','|')).split('|'))[0]
localtagSLASH = '_ACTANT/'
localtag = '_ACTANT'
EXEnoslash = rootpath + 'EXE' + localtag
sys.path[0:0] = [EXEnoslash] 
import rputiles, rpu_rp
################################
EXE = EXEnoslash + '/'
DATA = rootpath + 'DATA' + localtagSLASH
TMP = rootpath + 'TMP' + localtagSLASH
ActantData = 'C:/Program Files/Actant/Log/'
ActantDataNoSlash = 'C:/Program Files/Actant/Log'
todayf = 'AQTOR_20150406_1.log'

##def grep_txtfile_to_array(infilename,greppattern):
###############################################################################
##def grep_to_txtfile(infilename,greppattern,outfilename,fieldnum):
##   WriteStringsToFileAppend(filename,stringname):
#######################################################
##array =[]
for f in  os.listdir(ActantDataNoSlash):   
    print f
fblaw = raw_input('enter filename here:  ')
##rpu_rp.WriteStringsToFileAppend(ActantData + f,f)
array = rpu_rp.grep_txtfile_to_array(ActantData + todayf,'6A')
##print array
for line in array:
    print line

##grep '6A' ActantData + f
####### flush the outfile   ####
##filename = TMP + 'tempflashmail.txt'
##rputiles.write_file_array(filename,'\n')
#### end flush   ################

########################################
##recipient = 'helen.vollxxxxxxxxmann@actant.com'
##subject = 'recent sage flash output'
##body = 'see report pls'
##attachment_fullpath = filename
##sender = 'rob.prior@actant.com'
##senderpwd = 'clipper123'
##ccnamelisttext = sender
##rputiles.gmail_attachment(recipient, subject, body, attachment_fullpath, sender, senderpwd, ccnamelisttext)
##print 'sagecode', 'sagedate', 'Year', 'Month', 'firmcode', 'transid', 'CHFamtACTUAL', 'BaseAmt', 'CHFamtFIXED', 'Curr', 'nomAcct', 'nominalname', 'Details',\
##      'Type', 'ref', 'Exref', 'cat1', 'cat2', 'cat3', 'cat4', 'cat5', 'owner', 'ImportMeFX', 'TaxAmtBase', 'STATUS', 'PrevNominal', 'Prevtransid',\
##      'Detailsshort'
