#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sys
sys.path.insert(0, '/root/Bash_Mysql/')


# In[3]:


import os
import io, os, sys, types
import QueryString as QS
import logging
import logging.handlers
from logging.handlers import RotatingFileHandler
import sys

from cm_api.api_client import ApiResource
from datetime import datetime
from datetime import timedelta

import pandas as pd
import pymysql

import pytz

pd.set_option("display.width", 1500)
pd.set_option("display.max_Columns", 11)


# In[4]:


#command are consist of "opne" and "close"
def db_connection(command):
    global connection

    if command == "Open":
        logger = create_logger("db_connection.open")
        try:
            connection = pymysql.connect(host='bd-dev01', user='root', password='', db='TEST', charset='utf8')
        except Exception as e:
            logger.exception(e)

    elif command == "Close":
        if connection.open == True:
            logger = create_logger("db_connection.close")

            try:
                connection.close
            except Exception as e:
                logger.exception(e)
        else:
            return()


# In[5]:


#command are consist of "opne" and "close"
def db_connection(command):
    global connection
    
    if command == "Open":
        logger = create_logger("db_connection.open")
        try:
            connection = pymysql.connect(host='bd-dev01', user='root', password='', db='TEST', charset='utf8')
        except Exception as e:
            logger.exception(e)

    elif command == "Close":
        if connection.open == True:
            logger = create_logger("db_connection.close")

            try:
                connection.close
            except Exception as e:
                logger.exception(e)
        else:
            return()


# In[6]:


def create_logger(logger_name):
        today_date = datetime.today().strftime('%Y')

        #Create Logger
        logger = logging.getLogger(logger_name)
        
        #Check handler exists
        if len(logger.handlers) > 0:
            return logger # Logger already exists

        logger.setLevel(logging.INFO)

        formatter = logging.Formatter('[ %(asctime)s | %(levelname)s | %(name)s | #(filename)s:%(lineno)s ] > %(message)s')

        #Create Handlers
        streamHandler = logging.StreamHandler()
        
        if not os.path.exists('./log'):
                os.makedirs('./log/')

        #FileHandler = logging.FileHandler('./log/' + 'job_duration' + str(today_date) + '.log')
        rotatingFileHandler = RotatingFileHandler('./log/' + 'job_duration' + str(today_date) + '.log', maxBytes=10485760, backupCount=2) #10MB

        streamHandler.setLevel(logging.INFO)
        streamHandler.setFormatter(formatter)

        #FileHandler.setLevel(logging.INFO)
        #FileHandler.setFomatter(formatter)

        rotatingFileHandler.setLevel(logging.INFO)
        rotatingFileHandler.setFormatter(formatter)

        #Handlers Add
        logger.addHandler(streamHandler)
        #logger.addHandler(FileHandler)
        logger.addHandler(rotatingFileHandler)
        
        return logger


# In[7]:


def pre_process(query_data_df,user_jobstate):
    logger=create_logger("pre_process")


# In[8]:


def db_select(query):
    logger=create_logger("db_query")
    logger.info("# db_select START #")

    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        
            select_sql = str(query)

            #Linux Consol ANSI Control Word
            print("\033[3m" + "\033[32m" + "\t\t\t" + query + "\033[0m")

            cursor.execute(select_sql)
            selectData = cursor.fetchall()

    except Exception as e:
        logger.exception(e)
    finally:
        logger.info("# db_select END #")
        return selectData


# In[9]:


def db_insert(pre_process_data, query_date):
    logger=create_logger("db_insert")
    logger.info("# db_insert START #")
    
    try:
        with connection.cursor() as cursor:
        
            insert_sql = "INSERT INT ?tbl_nm (?col_nm) VALUES (?Col_TP)"
            
            insert_data = []
            for data in pre_process_data:
                insert_data.append((data['base_dt'], data['user'], data['app_name'], data['application_duration'], data['state'], data['start_time'], data['end_time']))

            cursor.executemany(insert_sql, insert_data)
            connection.commit()

    except Exception as e:
        logger.exception(e)
    finally:
        connection.close()
    logger.info("# db_insert END #")


# In[10]:


def db_update(query):
    logger=create_logger("db_update")

    try:
        with connection.cursor() as cursor:
        
            #"UPDATE BYDY_RISK_NTC_PRTC SET SEND_PROC_TP = '02' WHERE SEND_PROC_TP = '01'"
            update_sql = str(query)

            #Linux Consol ANSI Control Word
            print("\033[3m" + "\033[32m" + "\t\t\t" + query + "\033[0m")
            
            cursor.execute(update_sql)
            connection.commit()

    except Exception as e:
        logger.exception(e)
    finally:
        return()


# In[11]:


def read_exist_json():
    logger=create_logger("read_exist_json")
    logger.info("# read_exist_json START #")
    
    global jsonDir
    oneDayAgo     = datetime.today()-timedelta(1)

    jsonDir       = './' + 'mostRecentEvent_cumulateCount/'
    jsonToday     = jsonDir + datetime.today().strftime('%Y-%m-%d')  + ".json"
    jsonOneDayAgo = jsonDir + oneDayAgo.strftime('%Y-%m-%d')  + ".json"
    try:
        if not os.path.exists(jsonDir) :
            os.makedirs(jsonDir)

        if os.path.exists(jsonToday):
            jsonDf = pd.read_json(jsonToday) 
            print("json File Path : " + jsonToday)
        elif os.path.exists(jsonOneDayAgo):
            jsonDf = pd.read_json(jsonOneDayAgo) 
            print("json File Path : " + jsonOneDayAgo)
        else :
            jsonDf = pd.DataFrame()
            print("json File Doesn't exiest ")

        if not jsonDf.empty :
            jsonDf.OCR_DTM=jsonDf.OCR_DTM.astype('datetime64[ns]')
            jsonDf = jsonDf[['OCR_DTM', 'RISK_CLS_TP', 'SRVR_NM', 'TR_NM', 'HIGH_CALC_CNT', 'SUM_CNT', 'LOW_CALC_CNT', 'count(SRVR_NM)']]
        
        print(jsonDf)

    except Exception as e:
        logger.exception(e)

    logger.info("# read_exist_json END #")
    return(jsonDf.sort_index())


# In[18]:


def main(argv):
    logger = create_logger("main")
    logger.info("################ main START ###################")
    
    db_connection("Open")

    # db select
    for num in range(1,2):
        selectData = db_select(eval("QS.Qry"+str(num)))
        dbDataDf = pd.DataFrame(list(selectData))

    if not ( dbDataDf.empty ):
        dbDataDf = dbDataDf[['OCR_DTM', 'RISK_CLS_TP', 'SRVR_NM', 'TR_NM', 'HIGH_CALC_CNT', 'SUM_CNT', 'LOW_CALC_CNT', 'count(SRVR_NM)' ]]
        dbDataDf.RISK_CLS_TP=dbDataDf.RISK_CLS_TP.astype('int64')
    print(dbDataDf)

    #read json
    jsonDataDf=read_exist_json()
    
    if ( not (dbDataDf.empty) and (jsonDataDf.empty) ) :
        dbDataDf.to_json("./" + "mostRecentEvent_cumulateCount/" + datetime.today().strftime('%Y-%m-%d')  + ".json", date_format='iso')
    

    
    if not ( (dbDataDf.empty) or (jsonDataDf.empty) ):
        if 'OCR_DTM' in dbDataDf.columns :
            print("#"*30 + " mostRecentEvent_cumulateCount dataframe " + "#"*30)
            
            #if use df.append() then must do drop same tuple -> update recent_Time -> sum(count_1, count_2)
            #print("stored+select -> sort")
            appendSortDf=jsonDataDf.append(dbDataDf).sort_values(by='OCR_DTM',ascending=False).sort_values(by=['SRVR_NM','TR_NM']).reset_index(drop=True, level=0)
            #print(appendSortDf)

            #print("agg_sum")
            groupByAggDf=appendSortDf.groupby(['RISK_CLS_TP','SRVR_NM','TR_NM'],as_index=False).agg('sum')
            #print(groupByAggDf)

            #print("agg_sum -> sort")
            groupByAggDf=groupByAggDf.sort_values(by=['SRVR_NM','TR_NM']).reset_index(drop=True, level=0)
            #print(groupByAggDf)

            #print("dup drop -> drop count")
            appendSortDf=appendSortDf.drop_duplicates(['RISK_CLS_TP','SRVR_NM','TR_NM'], keep='first').drop(['count(SRVR_NM)'], axis=1).reset_index(drop=True, level=0)
            #print(appendSortDf)
            
            #print("concat agg_sum")
            appendSortDf=pd.concat([appendSortDf,groupByAggDf['count(SRVR_NM)']],axis=1)
            #print(appendSortDf)

            mergedDataDf=appendSortDf
            print(mergedDataDf)

            mergedDataDf.to_json(jsonDir + datetime.today().strftime('%Y-%m-%d')  + ".json", date_format='iso')

            print("*"*10+"TABLE(Dosen't Exist in mostRecentEvent_cumulateCount dataframe)"+"*"*10)
            uniqueDf=dbDataDf.append(jsonDataDf).append(jsonDataDf).reset_index(drop=True, level=0).drop_duplicates(subset=['RISK_CLS_TP','SRVR_NM','TR_NM'],keep=False).reset_index(drop=True, level=0)
            if not (uniqueDf.empty):
                if not os.path.exists("./smsAlert/") :
                    os.makedirs("./smsAlert/")
                    
                uniqueDf.to_json("./" + "smsAlert/" + "smsAlert" + datetime.today().strftime('%Y-%m-%d_%H-%M%S') + ".json", date_format='iso')
                print(uniqueDf)

            #select+append.json.delete.nondup.sort.reindex['OCR_DTM'] - json.append.select.delete.nondup.sort.reindex.['OCR_DTM']
            #a=dbDataDf.append(jsonDataDf)
            #a=a[a.duplicated(['RISK_CLS_TP', 'SRVR_NM', 'TR_NM'], keep=False)].drop

            print("*"*100+"dbSelectDf")
            dbSelectDf=dbDataDf.sort_values(by=['SRVR_NM','TR_NM']).reset_index(drop=True, level=0)
            print(dbSelectDf)
            
            print("*"*100+"json+append+dbSelecet df")
            b=jsonDataDf.append(dbDataDf)
            print(b)
            
            print("*"*100+"c df")
            global c
            c=pd.DataFrame()
            c=b[b.duplicated(['RISK_CLS_TP', 'SRVR_NM', 'TR_NM'], keep=False)]
            c=c.drop_duplicates(subset=['RISK_CLS_TP','SRVR_NM','TR_NM'],keep='first').reset_index(drop=True,level=0)
            print(c)
            
            print("*"*100+"d df")
            #d=c.drop_duplicates(['RISK_CLS_TP','SRVR_NM','TR_NM'], keep=False)
            d=dbSelectDf.OCR_DTM-c.OCR_DTM
            print(d)
            
            #최근이벤트(recentEvent&누적합계(cumSum)_시간값차이(diff)
            print("*"*100+"C_append_[TimeDiff] df")
            c['TIME_DIFF'] = d
            print(c)
            
            db_update(QS.Qry3)
            
    else :
        print("there is no merged dataframe")

    logger.info("############### main END ######################")
    
    if connection.open == True:
        db_connection("Close")
        connection.close()
    
    return


# In[22]:


main("")


# In[19]:


# The "main" entry
if __name__ == '__main__':
    sys.exit(main(sys.argv))

