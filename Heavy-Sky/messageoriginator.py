import os
from flight import Flight
from datetime import datetime

class MessageOriginator:
  
  @classmethod
  def OriginateMessage(self, flights: list) -> str:
    if (len(flights) == 0):
      return self.__originate_nothing_found_msg()
    else:
      return self.__originate_something_found_msg(flights)
    
  @classmethod
  def __originate_nothing_found_msg(self) -> str:
    return f"Hey Biagio!\nToday we haven't found any deal for you!"
  
  @classmethod
  def __originate_something_found_msg(self, flights: list) -> str:
    date_format  = os.environ.get('FLIGHT_DATE_FORMAT')
    introduction = f"Hey Biagio!\nToday we have found {len(flights)} deals for you!"
    
    details_intro  = "The most convenient option is:"
    details_leave  = f"Leaving from: {flights[0].DepartureCity()} {flights[0].DepartureIATA()} at {flights[0].LocalDeparture().strftime(date_format)}"
    details_arrive = f"Arriving at: {flights[0].ArrivalCity()} {flights[0].ArrivalIATA()} at {flights[0].LocalArrival().strftime(date_format)}"
    details_price  = f"The flight costs {flights[0].Price()} {flights[0].Currency()}."
    details_all    = f"{details_intro}\n{details_leave}\n{details_arrive}\n{details_price}"
    
    return f"{introduction}\n{details_all}"