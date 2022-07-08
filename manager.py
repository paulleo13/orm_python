from executor import Executor


class DBModelManager:
    executor = Executor()

    def __init__(self, db_settings, model_class):
        self.executor.connection_details = db_settings
        self.model_class = model_class
