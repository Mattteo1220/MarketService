from Stock import Stock
from IOController import IOController
from StockRepository import StockRepository
import random


class StockModel(object):
  def __init__(self):
    self.IncomingFile = None
    self.IOController = IOController()
    self.StockRepository = StockRepository()
    self.Stock = Stock()
    
  def CountSimpleMovingAverage(self, low, high):
    countResult = None
    countResult = self.StockRepository.CountSimpleMovingAverage(low, high)
    
    return countResult
  
  def GetDocumentsByIndustry(self, industry):
    readResult = None
    readResult = self.StockRepository.GetDocumentsByIndustry(industry)
    
    return readResult
  
  def GetSharesOutstandingBySector(self, sector):
    _readResult = None
    _readResult = self.StockRepository.GetSharesOustandingPerSector(sector)
    
    return _readResult
  
  def GetByTicker(self, ticker):
    _readResult = None
    _readResult = self.StockRepository.GetByTicker(ticker)
    
    return _readResult
  
  def GetTopFivePerformingCompanies(self):
    _readResult = None
    
    _readResult = self.StockRepository.GetTopFivePerformingCompanies()
    
    return _readResult
    
  def Create(self, isTest):
    createResult = None
    stock = self.Stock.Create(isTest)
    
    try:
      self.IOController.Write(stock)
    except Exception as exception:
      raise exception()
    
    jsonResult = self.IOController.Read(self.IOController.Incoming)
    
    stocks = []
    #map jsonResult to a stock object
    stockObject = self.Stock.MapToObject(jsonResult)
          
    #append stockObject to Stocks
    stocks.append(stockObject)
      
    #Map to Database entity and Save
    for stock in stocks:
      stockDict = self.Stock.MapToDatabaseEntity(stockObject)
      createResult = self.StockRepository.Add(stockDict)
      
    return createResult
      
  def UpdateVolume(self, ticker, newValue):
    results = None
    if(newValue < 0):
      raise Error("Value must be greater than 0")
      
    if(not ticker):
      raise Error("No ticker provided")
      
    print("Updating Volume value...")
    try:
      results = self.StockRepository.GetByTicker(ticker)
    except Exception as exception:
      raise exception("Failed to retrieve documents by Ticker: {ticker}".format(ticker = ticker))
    
    for result in results:
      stock = self.Stock.MapToObject(result)
      stock.Volume = newValue
      stockDict = self.Stock.MapToDatabaseEntity(stock)
      
      updateResult = self.StockRepository.UpdateVolume(ticker, stockDict)
    
    return updateResult
  
  def DeleteStock(self, ticker):
    _deleteResult = None
    if(not ticker):
      raise Error("Ticker not provided")
    
    _deleteResult = self.StockRepository.DeleteByTicker(ticker)
    return _deleteResult
  
  def CleanupIncomingDirectory(self):
    self.IOController.RemoveAll()
  
  
  
  
#Use below for testing repository  
  
#stockModel = StockModel()
#createResult = stockModel.Create(True)
#updateResult = stockModel.UpdateVolume("T", round(random.random(), 3))
#deleteResult = stockModel.DeleteStock("T")
#countResult = stockModel.CountSimpleMovingAverage(0.02, 0.20)
#getIndustryResult = stockModel.GetDocumentsByIndustry("Aluminum")
#getSharesResult = stockModel.GetSharesOutstandingBySector("Healthcare")
#getTopFive = stockModel.GetTopFivePerformingCompanies()

#print(createResult)
#print(updateResult)
#print(deleteResult)
#print("NumDocuments: {count}".format(count = countResult))
#for obj in getIndustryResult:
#  print(obj)
#print(getSharesResult)
#for obj in getTopFive:
# print(obj)
