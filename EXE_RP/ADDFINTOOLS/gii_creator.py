# -*- coding: cp1252 -*-
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
alivedir = os.getcwd() + '/'
######need to create and add labels...
##then create tpl files
locationtag='GITHIGHVOL'
locationtag='HIGHVOL'
webroot='c:/' +locationtag + '/highvol/webroot/'
##webroot = alivedir
tplarea=  webroot+'modules/PP_PII/tpls/investor_workflow/'
stepnum='1'
##tplfile = tplarea +'step-'+stepnum+'.tpl'
outfile = 'step'+stepnum +'bla.tpl.php'
templatemodelfile = 'templatestep.tpl.php'
labelsfile =webroot +'custom/Extension/application/Ext/Language/en_us.CR_PII.php'
##labelsfile =webroot +'en_us.CR_ComplianceCenter.php'
##$app_strings['LBL_CR_INVESTOR_PROFILE
gii_filein=downloads+'giiscoring - Questions.csv'
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
########################
mode='search'
mode='all'
lable= 'LBL_CR_UP_TO'
lable='LBL_CR_SURROUNDINGS'
search = lable
##############extract_lbltags(labelsfile,mode,search)
mode='replace'
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
######################################
###  Need to append all lables to lable file and replace templates
def lable_adder(labelname,labelstring):
    lableline = '$app_strings[\''+labelname+'\'] = \''+labelstring +'\';'
    print lableline
    rpu_rp.WriteStringsToFileAppend(labelsfile,lableline)
    #########################################
def createtpl(tplfile,stepnum):     
##    answer1 =  '4%/year'
##    answer2 = answer3 = answer4 = answer1
    nextstepnum = str(int(stepnum) +1)
    answer1LBL = 'LBL_ANSWER_GIIresult_'+stepnum+'_1_TEXT'
    answer2LBL = 'LBL_ANSWER_GIIresult_'+stepnum+'_2_TEXT'
    answer3LBL = 'LBL_ANSWER_GIIresult_'+stepnum+'_3_TEXT'
    answer4LBL = 'LBL_ANSWER_GIIresult_'+stepnum+'_4_TEXT'    
    
    ansnumin='1'
    fname='risk_volatility'
    fileloadstepnum = str(int(stepnum) -1)
    fname= fileloader(gii_filein,'questionheader',stepnum,ansnumin)
    question_text = fileloader(gii_filein,'questiontext',stepnum,ansnumin)
    LBL_Question_title='LBL_'+fname.upper()

    answer1 = fileloader(gii_filein,'anstext',stepnum,ansnumin)
    answer2 = fileloader(gii_filein,'anstext',stepnum,'2')
    answer3 = fileloader(gii_filein,'anstext',stepnum,'3')
    answer4 = fileloader(gii_filein,'anstext',stepnum,'4')

    topsection = ' \n\
    <div class="step">\n\
            <div class="moduleTitle hd">\n\
                    <h2>{$APP.LBL_CR_INVESTOR_PROFILE} - {$APP.LBL_CR_LEGAL_ENTITIES}</h2>\n\
                    <h3>{$APP.LBL_CR_INVESTMENT_GUIDELINES} - {$APP.LBL_CR_STEP} '+ stepnum +'</h3>\n\
                    <div class="clear"></div>\n\
            </div>\n\
            <div class="row portfolio-overview">\n\
                    <div class="small-12 column">\n\
                            <p><b>{$APP.' +LBL_Question_title+'}</b><br><br>\n\
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
            <a href="javascript:void(0)" onclick="SUGAR.RiskWorkflow.next()" data-step="'+nextstepnum+'" class="button gen-button next" >{$APP.LBL_CR_NEXT}</a>\n\
    </div> '

    ### on last tpl file need finish text
    
##        <a href="javascript:void(0)" onclick="SUGAR.RiskWorkflow.next()" data-step="finish" class="button gen-button next" >{$APP.LBL_CR_FINISH}</a>
    fulltext =topsection + midlines
##    print fulltext
    rpu_rp.WriteStringsToFile(tplfile,fulltext)
    print 'wrtiing to...',tplfile
    labelname= answer1LBL
    labelstring=answer1
    lable_adder(answer1LBL,answer1)
    lable_adder(answer2LBL,answer2)
    lable_adder(answer3LBL,answer3)
    lable_adder(answer4LBL,answer4)
    
    lable_adder(LBL_Question_title,question_text)
######################
def create_vardefs(tplfile,stepnum):     
    nextstepnum = str(int(stepnum) +1)
    ansnumin='1'
    fname= fileloader(gii_filein,'questionheader',stepnum,ansnumin)
    question_text = fileloader(gii_filein,'questiontext',stepnum,ansnumin)
    LBL_Question_title='LBL_'+fname.upper()
    vardefsection = '\n\
                   \'' + fname + '\' =>\n\
                        array (\n\
                                \'required\' => false,\n\
                                \'name\' => \''+ fname+'\',\n\
                                \'vname\' => \''+ 'LBL_' + fname.upper() +'\',\n\
                                \'type\' => \'varchar\',\n\
                                \'massupdate\' => 0,\n\
                                \'no_default\' => false,\n\
                                \'comments\' => \'\',\n\
                                \'help\' => \'\',\n\
                                \'importable\' => \'true\',\n\
                                \'duplicate_merge\' => \'disabled\',\n\
                                \'duplicate_merge_dom_value\' => \'0\',\n\
                                \'audited\' => true,\n\
                                \'reportable\' => true,\n\
                                \'unified_search\' => false,\n\
                                \'merge_filter\' => \'disabled\',\n\
                                \'len\' => \'255\',\n\
                                \'size\' => \'20\',\n\
                        ),\n\
                        '
    topsection = ''
    rpu_rp.WriteStringsToFile('vardefsQs.txt',vardefsection)
##    print vardefsection
##    print LBL_Question_title
    lable_adder(LBL_Question_title,question_text)
    #################################
def create_giicontroller(tplfile,stepnum):
    nextstepnum = str(int(stepnum) +1)
    answer1LBL = 'LBL_ANSWER_GIIresult_'+stepnum+'_1_TEXT'
    answer2LBL = 'LBL_ANSWER_GIIresult_'+stepnum+'_2_TEXT'
    answer3LBL = 'LBL_ANSWER_GIIresult_'+stepnum+'_3_TEXT'
    answer4LBL = 'LBL_ANSWER_GIIresult_'+stepnum+'_4_TEXT'       
    ansnumin='1'
    fname= fileloader(gii_filein,'questionheader',stepnum,ansnumin)
    question_text = fileloader(gii_filein,'questiontext',stepnum,ansnumin)
    LBL_Question_title='LBL_'+fname.upper()

    answer1 = fileloader(gii_filein,'anstext',stepnum,ansnumin)
    answer2 = fileloader(gii_filein,'anstext',stepnum,'2')
    answer3 = fileloader(gii_filein,'anstext',stepnum,'3')
    answer4 = fileloader(gii_filein,'anstext',stepnum,'4')

    controllersection = '               \'' + fname + '\' => array(\n\
                            \''+answer1+'\' => \'1\',\n\
                            \''+answer2+'\' => \'2\',\n\
                            \''+answer3+'\' => \'3\',\n\
                            \''+answer4+'\' => \'4\',\n\
                            ),'
    rpu_rp.WriteStringsToFile('controllerQs.txt',controllersection)
    print controllersection    
#######################
def fileloader(filein,mode,qnumin,anumin):
##    print mode,qnumin,anumin
    lines = rpu_rp.CsvToLines(filein)
    tag=text=''
    finalanswer= 'nonfound'
    #['GII', 'GII_result', 'Q', '3', '3', 'n/a', '', '', 'MultipleChoice', 'income_certainty', '', 'Wie beurteilen S
    for l in lines:
        if mode=='print1line':
            print l
        qnum = anum ='xxx'       
        if l[0] == 'PII' and l[2] == 'Q':
            qnum=l[3]
            question_text=l[10]
            question_header=l[9]
        if l[0] == 'PII' and l[2] == 'A':
            anum=l[4]
            answer_text=l[11]
        if mode == 'questiontext' and qnum == qnumin :
            finalanswer = question_text
        if mode == 'questionheader' and qnum == qnumin :
            finalanswer = question_header
        if mode == 'anstext' and anum == qnumin +'.'+ anumin  :
            finalanswer = answer_text
##    print finalanswer.replace('ü','ue').replace('ä','au').replace('ö','oe')
    return finalanswer.replace('ü','ue').replace('ä','au').replace('ö','oe')
###################
for c in range(1,7):
    stepnum=str(c)
    stepnumfname = str(c+0)
##    print '>>>>>>>>>>>      ',stepnum, '     >>>>>>>>>'
    tplfile = tplarea +'step-'+stepnumfname+'.tpl'
##    revise_tpl_file(tplfile,mode,search,replacer)
##    createtpl(tplfile,stepnum)
##    create_vardefs(tplfile,stepnum)
##    show1line= fileloader(gii_filein,'print1line',stepnum,'1')
    create_giicontroller(tplfile,stepnum)
######################
##["$app_strings['LBL_CR_NO'] = 'No';"]
##<p><b>{$APP.LBL_CR_ASSETS}:</b><br><br>   line for questionheader
##nextline is the questiontag
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
<?php

if (!defined('sugarEntry') || !sugarEntry)
	die('Not A Valid Entry Point');

class CustomCR_GIIController extends SugarController {

	public function action_saveData() {
		$record = filter_input(INPUT_GET, 'record');
		$bean = BeanFactory::getBean('CR_GII');
		$bean->retrieve($record);
		$data = array();
		foreach ($_GET as $key => $value) {
			if (!in_array($key, array("module", "action", "record"))) {
				$data[$key] = $value;
				$bean->{$key} = $value;
			}
		}
		$bean->save();
		$this->auditFields($record, $data);
		
		header('Content-Type: application/json');
		echo json_encode(array('success' => true));
		sugar_cleanup(true);
	}

	public function auditFields($reportId, $fields) {
		global $current_user;
		$db = DBManagerFactory::getInstance();
		$bean = BeanFactory::getBean('CR_GII');
		$field_defs = $bean->getFieldDefinitions();
		$report = $bean->retrieve($reportId);
		$current_date = date('Y-m-d H:i:s', strtotime('now'));
		foreach ($fields as $key => $val) {
			$type = $before_value_text = $before_value_string = $after_value_text = $after_value_string = '';
			foreach ($field_defs as $def) {
				if ($def['name'] == $key) {
					$type = $def['type'];
					if (!in_array($type, array('text', 'varchar'))) {
						$before_value_string = $report->{$key};
						$after_value_string = $val;
					}else{
						$before_value_text = $report->{$key};
						$after_value_text = $val;
					}
				}
			}

	$sql = "INSERT INTO gii_audit (id, parent_id, date_created, created_by, field_name, data_type, before_value_string, after_value_string, before_value_text, after_value_text) "
					. "VALUES (UUID(), '$reportId', '$current_date', '$current_user->id', '$key', '$type', '$before_value_string', '$after_value_string', '$before_value_text', '$after_value_text')";
			$db->query($sql, false);
		}
	}
	
	public function action_saveRiskPoints(){
		$record = filter_input(INPUT_GET, 'record');
		$bean = BeanFactory::getBean('CR_GII');
		$report = $bean->retrieve($record);
		$report->appropiateness = $this->addRiskPoints('appropiateness', $report);
		$report->suitability = $this->addRiskPoints('suitability', $report);
		$report->risk_profile = ($report->appropiateness > $report->suitability) ? $report->suitability : $report->appropiateness;
		$report->save();
		
	}
	
	function addRiskPoints($qName, $data){
		$points  = $p = 0;
		$questions = array(
			'appropiateness' => array(
				'investment_horizon' => array(
					'lower_than1year' => '2',
					'1-4years' => '3',
					'4-10years' => '4',
					'greater_than10years' => '6',
				),
				'rate_security' => array(
					'short term' => '0',
					'currently' => '2',
					'long term' => '4',
				),
				'budgeted_expenses' => array(
					'no, invested assets required' => '0',
					'yes, invested assets dependent' => '2',
					'yes, no dependence from invested assets' => '4',
					'yes, allow savings to build assets' => '',
				),
				'assets_proportion' => array(
					'greater_than75%' => '0',
					'50-75%' => '1',
					'10-50%' => '2',
					'lower_than10%' => '4',
				),
				'liability' => array(
					'greater_than50%' => '0',
					'10-50%' => '3',
					'lower_than10%' => '5',
				),
				'bankable_assets' => array(
					'lower_than40%' => '0',
					'40-70%' => '2',
					'greater_than70%' => '4',
				),
				'planned_investment' => array(
					'greater_than30%' => '0',
					'10-30%' => '2',
					'lower_than10%' => '4',
				),
				'risk_evaluation' => array(
					'high' => '0',
					'average' => '1',
					'low' => '2',
				),
			),
			'suitability' => array(
				'willingness' => array(
					'(minus)2-5%' => '1',
					'10-(minus)4%' => '2',
					'17-(minus)7%' => '4',
					'31-(minus)16%' => '6',
					'45-(minus)25%' => '8',
				),
				'investment_loss' => array(
					'lower_than5%' => '2',
					'6-10%' => '4',
					'11-20%' => '6',
					'greater_than20%' => '8',
				),
				'tolerance_level' => array(
					'sell_asap' => '2',
					'wait_unconf' => '4',
					'accept_loss' => '6',
					'invest_more' => '8',
				),
			),
		);
		
		foreach($questions[$qName] as $k => $v){
			$p += (int) $questions[$qName][$k][$data->{$k}];
		}
		if($qName == 'appropiateness'){
			switch($p){
				case ($p >= 2 and $p <= 10):
					$points = 1;
					break;
				case ($p >= 11 and $p <= 19):
					$points = 2;
					break;
				case ($p >= 20 and $p <= 27):
					$points = 3;
					break;
				case ($p >= 28 and $p <= 35):
					$points = 4;
					break;
			}
		}elseif($qName == 'suitability'){
			switch($p){
				case ($p >= 5 and $p <= 9):
					$points = 1;
					break;
				case ($p >= 10 and $p <= 14):
					$points = 2;
					break;
				case ($p >= 15 and $p <= 19):
					$points = 3;
					break;
				case ($p >= 20 and $p <= 24):
					$points = 4;
					break;
			}
		}
		
		return $points;
	}
	
	public function pre_save(){
		parent::pre_save();
		$this->bean->name = $this->bean->client;
	}
}
'''
