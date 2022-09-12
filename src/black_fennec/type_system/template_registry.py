import logging

from src.black_fennec.structure.template.template import Template

logger = logging.getLogger(__name__)


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
        self._templates = []

    @property
    def templates(self):
        """templates getter

        Returns:
            set: of templates
        """
        return set(self._templates)

    def register_template(self, template: Template):
        """Function to register a new template

        Args:
            template (Template): future element of the template registry
        """
        self._templates.append(template)

    def deregister_template(self, template_type: type):
        """Function to deregister a template from the dictionary

        Args:
            template_type (type): element in the template registry

        Raises:
            KeyError: if template type not found in registry
        """


        for current_template in self._templates:
            if current_template.__class__ == template_type:
                self._templates.remove(current_template)
