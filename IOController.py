import json
import datetime
import os

class IOController(object):
  def __init__(self):
    self.Incoming = "MarketService/Incoming/NewStocks_{date}.json".format(date = datetime.datetime.now())
    self.IncomingDirectory = "MarketService/Incoming"
    self.ReadMode = "r"
    self.WriteMode = "w"
    
  def Read(self, file):
    jsonResult = None
    try:
      with open(file, self.ReadMode) as reader:
        for line in reader.readlines():
          jsonResult = json.loads(line)
    
    except Exception as error:
      raise error("Error Occurred")
      
    return jsonResult
    
    
    return self.Stocks
  
  def Write(self, stock):
    try:
      with open(self.Incoming, self.WriteMode) as json_file:
        json.dump(stock, json_file)
    except Exception as exception:
      raise("Failed to write file")
      
    
  def RemoveAll(self):
    try:
      incomingFiles = os.listdir(self.IncomingDirectory)
      for incomingFile in incomingFiles:
        fullFilePath = os.path.join(self.IncomingDirectory, incomingFile)
        os.remove(fullFilePath)
    except Exception as exception:
      raise exception("failed to remove files.")