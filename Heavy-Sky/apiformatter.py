from flight import Flight
from datetime import datetime

class ApiFormatter:
  
  @classmethod
  def FormatData(self, currency: str, raw_data: dict) -> Flight:
    return Flight(
      price    = float(raw_data["price"]),
      currency = currency,
      departure_city = raw_data["cityFrom"],
      departure_IATA = raw_data["flyFrom"],
      arrival_city = raw_data["cityTo"],
      arrival_IATA = raw_data["flyTo"],
      local_departure = self.__format_date(raw_data["local_departure"]),
      local_arrival   = self.__format_date(raw_data["local_arrival"]),
      has_airport_change = raw_data["has_airport_change"]
    )

  @classmethod
  def __format_date(self, raw_date: str) -> datetime:
    date = raw_date.split("T")[0].split("-")
    time = raw_date.split("T")[1].split(":")
    return datetime(
      year   = int(date[0]),
      month  = int(date[1]),
      day    = int(date[2]),
      hour   = int(time[0]),
      minute = int(time[1])
    )