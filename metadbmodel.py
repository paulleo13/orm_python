from torch import manager_path


from manager import DBModelManager


class MetaDBModel(type):
    manager_class = DBModelManager

    @property
    def objects(cls):
        return cls._get_manager()

    def _get_manager(cls):
        return cls.manager_class(model_class=cls)