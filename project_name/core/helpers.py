import logging

import phonenumbers

logger = logging.getLogger(__name__)


def format_e164_indo_phone_number(phone_number):
    try:
        parsed_phone_number = phonenumbers.parse(phone_number, "ID")
        e164_indo_phone_number = phonenumbers.format_number(
            parsed_phone_number, phonenumbers.PhoneNumberFormat.E164)
    except:
        logger.debug({
            'phone_number': phone_number,
            'formatted_phone_number': e164_indo_phone_number
        })
        return phone_number
    return e164_indo_phone_number
