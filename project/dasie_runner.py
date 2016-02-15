# -*- coding: utf-8 -*-
import multiprocessing
import subprocess


#config
#: DASIE 경로
DASIE = '/home/pi/dasie'
#: exedep.sh 경로
EXEDEP_PATH = DASIE+'/exedep.sh'
#: exedesc.sh 경로
EXEDESC_PATH = DASIE+'/exedesc.sh'
#: kill.sh 경로
KILL_PATH = DASIE+'/kill.sh'
#: 외부모듈들의 경로들
MODULE1_PATH = DASIE+'/module1.py'
MODULE2_PATH = DASIE+'/module2.py'
MODULE3_PATH = DASIE+'/module3.py'
MODULE4_PATH = DASIE+'/module4.py'
#: DataDefinition.xml 이 생성된 경로와 실행될(복사되야하는) 경로, 파일이름
DATADEFINITION_SRC_FILE_PATH = DASIE+'/template/ddl/newDataDefinition.xml'
DATADEFINITION_TAR_FILE_PATH = DASIE+'/dist/config/DataDefinition.xml'
#: Task.xml 이 생성된 경로와 실행될(복사되야하는) 경로
#TASK_SRC_PATH = ''
#TASK_TAR_PATH = ''

def copy_xmls():
	subprocess.call('cp ' + DATADEFINITION_SRC_FILE_PATH + " " + DATADEFINITION_TAR_FILE_PATH)

def run_exedep():
	subprocess.call("cd "+DASIE+"\n"+"./exedep.sh", shell=True)

def run_exedesc():
	subprocess.call("cd "+DASIE+"\n"+"./exedesc.sh", shell=True)

def module1():
	subprocess.call('python '+MODULE1_PATH, shell=True)

def module2():
	subprocess.call('python '+MODULE2_PATH, shell=True)

def module3():
	subprocess.call('python '+MODULE3_PATH, shell=True)

def module4():
	subprocess.call('python '+MODULE4_PATH, shell=True)

def run_dasie():
    jobs = []

    m1 = multiprocessing.Process(target=module1)
    jobs.append(m1)
    m1.start()

    m2 = multiprocessing.Process(target=module2)
    jobs.append(m2)
    m2.start()

    m3 = multiprocessing.Process(target=module3)
    jobs.append(m3)
    m3.start()

    m4 = multiprocessing.Process(target=module4)
    jobs.append(m4)
    m4.start()

    p = multiprocessing.Process(target=run_exedep)
    jobs.append(p)
    p.start()

    q = multiprocessing.Process(target=run_exedesc)
    jobs.append(q)
    q.start()

def shoot():
	subprocess.call("cd "+DASIE+"/pipe"+"\n"+"cat original.csv > read_1.pip", shell=True)


def shoot_data():
	jobs = []
	m1 = multiprocessing.Process(target=shoot)
	jobs.append(m1)
	m1.start()

def kill():
	subprocess.call("cd "+DASIE+"\n"+"./kill.sh", shell=True)

def kill_dasie():
	jobs = []
	m1 = multiprocessing.Process(target=kill)
	jobs.append(m1)
	m1.start()