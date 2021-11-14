import pytest
import sys
from injector import Injector, Module
from datetime import datetime

sys.path.append("./src/")

from i_slot_adapter import ISlotAdapter
from slot_port import SlotPort
from slot import Slot

slot_id = "1"
reservation_date = datetime(2021,12,20, 9, 0, 0)
location = "Tokyo"


class DummySlotAdapter(ISlotAdapter):
    def load(self, slot_id:str) -> Slot:
        return Slot(slot_id, reservation_date, location)


class DummyModule(Module):
    def configure(self, binder):
        binder.bind(SlotPort, to=SlotPort(DummySlotAdapter()))


@pytest.fixture()
def fixture_slot_port():
    injector = Injector([DummyModule])
    slot_port = injector.get(SlotPort)
    return slot_port


def test_recipient_port_recipient_by_id(fixture_slot_port):
    target = fixture_slot_port
    slot_id = "1"
    slot = target.slot_by_id(slot_id)
    assert slot != None
    assert reservation_date == slot.reservation_date
    assert location == slot.location

