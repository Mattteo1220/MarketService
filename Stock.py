import json
from bson import json_util
import random
import datetime


class Stock(object):
  def __init__(self):
    self._id = None 
    self.Ticker = None
    self.ProfitMargin = None 
    self.InstitutionalOwnership = None 
    self.EPSGrowthPastFiveYears = None 
    self.TotalDebtOrEquity = None 
    self.CurrentRatio = None
    self.ReturnOnAssets = None
    self.Sector = None 
    self.PS = None 
    self.ChangeFromOpen = None 
    self.PerformanceYTD = None
    self.PerformanceWEEK = None 
    self.QuickRatio = None
    self.InsiderTransactions = None 
    self.PB = None
    self.EPSGrowthQuarterOverQuarter = None
    self.PayoutRatio = None
    self.PerformanceQUARTER = None
    self.ForwardPE = None
    self.PE = None
    self.TwoHundredDaySimpleMovingAverage = None
    self.SharesOutstanding = None
    self.EarningsDate = None
    self.FiftyTwoWeekHigh = None
    self.PCash = None 
    self.Change = None
    self.AnalystRecom = None 
    self.VolatilityWEEK = None 
    self.Country = None
    self.ReturnOnEquity = None
    self.FiftyDayLow = None 
    self.Price = None 
    self.FiftyDayHigh = None
    self.ReturnOnInvestment = None
    self.SharesFloat = None 
    self.DividendYield = None
    self.EPSGrowthNextFiveYears = None 
    self.Industry = None 
    self.Beta = None
    self.SalesGrowthQuarterOverQuarter = None
    self.OperatingMargin = None 
    self.EPSttm = None
    self.PEG = None 
    self.FloatShort = None
    self.FiftyTwoWeekLow = None
    self.AverageTrueRange = None
    self.EPSGrowthNextYear = None
    self.SalesGrowthPastFiveYears = None
    self.Company = None
    self.Gap = None
    self.RelativeVolume = None
    self.VolatilityMONTH = None
    self.MarketCap = None
    self.Volume = None
    self.GrossMargin = None 
    self.ShortRatio = None
    self.PerformanceHALFYEAR = None
    self.RelativeStrengthIndex14 = None
    self.InsiderOwnership = None 
    self.TwentyDaySimpleMovingAverage = None
    self.PerformanceMONTH = None 
    self.PFreeCashFlow = None 
    self.InstitutionalTransactions = None
    self.PerformanceYEAR = None
    self.LTDebtEquity = None
    self.AverageVolume = None
    self.EPSGrowthThisYear = None
    self.FiftyDaySimpleMovingAverage = None
    
  def MapToObject(self, jsonResult):
    self._id = self.ValidateJsonKey(jsonResult, "_id")
    self.Ticker = self.ValidateJsonKey(jsonResult, "Ticker")
    self.ProfitMargin = self.ValidateJsonKey(jsonResult, "Profit Margin")
    self.InstitutionalOwnership = self.ValidateJsonKey(jsonResult, "Institutional Ownership")
    self.EPSGrowthPastFiveYears = self.ValidateJsonKey(jsonResult, "EPS growth past 5 years")
    self.TotalDebtOrEquity = self.ValidateJsonKey(jsonResult, "Total Debt/Equity")
    self.CurrentRatio = self.ValidateJsonKey(jsonResult, "Current Ratio")
    self.ReturnOnAssets = self.ValidateJsonKey(jsonResult, "Return on Assets")
    self.Sector = self.ValidateJsonKey(jsonResult, "Sector")
    self.PS = self.ValidateJsonKey(jsonResult, "P/S")
    self.ChangeFromOpen = self.ValidateJsonKey(jsonResult, "Change from Open")
    self.PerformanceYTD = self.ValidateJsonKey(jsonResult, "Performance (YTD)")
    self.PerformanceWEEK = self.ValidateJsonKey(jsonResult, "Performance (Week)")
    self.QuickRatio = self.ValidateJsonKey(jsonResult, "Quick Ratio")
    self.InsiderTransactions = self.ValidateJsonKey(jsonResult, "Insider Transactions")
    self.PB = self.ValidateJsonKey(jsonResult, "P/B")
    self.EPSGrowthQuarterOverQuarter = self.ValidateJsonKey(jsonResult, "EPS growth quarter over quarter")
    self.PayoutRatio = self.ValidateJsonKey(jsonResult, "Payout Ratio")
    self.PerformanceQUARTER = self.ValidateJsonKey(jsonResult, "Performance (Quarter)")
    self.ForwardPE = self.ValidateJsonKey(jsonResult, "Forward P/E")
    self.PE = self.ValidateJsonKey(jsonResult, "P/E")
    self.TwoHundredDaySimpleMovingAverage = self.ValidateJsonKey(jsonResult, "200-Day Simple Moving Average")
    self.SharesOutstanding = self.ValidateJsonKey(jsonResult, "Shares Outstanding")
    self.EarningsDate = self.ValidateJsonKey(jsonResult, "Earnings Date")
    self.FiftyTwoWeekHigh = self.ValidateJsonKey(jsonResult, "52-Week High")
    self.PCash = self.ValidateJsonKey(jsonResult, "P/Cash")
    self.Change = self.ValidateJsonKey(jsonResult, "Change")
    self.AnalystRecom = self.ValidateJsonKey(jsonResult, "Analyst Recom")
    self.VolatilityWEEK = self.ValidateJsonKey(jsonResult, "Volatility (Week)")
    self.Country = self.ValidateJsonKey(jsonResult, "Country")
    self.ReturnOnEquity = self.ValidateJsonKey(jsonResult, "Return on Equity")
    self.FiftyDayLow = self.ValidateJsonKey(jsonResult, "50-Day Low")
    self.Price = self.ValidateJsonKey(jsonResult, "50-Day Low")
    self.FiftyDayHigh = self.ValidateJsonKey(jsonResult, "50-Day High")
    self.ReturnOnInvestment = self.ValidateJsonKey(jsonResult, "Return on Investment")
    self.SharesFloat = self.ValidateJsonKey(jsonResult, "Shares Float")
    self.DividendYield = self.ValidateJsonKey(jsonResult, "Dividend Yield")
    self.EPSGrowthNextFiveYears = self.ValidateJsonKey(jsonResult, "EPS growth next 5 years")
    self.Industry = self.ValidateJsonKey(jsonResult, "Industry")
    self.Beta = self.ValidateJsonKey(jsonResult, "Beta")
    self.SalesGrowthQuarterOverQuarter = self.ValidateJsonKey(jsonResult, "Sales growth quarter over quarter")
    self.OperatingMargin = self.ValidateJsonKey(jsonResult, "Operating Margin")
    self.EPSttm = self.ValidateJsonKey(jsonResult, "EPS (ttm)")
    self.PEG = self.ValidateJsonKey(jsonResult, "PEG")
    self.FloatShort = self.ValidateJsonKey(jsonResult, "Float Short")
    self.FiftyTwoWeekLow = self.ValidateJsonKey(jsonResult, "52-Week Low")
    self.AverageTrueRange = self.ValidateJsonKey(jsonResult, "Average True Range")
    self.EPSGrowthNextYear = self.ValidateJsonKey(jsonResult, "EPS growth next year")
    self.SalesGrowthPastFiveYears = self.ValidateJsonKey(jsonResult, "Sales growth past 5 years")
    self.Company = self.ValidateJsonKey(jsonResult, "Company")
    self.Gap = self.ValidateJsonKey(jsonResult, "Gap")
    self.RelativeVolume = self.ValidateJsonKey(jsonResult, "Relative Volume")
    self.VolatilityMONTH = self.ValidateJsonKey(jsonResult, "Volatility (Month)")
    self.MarketCap = self.ValidateJsonKey(jsonResult, "Market Cap")
    self.Volume = self.ValidateJsonKey(jsonResult, "Volume")
    self.GrossMargin = self.ValidateJsonKey(jsonResult, "Gross Margin")
    self.ShortRatio = self.ValidateJsonKey(jsonResult, "Short Ratio")
    self.PerformanceHALFYEAR = self.ValidateJsonKey(jsonResult, "Performance (Half Year)")
    self.RelativeStrengthIndex14 = self.ValidateJsonKey(jsonResult, "Relative Strength Index (14)")
    self.InsiderOwnership = self.ValidateJsonKey(jsonResult, "Insider Ownership")
    self.TwentyDaySimpleMovingAverage = self.ValidateJsonKey(jsonResult, "20-Day Simple Moving Average")
    self.PerformanceMONTH = self.ValidateJsonKey(jsonResult, "Performance (Month)")
    self.PFreeCashFlow = self.ValidateJsonKey(jsonResult, "P/Free Cash Flow")
    self.InsiderTransactions = self.ValidateJsonKey(jsonResult, "Institutional Transactions")
    self.PerformanceYEAR = self.ValidateJsonKey(jsonResult, "Performance (Year)")
    self.LTDebtEquity = self.ValidateJsonKey(jsonResult, "LT Debt/Equity")
    self.AverageVolume = self.ValidateJsonKey(jsonResult, "Average Volume")
    self.EPSGrowthThisYear = self.ValidateJsonKey(jsonResult, "EPS growth this year")
    self.FiftyDaySimpleMovingAverage = self.ValidateJsonKey(jsonResult, "50-Day Simple Moving Average")

    return self
    
  def MapToDatabaseEntity(self, stock):
    return {
        "_id" : stock._id,
        "Ticker" : stock.Ticker,
        "Profit Margin" : stock.ProfitMargin,
        "Institutional Ownership" : stock.InstitutionalOwnership,
        "EPS growth past 5 years" : stock.EPSGrowthPastFiveYears,
        "Total Debt/Equity" : stock.TotalDebtOrEquity,
        "Current Ratio" : stock.CurrentRatio,
        "Return on Assets" : stock.ReturnOnAssets,
        "Sector" : stock.Sector,
        "P/S" : stock.PS,
        "Change from Open" : stock.ChangeFromOpen,
        "Performance (YTD)" : stock.PerformanceYTD,
        "Performance (Week)" : stock.PerformanceWEEK,
        "Quick Ratio" : stock.QuickRatio,
        "Insider Transactions" : stock.InsiderTransactions,
        "P/B" : stock.PB,
        "EPS growth quarter over quarter" : stock.EPSGrowthQuarterOverQuarter,
        "Payout Ratio" : stock.PayoutRatio,
        "Performance (Quarter)" : stock.PerformanceQUARTER,
        "Forward P/E" : stock.ForwardPE,
        "P/E" : stock.PE,
        "200-Day Simple Moving Average" : stock.TwoHundredDaySimpleMovingAverage,
        "Shares Outstanding" : stock.SharesOutstanding,
        "Earnings Date" : json.dumps(stock.EarningsDate,default=json_util.default),
        "52-Week High" : stock.FiftyTwoWeekHigh,
        "P/Cash" : stock.PCash,
        "Change" : stock.Change,
        "Analyst Recom" : stock.AnalystRecom,
		    "Volatility (Week)" : stock.VolatilityWEEK,
        "Country" : stock.Country,
        "Return on Equity" : stock.ReturnOnEquity,
        "50-Day Low" : stock.FiftyDayLow,
        "Price" : stock.Price,
        "50-Day High" : stock.FiftyDayHigh,
        "Return on Investment" : stock.ReturnOnInvestment,
        "Shares Float" : stock.SharesFloat,
        "Dividend Yield" : stock.DividendYield,
        "EPS growth next 5 years" : stock.EPSGrowthNextFiveYears,
        "Industry" : stock.Industry,
        "Beta" : stock.Beta,
        "Sales growth quarter over quarter" : stock.SalesGrowthQuarterOverQuarter,
        "Operating Margin" : stock.OperatingMargin,
        "EPS (ttm)" : stock.EPSttm,
        "PEG" : stock.PEG,
        "Float Short" : stock.FloatShort,
        "52-Week Low" : stock.FiftyTwoWeekLow,
        "Average True Range" : stock.AverageTrueRange,
        "EPS growth next year" : stock.EPSGrowthNextYear,
        "Sales growth past 5 years" : stock.SalesGrowthPastFiveYears,
        "Company" : stock.Company,
        "Gap" : stock.Gap,
        "Relative Volume" : stock.RelativeVolume,
        "Volatility (Month)" : stock.VolatilityMONTH,
        "Market Cap" : stock.MarketCap,
        "Volume" : stock.Volume,
        "Gross Margin" : stock.GrossMargin,
        "Short Ratio" : stock.ShortRatio,
        "Performance (Half Year)" : stock.PerformanceHALFYEAR,
        "Relative Strength Index (14)" : stock.RelativeStrengthIndex14,
        "Insider Ownership" : stock.InsiderOwnership,
        "20-Day Simple Moving Average" : stock.TwentyDaySimpleMovingAverage,
        "Performance (Month)" : stock.PerformanceMONTH,
        "P/Free Cash Flow" : stock.PFreeCashFlow,
        "Institutional Transactions" : stock.InstitutionalTransactions,
        "Performance (Year)" : stock.PerformanceYEAR,
        "LT Debt/Equity" : stock.LTDebtEquity,
        "Average Volume" : stock.AverageVolume,
        "EPS growth this year" : stock.EPSGrowthThisYear,
        "50-Day Simple Moving Average" : stock.FiftyDaySimpleMovingAverage
    }
  
  def Create(self, isTest):
    self._id = "Test{id}".format(id = random.randint(111111111,999999999))
    self.Ticker = ("T" if isTest else "A")
    self.ProfitMargin = round(random.random(), 3)
    self.EPSGrowthPastFiveYears = round(random.random(), 3)
    self.TotalDebtOrEquity = round(random.random(), 3)
    self.CurrentRatio = round(random.random(), 3)
    self.ReturnOnAssets = round(random.random(), 3)
    self.Sector = "Health Care"
    self.PS = round(random.random(), 3)
    self.ChangeFromOpen = round(random.random(), 3)
    self.PerformanceYTD = round(random.random(), 3)
    self.PerformanceWEEK = round(random.random(), 3)
    self.QuickRatio = round(random.random(), 3)
    self.InsiderTransactions = round(random.random(), 3)
    self.PB = round(random.random(), 3)
    self.EPSGrowthQuarterOverQuarter = round(random.random(), 3)
    self.PayoutRatio = round(random.random(), 3)
    self.PerformanceQUARTER = round(random.random(), 3)
    self.ForwardPE = round(random.random(), 3)
    self.PE = round(random.random(), 3)
    self.TwoHundredDaySimpleMovingAverage = round(random.random(), 3)
    self.SharesOutstanding = round(random.random(), 3)
    self.EarningsDate = datetime.datetime.now()
    self.FiftyTwoWeekHigh = round(random.random(), 3)
    self.PCash = round(random.random(), 3) 
    self.Change = round(random.random(), 3) 
    self.AnalystRecom = round(random.random(), 3)  
    self.VolatilityWEEK = round(random.random(), 3)  
    self.Country = "USA"
    self.ReturnOnEquity = round(random.random(), 3) 
    self.FiftyDayLow = round(random.random(), 3)  
    self.Price = round(random.random(), 3)  
    self.FiftyDayHigh = round(random.random(), 3) 
    self.ReturnOnInvestment = round(random.random(), 3) 
    self.SharesFloat = round(random.random(), 3)  
    self.DividendYield = round(random.random(), 3) 
    self.EPSGrowthNextFiveYears = round(random.random(), 3)  
    self.Industry = "HealthCare" 
    self.Beta = round(random.random(), 3) 
    self.SalesGrowthQuarterOverQuarter = round(random.random(), 3) 
    self.OperatingMargin = round(random.random(), 3)  
    self.EPSttm = round(random.random(), 3) 
    self.PEG = round(random.random(), 3)  
    self.FloatShort = round(random.random(), 3) 
    self.FiftyTwoWeekLow = round(random.random(), 3) 
    self.AverageTrueRange = round(random.random(), 3) 
    self.EPSGrowthNextYear = round(random.random(), 3) 
    self.SalesGrowthPastFiveYears = round(random.random(), 3) 
    self.Company = "TestHealthCare"
    self.Gap = round(random.random(), 3) 
    self.RelativeVolume = round(random.random(), 3) 
    self.VolatilityMONTH = round(random.random(), 3) 
    self.MarketCap = round(random.random(), 3) 
    self.Volume = round(random.random(), 3) 
    self.GrossMargin = round(random.random(), 3)  
    self.ShortRatio = round(random.random(), 3) 
    self.PerformanceHALFYEAR = round(random.random(), 3) 
    self.RelativeStrengthIndex14 = round(random.random(), 3) 
    self.InsiderOwnership = round(random.random(), 3)  
    self.TwentyDaySimpleMovingAverage = round(random.random(), 3) 
    self.PerformanceMONTH = round(random.random(), 3)  
    self.PFreeCashFlow = round(random.random(), 3)  
    self.InstitutionalTransactions = round(random.random(), 3) 
    self.InstitutionalOwnership = round(random.random(), 3)
    self.PerformanceYEAR = round(random.random(), 3) 
    self.LTDebtEquity = round(random.random(), 3) 
    self.AverageVolume = round(random.random(), 3) 
    self.EPSGrowthThisYear = round(random.random(), 3) 
    self.FiftyDaySimpleMovingAverage = round(random.random(), 3) 
    
    stock = self.MapToDatabaseEntity(self)
    return stock
  
  def ValidateJsonKey(self,json, key):
    if(key in json):
      return json[key]
    else:
      if(key == "Country"
        or key == "Sector"
        or key == "Industry"
        or key == "Company"):
        return "None"
      else:
        return 0.001

  
    