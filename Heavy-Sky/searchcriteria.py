from datetime import datetime

class SearchCriteria:
  def __init__(self, 
               fly_from    : str,
               fly_to      : str,
               date_from   : datetime,
               date_to     : datetime,
               return_from : datetime,
               return_to   : datetime,
               adults      : int,
               price_from  : int,
               price_to    : int
               ) -> None:
    self.__fly_from     = fly_from
    self.__fly_to       = fly_to
    self.__date_from    = date_from
    self.__date_to      = date_to
    self.__return_from  = return_from
    self.__return_to    = return_to
    self.__adults       = adults
    self.__price_from   = price_from
    self.__price_to     = price_to
  
  def FlyFrom(self)    -> str: return self.__fly_from
  def FlyTo(self)      -> str: return self.__fly_to
  def DateFrom(self)   -> datetime: return self.__date_from
  def DateTo(self)     -> datetime: return self.__date_to
  def ReturnFrom(self) -> datetime: return self.__return_from
  def ReturnTo(self)   -> datetime: return self.__return_to
  def Adults(self)     -> int: return self.__adults
  def PriceFrom(self)  -> int: return self.__price_from
  def PriceTo(self)    -> int: return self.__price_to