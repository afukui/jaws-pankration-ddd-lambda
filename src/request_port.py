from injector import inject
from reservation_service import ReservationService
from status import Status

class RequestPort:
    @inject
    def __init__(self, reservation_service:ReservationService):
        self.__reservation_service = reservation_service

    def make_reservation(self, recipient_id:str, slot_id:str) -> Status:
        status = None        
        # call domain object
        if self.__reservation_service.add_reservation(recipient_id, slot_id) == True:
            status = Status(200, "The recipient's reservation is added.")
        else:
            statsu = Status(200, "The recipient's reservation is NOT added!")
        return status
