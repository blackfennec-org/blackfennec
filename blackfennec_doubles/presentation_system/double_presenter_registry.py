from blackfennec_doubles.presentation_system.double_presenter_factory import PresenterFactoryMock


class PresenterRegistryMock:

    def __init__(self, presenters=None):
        self._presenters = presenters or [PresenterFactoryMock()]
        self.presenters_getter_count = 0

        self.register_presenter_count = 0
        self.register_presenter_last_factory = None

        self.deregister_presenter_count = 0
        self.deregister_presenter_last_factory_type = None

    @property
    def presenters(self):
        self.presenters_getter_count += 1
        return self._presenters

    def register_presenter(self, factory):
        self.register_presenter_last_factory = factory
        self.register_presenter_count += 1

    def deregister_presenter(self, factory_type):
        self.deregister_presenter_last_factory_type = factory_type
        self.deregister_presenter_count += 1
