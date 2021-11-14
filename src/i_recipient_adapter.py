from abc import ABCMeta, abstractmethod
from recipient import Recipient

class IRecipientAdapter(metaclass=ABCMeta):
    
    @abstractmethod
    def load(self, recipient_id:str) -> Recipient:
        raise NotImplementedError()

    @abstractmethod
    def save(self, recipient:Recipient) -> bool:
        raise NotImplementedError()
