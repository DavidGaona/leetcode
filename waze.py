import logging

import WazeRouteCalculator

logger = logging.getLogger('WazeRouteCalculator.WazeRouteCalculator')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
logger.addHandler(handler)

from_address = 'Cali, Colombia'
to_address = 'Bogota, Colombia'

route = WazeRouteCalculator.WazeRouteCalculator(from_address, to_address)
route.calc_route_info()