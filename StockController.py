#!/usr/bin/python
import json
import datetime
from bson import json_util
import bottle
from bottle import Bottle, template, route, run, request, abort, get, post, put, delete
from StockModel import StockModel
import random

class StockController:
  def __init__(self):
    self._host = "localhost"
    self._port = 8080
    self._app = Bottle()
    
  def Initialize(self):
    if __name__ == '__main__':
      #app.run(debug=True)
      print("Host={host}".format(host=self._host))
      run(host=self._host, port=self._port)
      
  @get('/IsAlive')
  def IsAlive():
    IsAlive = True
    string = "IsAlive: {IsAlive}\n".format(IsAlive = IsAlive)
    
    return json.loads(json.dumps(string, indent=4, default=json_util.default))
  
  @get('/Ticker')
  def GetStockByTicker():
    ticker = request.query.ticker
    
    if(not ticker):
      abort(404, "Not Found")
      
    stockModel = StockModel()
    _readResult = None
    
    try:
      _readResult = stockModel.GetByTicker(ticker)
    except Exception as exception:
      raise exception("failed to retrieve stocks")
      
    return dict(data = json.loads(json.dumps(_readResult, indent=4, default=json_util.default)))
  
  @get('/Industry')
  def GetDocumentsByIndustry():
    industry = request.query.industry
    
    if(not industry):
      abort(404, "Not Found")
      
    stockModel = StockModel()
    _readResult = None
    _resultString = []
    try:
      _readResult = stockModel.GetDocumentsByIndustry(industry)
    except Exception as exception:
      raise exception("Failed to get stock")
    for result in _readResult:
      _resultString.append(json.loads(json.dumps(result, indent=4, default=json_util.default)))
    print(_resultString)
    return dict(data=_resultString)
  
  @get('/CountFiftyDaySimpleMovingAverage')
  def CountFiftyDaySimpleMovingAverage():
    low = request.query.low
    high = request.query.high
    
    if(low <= 0 or high <= low or high <= 0):
      abort(404, "Not Found")
      
    float(low)
    float(high)
    print(low)
    print(high)
    stockModel = StockModel()
    _readResult = None
    
    try:
      _readResult = stockModel.CountSimpleMovingAverage(low, high)
    except Exception as exception:
      raise exception("Failed to find Count")
      
    return json.loads(json.dumps(_readResult, indent=4, default=json_util.default))
  
  @get('/SharesBySector')
  def GetSharesPerSector():
    sector = request.query.sector
    
    print(sector)
    if(not sector):
      abort(404, "Not Found")
      
    stockModel = StockModel()
    _readResult = None
    _resultString = []
    
    try:
      _readResult = stockModel.GetSharesOutstandingBySector(sector)
    except Exception as exception:
      raise exception("Failed to retrieve documents by sector")
      
    return dict(data = json.loads(json.dumps(_readResult, indent=4, default=json_util.default)))
  
  @get('/TopFive')
  def GetTopFive():
    _readResult = None
    
    stockModel = StockModel()
    try:
      _readResult = stockModel.GetTopFivePerformingCompanies()
    except Exception as exception:
      raise exception("Failed to get top five")
    
    return dict(data = json.loads(json.dumps(_readResult, indent=4, default=json_util.default)))
  
  @post('/CreateStock')
  def CreateStock():
    isTest = request.forms.get("IsTest")
    if(not isTest):
      isTest = False
      
    stockModel = StockModel()
    resultString = stockModel.Create(isTest)
      
    return json.loads(json.dumps(resultString, indent=4, default=json_util.default))
  
  @put('/UpdateVolume')
  def UpdateVolume():
    ticker = request.forms.get("Ticker")
    volume = request.forms.get("Volume")
    _updateResult = None
    
    if(not ticker):
      abort(404, "Not Found")
      
    if(volume <= 0):
      abort(404, "Not Found")
      
    stockModel = StockModel()
    
    try:
      _updateResult = stockModel.UpdateVolume(ticker, volume)
    except Exception as exception:
      raise exception("Error Occurred")
      
    if(_updateResult is None):
      raise error("Update Failed")
  
    return json.loads(json.dumps(_updateResult, indent=4, default=json_util.default))
  
  @delete('/Delete')
  def Delete():
    ticker = request.forms.get("Ticker")
    
    if (not ticker):
      abort(404, "Not Found")
    
    _deleteResult = None
    stockModel = StockModel()
    
    try:
      _deleteResult = stockModel.DeleteStock(ticker)
    except Exception as exception:
      raise exception("Failed to delete Stock")
      
    return _deleteResult


stockController = StockController()
stockController.Initialize()
#stockController.CountFiftyDaySimpleMovingAverage(0.02, 2.0)