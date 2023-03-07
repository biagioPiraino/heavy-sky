from datetime import datetime

class Flight:
  def __init__(self,
               price   : float,
               currency: str,
               departure_city: str,
               departure_IATA: str,
               arrival_city: str,
               arrival_IATA: str,
               local_departure: datetime,
               local_arrival  : datetime,
               has_airport_change: bool) -> None:
    self.__price    = price
    self.__currency = currency
    self.__departure_city = departure_city
    self.__departure_IATA = departure_IATA
    self.__arrival_city = arrival_city
    self.__arrival_IATA = arrival_IATA
    self.__local_departure = local_departure
    self.__local_arrival   = local_arrival
    self.__has_airport_change = has_airport_change
  
  def Price(self)    -> float: return self.__price
  def Currency(self) -> str: return self.__currency
  def DepartureCity(self) -> str: return self.__departure_city
  def DepartureIATA(self) -> str: return self.__departure_IATA
  def ArrivalCity(self) -> str: return self.__arrival_city
  def ArrivalIATA(self) -> str: return self.__arrival_IATA
  def LocalDeparture(self) -> datetime: return self.__local_departure
  def LocalArrival(self)   -> datetime: return self.__local_arrival
  def HasAirportChange(self) -> bool: return self.__has_airport_change