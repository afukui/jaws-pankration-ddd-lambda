from abc import ABCMeta, abstractmethod
from slot import Slot

class ISlotPort(metaclass=ABCMeta):

    @abstractmethod
    def slot_by_id(self, slot_id:str) -> Slot:
        raise NotImplementedError()
