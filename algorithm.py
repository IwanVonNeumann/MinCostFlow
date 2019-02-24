import numpy as np

from math import inf

from logs import log_successful_step, log_unsuccessful_step
from shortest_path import find_shortest_path


def zero_flow(n):
    return np.zeros(shape=(n, n))


def calc_residual_capacities(Cap, Flow):
    return Cap - Flow


def build_direct_reverse_edges(Cap, Flow):
    Cap_res = calc_residual_capacities(Cap, Flow)

    direct_edges = (Cap_res > 0)
    reverse_edges = (Flow > 0).T

    return direct_edges, reverse_edges


def make_incremental_distances_graph(Cap, Flow, Cost):
    direct_edges, reverse_edges = build_direct_reverse_edges(Cap, Flow)

    G = np.full_like(Cost, fill_value=inf)
    G = np.where(direct_edges, Cost, G)
    G = np.where(reverse_edges, Cost.T * (-1), G)

    return G


def make_incremental_capacities_graph(Cap, Flow):
    direct_edges, reverse_edges = build_direct_reverse_edges(Cap, Flow)
    Cap_res = calc_residual_capacities(Cap, Flow)

    return np.where(direct_edges, Cap_res, 0) + np.where(reverse_edges, Flow.T, 0)


def choose_flow_inc(Cap, Flow, path, threshold=inf):
    G = make_incremental_capacities_graph(Cap, Flow)
    path_capacities = [G[i, j] for i, j in path]

    return min(path_capacities + [threshold])


def increment_flow(Cap, Flow, path, value):
    direct_edges, reverse_edges = build_direct_reverse_edges(Cap, Flow)

    for i, j in path:
        if direct_edges[i, j]:
            Flow[i, j] += value
        else:
            Flow[j, i] -= value

    return Flow


def find_min_cost_flow(Cap, Cost, target_flow_value, log=False):
    n, _ = Cap.shape
    flow_value = 0
    Flow = zero_flow(n)

    step_number = 0

    while flow_value != target_flow_value:
        step_number += 1

        G_inc = make_incremental_distances_graph(Cap, Flow, Cost)
        path = find_shortest_path(G_inc, source=0, target=n - 1)

        if path is None:
            if log:
                log_unsuccessful_step(step_number)
            break

        max_flow_inc = target_flow_value - flow_value
        flow_inc = choose_flow_inc(Cap, Flow, path, threshold=max_flow_inc)
        Flow = increment_flow(Cap, Flow, path, flow_inc)
        flow_value += flow_inc

        if log:
            current_cost = calc_flow_cost(Flow, Cost)
            log_successful_step(step_number, G_inc, path, flow_inc, Flow, flow_value, current_cost)

    return Flow


def calc_flow_value(Flow):
    return np.sum(Flow[0, :])


def calc_flow_cost(Flow, Cost):
    return np.sum(Flow * np.where(Cost != inf, Cost, 0))
