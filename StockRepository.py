import json
import random
import datetime
from bson import json_util
from pymongo import MongoClient
from pprint import pprint
from IOController import IOController
from Stock import Stock

class StockRepository(object):
  def __init__(self):
    self.Connection = MongoClient('localhost', 27017)
    self.DataBase = self.Connection["Market"]
    self.StocksCollection = self.DataBase["Stocks"]
    try:
      self.Connection.server_info()
    
    except Exception as ServerError:
      raise ServerError("Failed to Connect: Check to see Mongod server is running.")
    
  def CountSimpleMovingAverage(self, low, high):
    _countResult = None
    
    try:
      _countResult = self.StocksCollection.find({"50-Day Simple Moving Average" : {"$gt" : low, "$lt" : high}})
      if(_countResult.count() <= 0):
        raise Error("Failed to find any stocks between {low} and {high}".format(low = low, high = high))
    except Exception as exception:
      raise exception("Failed to count")
      
    return ("Number of Stocks FiftyDaySimpleMovingAverage between {low} and {high} is: {count}\n".format(low=low, high=high, count=_countResult.count()))
  
  def GetDocumentsByIndustry(self, industry):
    _readResult = None
    
    try:
      _readResult = self.StocksCollection.find({"Industry" : industry})
      if(_readResult is None):
        raise error("Failed to find documents by industry: {i}".format(i = industry))
    except Exception as exception:
      raise exception("Failed to retrieve documents")
      
    print(_readResult)
    return _readResult
    
  def GetByTicker(self, ticker):
    _readResult = None
    
    try:
      _readResult = self.StocksCollection.find({"Ticker": ticker}, {"_id" : 1, "Company": 1, "Profit Margin":1})
      if(_readResult is None):
        raise Error("Failed to retrieve stocks")
    except Exception as exception:
      raise exception("Failed to get Document by Ticker: {ticker}".format(ticker = ticker))
      
    return list(_readResult)
  
  def GetSharesOustandingPerSector(self, sector):
    if(not sector):
      raise Error("No Sector Provided")
    
    _readResult = None
    query = [{"$project" : {"Sector" : 1, "Shares Outstanding" :1}},{"$match" : {"Sector": "Healthcare"}},{"$group" : {"_id" : "$Sector", "Total" : {"$sum" : "$Shares Outstanding"}}}]
    
    try:
      _readResult = self.StocksCollection.aggregate(pipeline = query)
    except Exception as exception:
      raise exception("Failed to retrieve Shares oustanding")

    return list(_readResult)
  
  def GetTopFivePerformingCompanies(self):
    _readResult = None
    
    try:
      _readResult = self.StocksCollection.find({}, {"Company" : 1,"Profit Margin" : 1}).sort([("Profit Margin", -1)]).limit(5)
    except Exception as exception:
      raise exception("Failed to get top performing stocks")
      
    return list(_readResult)
  
  def UpdateVolume(self, ticker, stock):
    _updateResult = None
    _resultString = None
    
    try:
      _updateResult = self.StocksCollection.update({"_id":stock["_id"], "Ticker" : ticker}, stock)
    except Exception as exception:
      raise exception("Failed to update stock")
      
    print(_updateResult)
    if(_updateResult["ok"] > 0):
      _resultString = "UpdateResult: Successful\n"
    else:
      _resultString = "UpdateResult: Failed\n"
    
    return _resultString
  
  def Add(self, stockDict):
    _insertResult = None
    
    try:
      _insertResult = self.StocksCollection.insert_one(stockDict)
    except Exception as exception:
      raise exception("Failed to insert stock")
      
    #Error logging
    if (_insertResult.acknowledged is False):
      _insertResult = "{InsertResult: Failed}\n"
      raise error("Failed to insert Stock Object: {id}".format(id = stockObject._id))
    else:
      _insertResult = "{InsertResult: Successful}\n"
    return _insertResult
      
  def DeleteByTicker(self, ticker):
    _deleteResults = None
    
    try:
      _deleteResults = self.StocksCollection.delete_many({"Ticker" : ticker})
    except Exception as exception:
      raise exception("Failed to delete Stocks")
      
    if(_deleteResults.deleted_count > 0):
      _deleteResults = "DeleteResult: Successful; Deleted: {count}\n".format(count = _deleteResults.deleted_count)
    else:
      _deleteResults = "DeleteResult: Failed\n"
      
    return _deleteResults
  

