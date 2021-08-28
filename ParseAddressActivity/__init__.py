# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging

from scourgify import normalize_address_record
from scourgify.exceptions import AddressNormalizationError


def main(address: str) -> dict:
    try:
        normalized_address = normalize_address_record(address)
        result = {
            "success": True,
            "address_text": address,
            "normalized_address": normalized_address,
        }

    except AddressNormalizationError as e:
        result = {"success": False, "address_text": address, "error": f"{e.TITLE}: {e.MESSAGE}"}

        logging.exception(e)

    return result


if __name__ == "__main__":

    # set logging format - personal preference
    log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # call main function

    main()
