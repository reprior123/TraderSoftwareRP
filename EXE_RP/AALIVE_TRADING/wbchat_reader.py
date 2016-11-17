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
######need to create and add labels...
##then create tpl files
locationtag='GITHIGHVOL'
locationtag='HIGHVOL'
webroot='c:/' +locationtag + '/highvol/webroot/'
tplarea= webroot+'modules/CR_GII/tpls/investor_workflow/'
stepnum='4'
tplfile = tplarea +'step-'+stepnum+'.tpl'
outfile = 'step'+stepnum +'bla.tpl.php'
templatemodelfile = 'templatestep.tpl.php'
labelsfile =webroot +'custom/Extension/application/Ext/Language/en_us.CR_ComplianceCenter.php'
##$app_strings['LBL_CR_INVESTOR_PROFILE
gii_filein=downloads+'GII Questions and scoring - Questions.csv'
wbfilearea=EXE+'wbfiles'
flist=glob.glob(wbfilearea+'/*xlsx')
print flist
'''
###############################
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
##############extract_lbltags(labelsfile,mode,search)

mode='replagii_fileince'
mode='grep'
search = lable
search = 'radio'
search = '<'
replacer ='LBL'
##search = 'LBL_CR_INVESTOR_PROFILE'
replacer ='LBL_CR_INVESTOR_PROFILE.NEW'
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

###  Need to append all lables to lable file and replace templates
def lable_adder(labelname,labelstring):
    lableline = '$app_strings[\''+labelname+'\'] = \''+labelstring +'\';'
    rpu_rp.WriteStringsToFileAppend(labelsfile,lableline)
def createtpl(tplfile,stepnum):     
    fname='risk_volatility'
    answer1 =  '4%/year'
    answer2 = answer3 = answer4 = answer1
    answer1LBL = 'LBL_ANSWER_1_1_TEXT'
    answer2LBL=answer3LBL=answer4LBL=answer1LBL
    LBL_Question_title='LBL_'+fname.upper()
    question_text='what is assets?'

    ansnumin='1'
    question_text = fileloader(gii_filein,'questiontext',stepnum,ansnumin)
    a1_text = fileloader(gii_filein,'anstext',stepnum,ansnumin)
    a1_text = fileloader(gii_filein,'anstext',stepnum,'2')
    a1_text = fileloader(gii_filein,'anstext',stepnum,'3')
    a1_text = fileloader(gii_filein,'anstext',stepnum,'4')

    topsection = ' \n\
    <div class="step">\n\
            <div class="moduleTitle hd">\n\
                    <h2>{$APP.LBL_CR_INVESTOR_PROFILE} - {$APP.LBL_CR_LEGAL_ENTITIES}</h2>\n\
                    <h3>{$APP.LBL_CR_INVESTMENT_GUIDELINES} - {$APP.LBL_CR_STEP} '+ stepnum +'</h3>\n\
                    <div class="clear"></div>\n\
            </div>\n\
            <div class="row portfolio-overview">\n\
                    <div class="small-12 column">\n\
                            <p><b>{$APP.' +LBL_Question_title+'}:</b><br><br>\n\
                            </p>\n\
                            <form class="step_form">\n\
                                    <p>'
    midlines = '\n\
    <input type="radio" name="'+fname+'" value="'+answer1+'" {if $data->'+fname+' eq "'+answer1+'"}checked="checked"{/if}>{$APP.'+answer1LBL + '}<br>\n\
    <input type="radio" name="'+fname+'" value="'+answer2+'" {if $data->'+fname+' eq "'+answer2+'"}checked="checked"{/if}>{$APP.'+answer2LBL + '}<br>\n\
    <input type="radio" name="'+fname+'" value="'+answer3+'" {if $data->'+fname+' eq "'+answer3+'"}checked="checked"{/if}>{$APP.'+answer3LBL + '}<br>\n\
    <input type="radio" name="'+fname+'" value="'+answer4+'" {if $data->'+fname+' eq "'+answer4+'"}checked="checked"{/if}>{$APP.'+answer4LBL + '}<br>\n\
                                    </p>\n\
                            </form>\n\
                    </div>\n\
            </div>\n\
            <a href="javascript:void(0)" onclick="SUGAR.RiskWorkflow.next()" data-step="'+stepnum+'" class="button gen-button next" >{$APP.LBL_CR_NEXT}</a>\n\
    </div> '
##    print topsection
##    print midlines
    fulltext =topsection + midlines
    rpu_rp.WriteStringsToFile(tplfile,fulltext)
    print 'wrtiing to...',tplfile
    labelname='LBL_ANSWER_1_1_TEXT'
    labelstring='LBL_ANSWER_1_1_TEXT'
    lable_adder(labelname,labelstring)
    lable_adder(LBL_Question_title,question_text)
#######################
def fileloader(filein,mode,qnumin,anumin):
    lines = rpu_rp.CsvToLines(filein)
    tag=text=''
    finalanswer= 'nonfound'
    #['GII', 'GII_result', 'Q', '3', '3', 'n/a', '', '', 'MultipleChoice', 'income_certainty', '', 'Wie beurteilen S
    for l in lines:
        qnum = anum ='xxx'       
        if l[0] == 'GII' and l[2] == 'Q':
            qnum=l[3]
            question_text=l[11]
        if l[0] == 'GII' and l[2] == 'A':
            anum=l[3]
            answer_text=l[11]
        if mode == 'questiontext' and qnum == qnumin :
            finalanswer = question_text
        if mode == 'anstext' and anum == anumin :
            finalanswer = answer_text
    print finalanswer
    return finalanswer
######################
##question_text = fileloader(gii_filein,'questiontext','1')
##print question_text
#######################
for c in range(1,6):
    stepnum=str(c)
    print '>>>>>>>>>>>      ',stepnum, '     >>>>>>>>>'
    tplfile = tplarea +'step-'+stepnum+'.tpl'
##    revise_tpl_file(tplfile,mode,search,replacer)
    createtpl(tplfile,stepnum)
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
'''
