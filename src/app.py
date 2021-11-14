import json
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

def lambda_handler(event, context):
    '''
    API Gateway event adapter

    retrieve reservation request parameters
    ex: '{"recipient_id": "1", "slot_id":"1"}'
    '''
    body = json.loads(event['body'])
    recipient_id = body['recipient_id']
    slot_id = body['slot_id']

    injector = Injector([RequestPortModule])
    request_port = injector.get(RequestPort)
    status = request_port.make_reservation(recipient_id, slot_id)
 
    return {
        "statusCode": status.status_code,
        "body": json.dumps({
            "message": status.message
        }),
    }

