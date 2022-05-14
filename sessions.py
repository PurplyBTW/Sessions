import os
import sys
import random
import datetime
filename = "sessions"

def useLogs():
  if os.path.exists('logs.txt'):
    sys.exit(f"{datetime.datetime.now()} - 'logs.txt' file already created. Delete command now. This could cause: Loss of logged information.")
  else:
    with open(f"logs.txt", "w") as f:
      f.write(f"{datetime.datetime.now()} - Created logs using Sessions. Thanks for Using Sessions. Delete this if you want." + '\n')

def getSessionData(searchType, searchData, searchResultNumber=False, returnLine=False):
  Found = False
  #Search Types: ID, Name, Data
  #Example: getSessionData('ID', '1298', False)
  searchNum = 0
  with open(f"{filename}.txt", "r") as f:
    lines = f.readlines()
    cline = 0
    for line in lines:
      cline += 1
      searchNum += 1
      foundData = line.rstrip()
      progress = foundData.split('|')
      foundValue = progress[2]
      foundID = progress[0]
      foundName = progress[1]
      if searchType.lower() == 'id':
        try:
          searchData = int(searchData)
        except:
          return "ValueError: invalid literal for 'ID'"
      else:
        searchData = str(searchData)
        foundData = str(foundData)
        foundData = foundData.lower()
      #id
      if searchType.lower() == 'id':
        if str(searchData) in foundID:
          ConvertedData = foundData.split('|')
          if searchNum == searchResultNumber:
            Found = True
            ConvertedData = foundData.split('|')
          elif searchResultNumber == False:
            Found = True
            ConvertedData = foundData.split('|')
          else:
            Found = False
      #Data Value
      if searchType.lower() == 'data':
        if searchData.lower() in foundValue.lower():
          ConvertedData = foundData.split('|')
          if searchNum == searchResultNumber:
            Found = True
            ConvertedData = foundData.split('|')
          elif searchResultNumber == False:
            Found = True
            ConvertedData = foundData.split('|')
          else:
            Found = False
      #Name
      if searchType.lower() == 'name':
        if searchData.lower() in foundName.lower():
          ConvertedData = foundData.split('|')
          if searchNum == searchResultNumber:
            Found = True
            ConvertedData = foundData.split('|')
          elif searchResultNumber == False:
            Found = True
            ConvertedData = foundData.split('|')
          else:
            Found = False
    if Found:
      if os.path.exists('logs.txt'):
        with open(f"logs.txt", "a") as f:
          f.write(f'{datetime.datetime.now()} - data request for id {foundID}. Req Array: {ConvertedData}' + '\n')
      if returnLine:
        arr = [cline, lines]
        return arr
      else:
        return ConvertedData
    else:
      if os.path.exists('logs.txt'):
        with open(f"logs.txt", "a") as f:
          f.write(f'{datetime.datetime.now()} - data request for id of undefined failed. Req Array: undefined, returned: false' + '\n')
      
      return False

def removeSession(searchType, searchData):
  result = getSessionData(searchType, searchData, returnLine=True)
  list_of_lines = []
  print(result[0])
  if result == False:
    sys.exit("Session requested to remove doesn't exist. This can be avoided by changing the arguments or checking the sessions list (sessions.txt)")
  else:
    if os.path.exists(f'{filename}.txt'):
      with open(f'{filename}.txt', 'r') as f:
        list_of_lines = f.readlines()
        f.close()

      with open(f"{filename}.txt", "r+") as f:
        d = f.readlines()
        f.seek(0)
        for i in d:
          if i == int(result[0]):
            f.write('')
        f.truncate()

def createSessionFile():
  if os.path.exists('logs.txt'):
    with open(f"logs.txt", "a") as f:
      f.write(f'{datetime.datetime.now()} - Created session file.' + '\n')
  with open(f"{filename}.txt", "w") as f:
    f.write("0001|ThankUForUsingSessions|DeleteMe")
    f.close()

def addSession(sessionName, sessionData):
  sessionID = random.randint(1000, 999999)
  with open(f"{filename}.txt", "r") as f:
    if sessionID in f:
      addSession(sessionName, sessionData)
  with open(f"{filename}.txt", "a") as f:
    if '|' in sessionName:
      sessionName = str(sessionName)
      sessionName = sessionName.replace('|', '')

    if os.path.exists('logs.txt'):
      with open(f"logs.txt", "a") as f2:
        f2.write(f'{datetime.datetime.now()} - Created session. Id: {sessionID}, Name: {sessionName}, Value:{sessionData}' + '\n')
        f2.close()
    
    f.write(f'{sessionID}|{sessionName}|{sessionData}' + '\n')
    f.close()
