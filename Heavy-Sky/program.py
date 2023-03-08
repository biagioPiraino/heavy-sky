from apirequester import ApiRequester
from messageoriginator import MessageOriginator
from notificationsender import NotificationSender
from searchcriteria import SearchCriteriaRetriever

class Program:
  @classmethod
  def RunProgram(self) -> None:
    search_criteria = SearchCriteriaRetriever.DefineSearchCriteria()
    flights = ApiRequester.SearchFlight(search_criteria)
    message = MessageOriginator.OriginateMessage(flights)
    NotificationSender().SendNotification(message)