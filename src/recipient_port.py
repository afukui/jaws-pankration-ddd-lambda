from injector import inject
from recipient import Recipient
from i_recipient_port import IRecipientPort
from i_recipient_adapter import IRecipientAdapter

class RecipientPort(IRecipientPort):

    @inject
    def __init__(self, adapter:IRecipientAdapter):
       self.__adapter = adapter

    def recipient_by_id(self, recipient_id:str) -> Recipient:
        return self.__adapter.load(recipient_id)
    
    def add_reservation(self, recipient:Recipient) -> bool:
        return self.__adapter.save(recipient)
