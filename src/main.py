from typing import Any, Final

from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.typing import LambdaContext

logger = Logger()

DEFAULT_RESPONSE: Final = {"statusCode": 200}

@logger.inject_lambda_context(log_event=True)
def handle_trigger(event: dict[str, Any], context: LambdaContext):
    logger.info("Successfully done X")
    return DEFAULT_RESPONSE
