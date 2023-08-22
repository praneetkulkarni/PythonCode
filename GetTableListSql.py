### Version       Date       Author                                    Comments
### 0.3         14/03/2023   Praneet Kulkarni            Firstversion of working code. first output for PVDMEXTR folder is sent and is working fine
### 0.3.1       17/03/2023   Praneet Kulkarni            Modifying script to run for all the sub-directories under a folder
### 0.3.2       20/03/2023   Praneet Kulkarni            Modifying script to extract table name along with the database name
### 0.3.3       20/03/2023   Praneet Kulkarni            Modifying script to get streamname by looking into CBMEXT/CBMODS.param file
### 0.3.4       30/03/2023   Praneet Kulkarni            Improved Performance of Code by
###                                                         1. Moving file creation to main module
###                                                         2. changed for condition in the main program to enable to scan at folder level 
### 0.3.5       11/04/2023   Praneet Kulkarni            Modified code to check only on tablename for the scripts located in unix folder
 ###                                                  2. changed for condition in the main program to enable to scan at folder level
import io
import os
import re

def remove_special_chars(input_string):
    last_char = input_string[-1]
    if re.match(r'[^a-zA-Z0-9_#$]',  last_char):
        return input_string[:-1]
    return input_string

def schemalookup(AbsPathFileName,FileName,subdir) :
    my_non_ods_file = open("U:\Praneet\python\sqlcodeinput\TerdataFullList_of_table.txt", "r")
    data_non_ods = my_non_ods_file.read().splitlines()
    StreamNameFound = ''
 
    

     # this is required on next run of the program the file is set to empty


   #Reading Paramter file which would be used in the program to find out stream name of a given table name
    StreamFileOpen = open("U:\Praneet\python\sqlcodeinput\\" + str(parametername) + ".param", "r")
    StreamFileInLines = StreamFileOpen.read().split('\n')


   
    print('FileName : ' +str(AbsPathFileName))
      
    
    MatchFound = 'N'

    if FileName.endswith(".sql"): # checks only file that ends with .sql
        
        #print(FileName)
        repotablename = FileName.rsplit(".", maxsplit=1)[0]  # gives the table name from the file name in github.
        #print("reportablename : " +str(repotablename))
        # Slicing the parameter file based on it's pattern further in order to match the table name coming from git hub.
        for i in range(len(StreamFileInLines)):
            linessubsplit =StreamFileInLines[i].split("|")
            for eachitem in range(len(linessubsplit)):
               # print("linessubsplit : " +linessubsplit[eachitem])
                if linessubsplit[eachitem] == repotablename and MatchFound == 'N':
                    StreamNameFoundTableName = linessubsplit
                    StreamNameFound = str(StreamNameFoundTableName)[1:(len(str(StreamNameFoundTableName))-1)]
                    MatchFound = 'Y'


                         
                elif MatchFound == 'N':
                    StreamNameFound = '  UNK ,UNK,UNK '
    if FileName.endswith(".log"):
         repotablename = FileName.rsplit(".", maxsplit=3)[0]

            ##### START Pasing inside SQL FIle ####
            
    my_file = open(AbsPathFileName, "r",encoding="latin1")   # encode is required as the files in windows may consists unicde format
    data = my_file.read().split()
    #print(data)
    #datastrip =  [x.replace(' ','').replace(';','') .replace(')','')for x in data]  # this is to remove any spaces between  schemaname.tablename e.g PVTECH. abc will be stripped to PVTECH.abc. this is to align data  to reference look up file

    datastrip =  [remove_special_chars(x) for x in data]



    for item in data_non_ods:
        #print("item  " + item)
        #print("Table Name " +subdir+'.'+ repotablename)
        ObjectName =  subdir+','+ repotablename

        if item in datastrip and not(item.endswith(subdir+'.'+repotablename)):  # Checking if word from file exists in the databse list
            #print("Yes contains the list  "+str(item) +' : ' +str(filepath) )
             ReferencetoNonODSSchemalist.write(str(ObjectName) + ', '+str(item).replace('.',',') +' , ' +  str(StreamNameFound)[1:(len(str(StreamNameFound))-1)]+'\n')

             
            ##### END Pasing inside SQL FIle ####
        
   



directory = r'U:\Praneet\python\sqlcodeinput\ODS\BteqLogLatest'
parametername = 'CBMEXT'
FileName = 'BTEQ'

outputfilename =  'U:\Praneet\python\output_test\CBMODS\MAR\\'+str(FileName)+'_Object_Dependency_17JUL.csv'
ReferencetoNonODSSchemalist = open (outputfilename, "a")
ReferencetoNonODSSchemalist.truncate(0)
ReferencetoNonODSSchemalist.write('DatabaseName ,ObjectName ,ObjRefDatabase,ObjRef ,STREAMNAME_FROM_PARAM FILE,OBJ_TYPE_FROM_PARAM ,OBJ_NAME_FROM_PARAM '+'\n')

i=0

for root, dirs, files in os.walk(directory):
    subdir = root.rsplit("\\",maxsplit=2)[2]

    ##     outputfilename =  'U:\Praneet\python\output_test\CBMODS\MAR\\'+str(subdir)+'_Referenceto_NonODS_Schemalist.csv'
    ##     ReferencetoNonODSSchemalist = open (outputfilename, "a")
    ##    ReferencetoNonODSSchemalist.truncate(0)
    ##    ReferencetoNonODSSchemalist.write('ObjectName ,ObjectReferred ,STREAMNAME_FROM_PARAM ,OBJ_TYPE_FROM_PARAM ,OBJ_NAME_FROM_PARAM  , COMMENTS '+'\n')

    for FileName in files :
        AbsPathFileName = os.path.join(root, FileName)
##        print('ListofFiles :' + str(files))
##        print('files :' + str(FileName))
##        print('dirs :' + str(dirs))
##        print('root :' + str(root))
##        ReferencetoNonODSSchemalist.write(str(FileName) +'\n')
##        subdir = AbsPathFileName.rsplit("\\",maxsplit=2)[1]
##        
##        
##        
        schemalookup(AbsPathFileName,FileName,subdir)
        i+=1
##        print('Total number of files scanned is : '+str(i))
ReferencetoNonODSSchemalist.write('Total number of files scanned in the folder '+str(subdir) +'  , '+str(i))
ReferencetoNonODSSchemalist.close()
        
##        print('subdir :' + str(subdir))
    
                        

