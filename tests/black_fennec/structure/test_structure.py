import unittest
from abc import ABCMeta, abstractmethod
from doubles.black_fennec.structure.double_root import RootMock
from doubles.black_fennec.structure.encapsulation_base.double_factory_base_visitor import FactoryBaseVisitorMock
from src.black_fennec.structure.structure import Structure


class StructureTestMixin(metaclass=ABCMeta):
    def test_can_set_parent(self):
        structure = self.create_instance(self.default_value)
        new_parent = RootMock()
        structure.parent = new_parent

        self.assertEqual(structure.parent, new_parent)

    @abstractmethod
    def create_instance(self, value):
        ...

    def test_can_get_value(self):
        structure = self.create_instance(self.default_value)

        self.assertEqual(self.default_value, structure.value)

    def test_can_set_value(self):
        structure = self.create_instance(self.default_value)
        structure.value = self.alternative_value

        self.assertEqual(self.alternative_value, structure.value)

    def test_can_accept(self):
        structure = self.create_instance(self.default_value)
        visitor = FactoryBaseVisitorMock()

        structure.accept(visitor)

        count, subject = visitor.get_stats(self.structure_type_name)
        self.assertEqual(subject, structure)
        self.assertEqual(count, 1)

    def test_can_get_repr(self):
        structure = self.create_instance(self.default_value)
        representation = str(structure)
        self.assertIn(self.structure_type_name, representation)
