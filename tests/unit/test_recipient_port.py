import pytest
import sys
from injector import Injector, Module

sys.path.append("./src/")

from i_recipient_adapter import IRecipientAdapter
from recipient_port import RecipientPort
from recipient import Recipient

recipient_id = "1"
email = "fatsushi@example.com"
first_name = "Atsushi"
last_name = "Fukui"
age = 30


class DummyRecipientAdapter(IRecipientAdapter):
    def load(self, recipient_id:str) -> Recipient:
        return Recipient(recipient_id, email, first_name, last_name, age)

    def save(self, recipient:Recipient) -> bool:
        return True


class DummyModule(Module):
    def configure(self, binder):
        binder.bind(RecipientPort, to=RecipientPort(DummyRecipientAdapter()))


@pytest.fixture()
def fixture_recipient_port():
    injector = Injector([DummyModule])
    recipient_port = injector.get(RecipientPort)
    return recipient_port


def test_recipient_port_recipient_by_id(fixture_recipient_port):
    target = fixture_recipient_port
    recipient_id = "dummy_number"
    recipient = target.recipient_by_id(recipient_id)
    assert recipient != None
    assert email == recipient.email
    assert first_name == recipient.first_name
    assert last_name == recipient.last_name
    assert age == recipient.age


def test_recipient_port_add_reservation_must_be_true(fixture_recipient_port):
    target = fixture_recipient_port
    ret = target.add_reservation(Recipient(recipient_id, email, first_name, last_name, age))
    assert True == ret
