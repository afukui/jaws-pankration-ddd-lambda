from injector import Injector, Module
from ddb_recipient_adapter import DDBRecipientAdapter
from ddb_slot_adapter import DDBSlotAdapter
from request_port import RequestPort
from slot_port import SlotPort
from recipient_port import RecipientPort
from reservation_service import ReservationService

class RequestPortModule(Module):
    def configure(self, binder):
        binder.bind(ReservationService, to=ReservationService(
            RecipientPort(DDBRecipientAdapter()), SlotPort(DDBSlotAdapter())))

def main():
    injector = Injector([RequestPortModule])
    request_port = injector.get(RequestPort)
    status = request_port.make_reservation("1", "1")
    print(f"status_code: {status.status_code}, message: {status.message}")

if __name__ == "__main__":
    main()
