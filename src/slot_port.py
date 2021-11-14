from injector import inject
from slot import Slot
from i_slot_port import ISlotPort
from i_slot_adapter import ISlotAdapter

class SlotPort(ISlotPort):
    @inject
    def __init__(self, adapter:ISlotAdapter):
        self.__adapter = adapter

    def slot_by_id(self, slot_id:str) -> Slot:
        return self.__adapter.load(slot_id)
