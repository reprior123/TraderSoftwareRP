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
global timedate_format, nextorderID, date, today,recentlimit, time_format
from time import sleep, strftime, localtime
import  rpu_rp, rpInd, ibutiles, TicksUtile, RP_Snapshot, glob, csv, subprocess, datetime, shutil, time, BarUtiles
from time import sleep, strftime, localtime
import RulesEngine
from datetime import datetime
import ctypes
################
sym = 'ES'
date =  today  ######## <<<<<<<
print '1 : ES \n2 : FDAX'
symnum = raw_input('sym: ')
if symnum == '1':
    sym = 'ES'
else:
    sym = 'FDAX'
for ind in indlist_oscils:
    dur = '5mins'
teststr = 'grnNnotailNbigbar' #'2016-02-19 21:'
closestr = 'grnNnotailN'
pos = netcost = 0
'''
add 5 bar moving average, vwap study, breakpoints assembler option
'''
import Createlines
#################################
def show_spots(sym,date,limit,spotfile):
    curprice = float(TicksUtile.recenttick(sym,'recent'))
    spotlines= rpu_rp.CsvToLines(spotfile)
    for l in spotlines:
        spotp = float(l[0])
        if len(l) > 1 :
##            print l
            spotid = l[1]
            pass
        else:
            spotid=''
        distance = abs(spotp-curprice)
        if (spotp-curprice) > 0:
            underover = 'under'
        else:
            underover = 'over'
        if distance < limit:
            if underover == 'under':
                sflag = 'SELL'
            else:
                sflag = 'BUY'
            print ('>>%4s at %8.2f %s|%s|%4.2f|%8.2f|' % (sflag,spotp,spotid,sym,distance,curprice))
#####################
def showlines(sym,dur,buysell):
    filen = DataDown +date +'.'+sym+'.'+dur + '.bothHA.csv'
    lines = rpu_rp.CsvToLines(filen)
    newlines = []
    pnlsign = -1    
    if buysell == 'sell':
        teststr = 'redNnotailNbigbar' #'2016-02-19 21:'
        closestr = 'redNnotailN'
        pnlsign = (1)
        pass
    elif buysell == 'buy':
        teststr = 'grnNnotailNbigbar' #'2016-02-19 21:'
        closestr = 'grnNnotailN'
        pass
    else:
        teststr = 't'
        closestr = 'xxxxx'
    pos =  netcost = 0
    for l in lines:
        if 'partxxxx'  in str(l):
            print l
        if len(l) > 15:
##            print l
            markprice = round(float(l[5]),2)
            tdate = str(l[1])
            if teststr in str(l):  #if red signal sell one until..
                pos +=1
                netcost += (1 * markprice)
                avgcost = round(netcost / pos,2)
                oneline = str(pos)+ ' | ' + str(avgcost)+ ' | ' +  str(markprice)+ ' | ' + tdate
                if buysell == 'allxx':
##                    print l
                    newlines.append(l[1]+l[16])
                    pass
                else:
                    newlines.append(oneline)
        ##        print l
            if closestr not in str(l):
                pnl = (netcost - (markprice * pos) )*pnlsign
                if pos != 0 :
                    oneline = 'closing_' + buysell.upper() +' | ' + str(markprice)+ ' | pnl= ' +str(pnl) + ' | ' + tdate
                    if buysell != 'allxx':
                        newlines.append(oneline)
                netcost = 0
                pos = 0
    return newlines
#################
now = datetime.strftime(datetime.now(),spaceYtime_format)
def run_oneloop(dur,now,sym,date):
    now_epoch = int(time.mktime(time.strptime(now, spaceYtime_format)))
##    print '##### ',now, dur, sym,' ####### '
##    Createlines.create_HAs([sym],date)
    print 'got to clines'
    Createlines.make_both_states([sym],date)
    ##########
    perc = .70
    maxlines = 5
    difflimit = 700
    taglist = ['buy','sell','allxx']
    for tag in taglist:    
        b = showlines(sym,dur,tag)
        print '#############'
        print '>>>>>> ',tag.upper(), 'WINDOW',dur,sym, ' <<<'
        lenha = len(b)
        c=0
        climitlines = int(lenha * perc)
        climit = max((lenha-maxlines),climitlines)
        bar_time = '  2016-02-21 13:16:30'
        for lha in b:
            c+=1
            if tag != 'allxx':
                if len(lha.split('|')) > 2:
                    bar_time = (lha.split('|')[3]).replace(' 201','201')  
                bar_time_epoch =  TicksUtile.convertTime(bar_time,'dashspace','timetoepoch')       
                tdiff =  now_epoch - bar_time_epoch
            else:
                    bar_time_epoch =  TicksUtile.convertTime(bar_time,'dashspace','timetoepoch')          
                    tdiff =  0# now_epoch - bar_time_epoch                
            if c > climit and tdiff < difflimit :
                print lha,'>>> ',tdiff #,difflimit
            #######   
############################################
def createOneMerge(dur,now,sym,date):
    now_epoch = int(time.mktime(time.strptime(now, spaceYtime_format)))
##    print '##### ', dur, sym,' ####### '
    durinseconds= secdict[dur]
    basisdur = '1min'
    if dur == '1min':
        basisdur ='5secs'
    basisfile = DataDown +date+'.'+sym+'.'+basisdur+'.both.csv' ### this bit not used yet until expand startmode
    basisbars = rpu_rp.CsvToLines(basisfile)
##    print'creating bars'   
    recentbars = TicksUtile.create_bars_from_bars(basisbars,date,sym,dur,durinseconds,'noHA')
##    print 'done creating bars'
    filerecent = DataDown +date+'.'+sym+'.'+dur.replace(' ','')+'.recent' +'.csv'
    rpu_rp.WriteArrayToCsvfile(filerecent,recentbars)
    ## now merge recent and both
    fileddload = filerecent.replace('recent','ddload')
    outfile = filerecent.replace('recent','both')
    cutoffmintime = int(int(durinseconds) - 5)
    if os.path.isfile(filerecent):
        TicksUtile.merge_bar_files(filerecent,fileddload,outfile,cutoffmintime)
    else:
        shutil.copyfile(fileddload,outfile)
##        print 'found no ddload file so did no merge'
        ##########
    basisfile = DataDown +date+'.'+sym+'.'+dur+'.both.csv' ### note the basis dur changed to just dur!!
    basisbars = rpu_rp.CsvToLines(basisfile)
    HAbars = TicksUtile.create_bars_from_bars(basisbars,date,sym,dur,durinseconds,'hamode')
##    print 'done creating HA bars'
    fileHABoth = DataDown +date+'.'+sym+'.'+dur.replace(' ','')+'.bothHA' +'.csv'
    rpu_rp.WriteArrayToCsvfile(fileHABoth,HAbars)
#################################    
loopmax = 505
loop = 0
while loop < loopmax:
    TicksUtile.prepare_tickfilesto5secBars(date,sym,'initialize')
        # need to create 5secs and then each dur before proceding
    now = datetime.strftime(datetime.now(),spaceYtime_format)
    durlist = ['1min','3mins','5mins','15mins','1hour','1day']
    for dur in durlist:
        createOneMerge(dur,now,sym,date)
    dur = '5mins'
    run_oneloop(dur,now,sym,date)
    factor = 1
    limitlines = 5.0
    if sym == 'FDAX':
        limitlines = 15.0
    curprice = float(TicksUtile.recenttick(sym,'recent'))
    print '###### LINEFADES #### ',curprice ,sym
    spotfiles = ['Full.','WBDaily.','Roundies.','AutoPivot.']
    print 'range is ',limitlines, 'check for passes'
    for tag in spotfiles:
        spotfile = libarea + 'Spots' +tag + sym+'.txt'           
        show_spots(sym,date,limitlines,spotfile)
    loop+=1
    sleep(15)
'''
['ES', ' 2016-02-19 22:05:00', '1913.75', '1914.5', '1913.75', '1914.0',
'8603.0', 'full', '300', '0.25', '0.5', '0.0', 'grnNnotailNshortbar']
['ES', ' 2016-02-19 22:30:00', '1914.25', '1914.25', '1913.75', '1914.0', '471.0', 'full', '960', '-0.25', '0.0', '-0.25', 'redNnotailNshortbar']
'''
