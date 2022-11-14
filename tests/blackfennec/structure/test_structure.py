from abc import ABCMeta, abstractmethod
from blackfennec_doubles.structure.double_root import RootMock
from blackfennec_doubles.layers.encapsulation_base.double_factory_base_visitor import FactoryBaseVisitorMock
from tests.test_utils.observer import Observer


class StructureTestMixin(metaclass=ABCMeta):
    @abstractmethod
    def create_instance(self, value):
        ...

    def test_can_get_value(self):
        structure = self.create_instance(self.default_value)

        assert self.default_value == structure.value

    def test_can_set_value(self):
        structure = self.create_instance(self.default_value)
        structure.value = self.alternative_value

        assert self.alternative_value == structure.value

    def test_notifies_on_value_change(self):
        observer = Observer()
        structure = self.create_instance(self.default_value)
        structure.bind(changed=observer.endpoint)
        structure.value = self.alternative_value

        assert observer.last_call[0][1].new_value == self.alternative_value
        assert observer.last_call[0][1].old_value == self.default_value

    def test_can_accept(self):
        structure = self.create_instance(self.default_value)
        visitor = FactoryBaseVisitorMock()

        structure.accept(visitor)

        count, subject = visitor.get_stats(self.structure_type_name)
        assert subject == structure
        assert count == 1

    def test_can_set_parent(self):
        structure = self.create_instance(self.default_value)
        new_parent = RootMock()
        structure.parent = new_parent

        assert structure.parent == new_parent
