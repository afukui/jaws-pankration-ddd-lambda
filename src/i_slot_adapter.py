from abc import ABCMeta, abstractmethod
from slot import Slot

class ISlotAdapter(metaclass=ABCMeta):

    @abstractmethod
    def load(self, slot_id:str) -> Slot:
        raise NotImplementedError()
