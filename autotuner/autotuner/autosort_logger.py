# autosort_logger.py

import time
import os
import json

class AutoSortLogger:
    def __init__(self, persist=False, log_file="autosort_logs.json"):
        self.logs = []
        self.persist = persist
        self.log_file = log_file

        if persist:
            self._load_existing_logs()

    def _load_existing_logs(self):
        if os.path.exists(self.log_file):
            with open(self.log_file, "r") as f:
                self.logs = json.load(f)

    def log(self, input_array, selected_algorithm, execution_time_ms):
        entry = {
            "timestamp": time.time(),
            "input_size": len(input_array),
            "selected_algorithm": selected_algorithm,
            "execution_time_ms": round(execution_time_ms, 3)
        }
        self.logs.append(entry)

        if self.persist:
            with open(self.log_file, "w") as f:
                json.dump(self.logs, f, indent=2)

    def get_logs(self):
        return self.logs

    def clear_logs(self):
        self.logs = []
        if self.persist and os.path.exists(self.log_file):
            os.remove(self.log_file)

# Singleton instance
autosort_logger = AutoSortLogger(persist=False)  # Set True to persist to file
