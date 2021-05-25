from src.black_fennec.util.observable import Observable
from src.black_fennec.structure.info import Info
from src.black_fennec.structure.map import Map
from src.black_fennec.navigation.navigation_proxy import NavigationProxy
from src.black_fennec.interpretation.specification import Specification
from src.black_fennec.interpretation.interpretation import Interpretation
from src.black_fennec.interpretation.interpretation_service import InterpretationService
from src.black_fennec.structure.template.template_base import TemplateBase
from src.black_fennec.type_system.template_registry import TemplateRegistry



class MapViewModel(Observable):
    """View model for core type Map."""

    def __init__(self,
            interpretation: Interpretation,
            interpretation_service: InterpretationService,
            template_registry: TemplateRegistry ):
        """Create with value empty map.

        Args:
            interpretation (Interpretation): The overarching interpretation
            interpretation_service (InterpretationService): service to
                interpret substructures and create previews
            template_registry (TemplateRegistry): registry used to
                add children to List from template.

        """
        Observable.__init__(self)
        self._interpretation = interpretation
        self._interpretation_service = interpretation_service
        self._template_registry = template_registry
        assert isinstance(self._interpretation.info, Map)
        self._map = self._interpretation.info

    @property
    def value(self):
        """Readonly property for value."""
        return self._map

    def create_preview(self, substructure: Info) -> Interpretation:
        """create preview for substructure

        Args:
            substructure (Info): will be interpreted as a preview

        Returns:
            Interpretation: represents the substructure as preview
        """
        preview = self._interpretation_service.interpret(
            substructure, Specification(request_preview=True))
        navigation_proxy = NavigationProxy(self._interpretation)
        preview.set_navigation_service(navigation_proxy)
        return preview

    def add_item(self, key, value: Info):
        """Add item (key, value) to the map.

        Args:
            key: The key under which to store the value.
            value (:obj:`Info`): The `Info` behind the key.
        """
        self._map[key] = value
        self._notify(self.value, 'value')

    def delete_item(self, key):
        """Delete an item from the map.

        Args:
            key: The key of the key value pair which should be deleted
        """
        self._map.pop(key)
        self._notify(self.value, 'value')

    def rename_key(self, old_key, new_key):
        """Rename the key of an item.

                Args:
                    old_key: The key of the key value pair
                        which should be renamed
                    new_key: The new key name of the key value pair
                """
        self._map[new_key] = self._map.pop(old_key)
        self._notify(self.value, 'value')

    def add_by_template(self, key, template: TemplateBase):
        self.add_item(key, template.subject)

    def get_templates(self):
        return self._template_registry.templates

    def navigate_to(self, route_target: Info):
        self._interpretation.navigate(route_target)
