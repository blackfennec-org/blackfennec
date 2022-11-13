


class ViewFactoryRegistryMock:
    def __init__(self, factory=None):
        self._factory = factory
        self.factories_getter_count = 0

        self.register_factory_count = 0
        self.register_factory_last_type = None

        self.deregister_factory_count = 0
        self.deregister_factory_last_type = None

    def get_factory(self, type, specification):
        self.factories_getter_count += 1
        return self._factory

    def register_view_factory(self, type, specification, factory):
        self.register_factory_last_type = type
        self.register_factory_count += 1

    def deregister_view_factory(self, type, specification):
        self.deregister_factory_last_type = type
        self.deregister_factory_count += 1
