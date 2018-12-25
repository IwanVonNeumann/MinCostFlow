import numpy as np

from math import inf

from algorithm import find_min_cost_flow, calc_flow_cost, calc_flow_value
from logs import log_results

Cap = np.array([
    [0, 2, 2, 0],
    [0, 0, 3, 2],
    [0, 0, 0, 2],
    [0, 0, 0, 0]
])

Cost = np.array([
    [inf, 10, 20, inf],
    [inf, inf, 1, 10],
    [inf, inf, inf, 5],
    [inf, inf, inf, inf]
])

Flow = find_min_cost_flow(Cap, Cost, target_flow_value=3, log=True)
flow_value = calc_flow_value(Flow)
total_cost = calc_flow_cost(Flow, Cost)

log_results(Flow, flow_value, total_cost)
