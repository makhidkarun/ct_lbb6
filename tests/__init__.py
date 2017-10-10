'''ct_lbb6'''

import logging
LOGGER = logging.getLogger(__name__)
logging.basicConfig(
    # format='%(asctime)-15s %(name)s %(funcName)s(): %(message)s',
    format='%(relativeCreated)d %(name)s %(funcName)s(): %(message)s',
    level=logging.DEBUG
)
