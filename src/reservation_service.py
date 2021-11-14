from injector import inject
from i_recipient_port import IRecipientPort
from i_slot_port import ISlotPort

class ReservationService:
    @inject
    def __init__(self, recipient_port:IRecipientPort, slot_port:ISlotPort):
        self.__recipient_port = recipient_port
        self.__slot_port = slot_port
    
    def add_reservation(self, recipient_id:str, slot_id:str) -> bool:
        recipient = self.__recipient_port.recipient_by_id(recipient_id)
        slot = self.__slot_port.slot_by_id(slot_id)
        print(f"recipient: {recipient.first_name}, slot date: {slot.reservation_date}")
        ret = recipient.add_reserve_slot(slot)
        if ret == True:
            ret = self.__recipient_port.add_reservation(recipient)
        return ret

