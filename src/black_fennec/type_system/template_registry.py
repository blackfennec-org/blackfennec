from src.black_fennec.structure.template.template_base import TemplateBase


class TemplateRegistry:
    """Template Registry Class

    Is a register of all known or registered templates.

    Attributes:
        _templates: stores internal templates
    """

    def __init__(self):
        """template_registry constructor.

        Initializes the _templates attribute with empty list
        """
        self._templates = set()

    @property
    def templates(self):
        """templates getter

        Returns:
            set: of templates
        """
        return set(self._templates)

    def register_template(self, template):
        """Function to register a new template

        Args:
            template (TemplateBase): future element of the template registry
        """
        self._templates.add(template)

    def deregister_template(self, template_type: type):
        """Function to deregister a template from the dictionary

        Args:
            template_type (type): element in the template registry
        """
        for template in self._templates:
            if type(template) == template_type:
                self._templates.remove(template)
