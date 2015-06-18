#!/usr/local/bin/python

from bs4 import BeautifulSoup
from django.conf import settings
from django.template import Template, Context 
from django.http import HttpResponse  
import re,datetime
import subprocess
import os
import mailAgent

def getSummFromOldReportFile(oldReportFile):
    summ_dict = {'total_num':0,'pass_num':0,'failed_num':0,'ignored_num':0,'exception_num':0,'costTime':0.0}
    fp = open(oldReportFile)
    soup = BeautifulSoup(fp) 
    summ_table = soup.find('table')
    for row in summ_table.findAll('tr'):
        col = row.findAll('td')
    records=[]
    for cell in  col:
        if cell.find('a'):
            records.append(cell.a.next)
        else:
            records.append(cell.next)
    print records
    summ_dict['total_num']=int(records[0].split()[0])
    summ_dict['pass_num']=int(records[1].split()[0])
    summ_dict['failed_num']=int(records[2].split()[0])
    summ_dict['ignored_num']=int(records[3].split()[0])
    summ_dict['exception_num']=int(records[4].split()[0])
    summ_dict['costTime']=float(records[5].split()[0])
 
    return summ_dict
#compare the testResult with last time
def diffTwoDict(newDict,oldDict):
    diff_dict = {'total_num':'','pass_num':'','failed_num':'','ignored_num':'','exception_num':'','costTime':''}
    for item in oldDict:
        diff_value=newDict[item]-oldDict[item]
        if diff_value<0:
            diff_dict[item]=str(diff_value)
        else:
            diff_dict[item]='+'+str(diff_value)
    print diff_dict
    return diff_dict
  
def outputTestReport(sourceFile,templateFile,fitnesseUrl,reportFile):
    fp = open(sourceFile)
    soup = BeautifulSoup(fp) 
    linkAttrPass = soup.findAll('tr',{'class':'pass'})
    linkAttrFail = soup.findAll('tr',{'class':'fail'})
    linkAttrIgnore = soup.findAll('tr',{'class':'ignore'})
    linkAttrException = soup.findAll('tr',{'class':'error'})
    time_ver_table = soup.find('table')
    test_summ = soup.find('div',{'id':'test-summary'})
    fp.close()
    #get runTime and fitnesse version
    first_td = time_ver_table.tr.td
    run_time = first_td.next
    fit_version = run_time.next.next.next
    #get every value of test_summary
    test_res_list =  test_summ.div.strong.next.next.split(',')
    
    #add url linked to artemis 
    testcase_list = []
    for sourceList in (linkAttrPass,linkAttrFail,linkAttrIgnore,linkAttrException):
        tmp_list=[]
        for attr in sourceList:
            attr.a['href'] = fitnesseUrl+attr.a['href']
            tmp_list.append(str(attr))
        testcase_list.append(tmp_list)        
    
    summ_dict = {'total_num':0,'pass_num':0,'failed_num':0,'ignored_num':0,'exception_num':0,'costTime':0.0,'runTime':'','fitnesseVer':''}
    old_summ_dict = summ_dict
    summ_dict['pass_num'] = int(test_res_list[0].split()[0])
    summ_dict['failed_num'] = int(test_res_list[1].split()[0])
    summ_dict['total_num'] = int(summ_dict['pass_num'])+int(summ_dict['failed_num'])
    summ_dict['ignored_num'] = int(test_res_list[2].split()[0])
    summ_dict['exception_num'] = int(test_res_list[3].split('\n')[1].split()[0])
    summ_dict['costTime'] = round(float(test_res_list[3].split('\n')[2].strip()[1:-1].split()[0])/1000,1)
    summ_dict['runTime'] = run_time.strip()
    summ_dict['fitnesseVer'] = fit_version.split(':')[1].strip()
    if os.path.exists(reportFile):
        old_summ_dict = getSummFromOldReportFile(reportFile)
    compare_summ_dict=diffTwoDict(summ_dict,old_summ_dict)
    compare_summ_dict=summ_dict
    settings.configure()
    fp = open(templateFile)  
    # using test report template file
    t = Template(fp.read())
    fp.close()
    c = Context({'summ_dict':summ_dict,'compare_summ_dict':compare_summ_dict,'failed_list':testcase_list[1],'ignored_list':testcase_list[2],'exception_list':testcase_list[3],'pass_list':testcase_list[0]})
    reportHtml = t.render(c) 
    writeToFile(reportFile,reportHtml)
    #return HttpResponse(reportHtml)  

#def downloadTestPage(usr,pwd,url):
def downloadTestPage(url):
    #indexFile = '/disk_d1/artemis/AutoTest/backgroud/jenkinsScripts/fitnesseIndex_tmp.html'
    #testResultFile = '/disk_d1/artemis/AutoTest/backgroud/jenkinsScripts/fitnesseTestPage_tmp.html'
    indexFile = 'fitnesseIndex_tmp.html'
    testResultFile = 'fitnesseTestPage_tmp.html'
    cmd = 'curl %s -o %s'%(url,indexFile)
    subprocess.call(cmd,shell=True)
    fp = open(indexFile)
    soup = BeautifulSoup(fp) 
    #pattern='ZeusSmokeTest\?pageHistory&amp;resultDate='+'[0-9]+'
    linkAttr = soup.table.a['href']
    
    fp.close()
    paramLastDate = ''
    if linkAttr:
        nPos = str(linkAttr).index('resultDate')-1
	paramLastDate = str(linkAttr)[nPos:nPos+26]
    if paramLastDate.strip != '':
	url=str(url+paramLastDate)
        cmd = 'curl -o %s "%s'%(testResultFile,url)
	cmd =cmd+'"'
        subprocess.call(cmd,shell=True)    
        return testResultFile
    else:
        return ''
def writeToFile(file,content):
    fp = open(file,'w')
    fp.writelines(content)
    fp.close

if __name__ == '__main__':
    #fitnesseUsr = 'admin'
    #fitnessePwd = 'admin'
    fitnesseHost = '192.168.16.212'
    fitnessePort = '8887'    
    fitnesseUrl = 'http://%s:%s/'%(fitnesseHost,fitnessePort)
    fitnesseResultUrl = 'http://%s:%s/ZeusSmokeTest?pageHistory'%(fitnesseHost,fitnessePort)
    report_template_file = '/home/fitnesse/ZeusSmokeTest/JenkinsZeusSmokeTest/reportTemplate.html'
    
    server ={'name':'mail.funshion.com','user':'qa-pub@funshion.com','passwd':'nihao123$'}
    fro = 'qa-pub@funshion.com'    
    to =['yangjiao@funshion.com']                                                
    #cc = ['team-gamma@funshion.com']                                                 
    cc = ['yangjiao@funshion.com']     
    subject = 'ZeusSmokeTest Report'  
    files = ['/home/fitnesse/ZeusSmokeTest/JenkinsZeusSmokeTest/finalTestReport.html']

    getSummFromOldReportFile(files[0])

    #fitnesse_test_hisotry_file = downloadTestPage(fitnesseUsr,fitnessePwd,fitnesseResultUrl)
    fitnesse_test_hisotry_file = downloadTestPage(fitnesseResultUrl)
    if fitnesse_test_hisotry_file.strip()!='':
        outputTestReport(fitnesse_test_hisotry_file,report_template_file,fitnesseUrl,files[0])       
        s = mailAgent.mailAgent(server, fro, to,cc, subject, "TO all:", files)
        s.send_mail()
    print 'done' 
    print(datetime.datetime.now())
