# autotuner/graph_logger.py
# Logger for AutoTuner graph algorithm decisions

_graph_log = []

def log_graph_run(algorithm_name, execution_time_ms):
    """
    Logs a graph algorithm run.

    :param algorithm_name: Name of the selected graph algorithm
    :param execution_time_ms: Execution time in milliseconds
    """
    _graph_log.append({
        "selected_algorithm": algorithm_name,
        "execution_time_ms": execution_time_ms
    })

def get_graph_history():
    """
    Returns the full history of graph algorithm runs.

    :return: List of logs in the format:
             [{"selected_algorithm": str, "execution_time_ms": float}, ...]
    """
    return _graph_log.copy()

def clear_graph_logs():
    """
    Clears all graph logs.
    """
    _graph_log.clear()