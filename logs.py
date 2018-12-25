def log_successful_step(step_number, G_inc, path, flow_inc, Flow, flow_value, current_cost):
    print('step', step_number)
    print('incremental:')
    print(G_inc)
    print('path:', path)
    print('flow inc value:', flow_inc)
    print('flow:')
    print(Flow)
    print('flow value:', flow_value)
    print('current cost:', current_cost)
    print('-' * 50)


def log_unsuccessful_step(step_number):
    print('step', step_number)
    print('No path found. Current flow is maximal')
    print('-' * 50)


def log_results(Flow, flow_value, total_cost):
    print('resulting flow:')
    print(Flow)
    print('flow value:', flow_value)
    print('total cost:', total_cost)
