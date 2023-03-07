import os
import requests as rq
from apiformatter import ApiFormatter
from searchcriteria import SearchCriteria

class ApiRequester:
  def SearchFlight(self, search_criteria: SearchCriteria) -> list:
    # Build API call parameters and headers
    flight_params = self.__buildParameters(search_criteria)
    headers       = self.__buildHeader()
    
    # Get a response from the endpoint
    response = rq.get(
      url     = f"{os.environ.get('API_ENDPOINT_PREFIX')}/search",
      params  = flight_params,
      headers = headers)
    response.raise_for_status()
    
    # Format the data
    raw_data      = response.json()
    flight_data   = raw_data["data"]
    currency_data = raw_data["currency"]
    
    formatted_data = list()
    for data in flight_data:
      formatted_data.append(ApiFormatter.FormatData(currency=currency_data, raw_data=data))

    # Return a list of Flights
    return formatted_data

  def __buildParameters(self, search_criteria: SearchCriteria) -> dict:
    date_format = os.environ.get('DATETIME_FORMAT')
    return {
      "fly_from"    :search_criteria.FlyFrom(),
      "fly_to"      :search_criteria.FlyTo(),
      "date_from"   :search_criteria.DateFrom().strftime(date_format),
      "date_to"     :search_criteria.DateTo().strftime(date_format),
      "return_from" :search_criteria.ReturnFrom().strftime(date_format),
      "return_to"   :search_criteria.ReturnTo().strftime(date_format),
      "adults"      :search_criteria.Adults(),
      "price_from"  :search_criteria.PriceFrom(),
      "price_to"    :search_criteria.PriceTo()
    }

  def __buildHeader(self) -> dict:
    return { "apikey":os.environ.get("APY_KEY") }