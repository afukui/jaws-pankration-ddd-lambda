import pytest
import sys
from injector import Injector, Module
from datetime import datetime

sys.path.append("./src/")

from reservation_service import ReservationService
from i_recipient_adapter import IRecipientAdapter
from recipient_port import RecipientPort
from recipient import Recipient
from i_slot_adapter import ISlotAdapter
from slot_port import SlotPort
from slot import Slot

recipient_id = "1"
email = "fatsushi@example.com"
first_name = "Atsushi"
last_name = "Fukui"
age = 30
slot_id = "1"
reservation_date = datetime(2021,12,20, 9, 0, 0)
location = "Tokyo"


class DummyRecipientAdapter(IRecipientAdapter):
    def load(self, recipient_id:str) -> Recipient:
        return Recipient(recipient_id, email, first_name, last_name, age)

    def save(self, recipient:Recipient) -> bool:
        return True


class DummySlotAdapter(ISlotAdapter):
    def load(self, slot_id:str) -> Slot:
        return Slot(slot_id, reservation_date, location)


class DummyModule(Module):
    def configure(self, binder):
        binder.bind(ReservationService, to=ReservationService(
            RecipientPort(DummyRecipientAdapter()), SlotPort(DummySlotAdapter())))


@pytest.fixture()
def fixture_reservation_service():
    injector = Injector([DummyModule])
    reservation_service = injector.get(ReservationService)
    return reservation_service


def test_add_reservation(fixture_reservation_service):
    target = fixture_reservation_service
    recipient_id = "dummy_id"
    slot_id = "dummy_id"

    ret = target.add_reservation(recipient_id, slot_id)
    assert True == ret

