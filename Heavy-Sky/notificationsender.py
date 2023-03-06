import os
from twilio.rest import Client

class NotificationSender:
  def __init__(self) -> None:
    account_sid   = os.environ.get('TWILIO_ACCOUNT_SID')
    auth_token    = os.environ.get('TWILIO_AUTH_TOKEN')
    self.__client = Client(account_sid, auth_token)

  def SendNotification(self, msg_body: str) -> None:
    self.__client.messages.create(
      from_ = os.environ.get('SENDER_NUMBER'),
      to    = os.environ.get('RECEIVER_NUMBER'),
      body  = msg_body
    )