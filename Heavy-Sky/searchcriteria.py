import os
import json
from pathlib import Path
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

class SearchCriteriaRetriever:
  @classmethod
  def DefineSearchCriteria(self) -> SearchCriteria:
    current_directory = os.path.dirname(os.path.realpath(__file__))
    with open(file=Path(current_directory, "criterias.json"), mode="r") as file:
      data = json.load(file)

      date_from   = [int(x) for x in data["date_from"].split("/")]
      date_to     = [int(x) for x in data["date_to"].split("/")]
      return_from = [int(x) for x in data["return_from"].split("/")]
      return_to   = [int(x) for x in data["return_to"].split("/")]

      return SearchCriteria(
        fly_from    = data["fly_from"],
        fly_to      = data["fly_to"],
        date_from   = datetime(date_from[2], date_from[1], date_from[0]),
        date_to     = datetime(date_to[2], date_to[1], date_to[0]),
        return_from = datetime(return_from[2], return_from[1], date_from[0]),
        return_to   = datetime(return_to[2], return_to[1], return_to[0]),
        adults      = data["adults"],
        price_from  = data["price_from"],
        price_to    = data["price_to"]
      )