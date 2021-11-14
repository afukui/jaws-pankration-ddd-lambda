from abc import ABCMeta, abstractmethod
from recipient import Recipient

class IRecipientPort(metaclass=ABCMeta):

    @abstractmethod
    def recipient_by_id(self, recipient_id:str) -> Recipient:
        raise NotImplementedError()

    @abstractmethod
    def add_reservation(self, recipient:Recipient) -> bool:
        raise NotImplementedError()

