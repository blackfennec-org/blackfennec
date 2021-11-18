import logging

from src.black_fennec.structure.template.template_base import TemplateBase

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
        self._templates = set()

    @property
    def templates(self):
        """templates getter

        Returns:
            set: of templates
        """
        return set(self._templates)

    def register_template(self, template: TemplateBase):
        """Function to register a new template

        Args:
            template (TemplateBase): future element of the template registry
        """
        self._templates.add(template)

    def deregister_template(self, template_type: type):
        """Function to deregister a template from the dictionary

        Args:
            template_type (type): element in the template registry

        Raises:
            KeyError: if template type not found in registry
        """
        to_delete = None
        for template in self._templates:
            if isinstance(
                    template,
                    template_type):  # pylint: disable=unidiomatic-typecheck
                to_delete = template
        if to_delete:
            self._templates.remove(to_delete)
        else:
            message = f'Could not find Template by type({template_type})'
            logger.error(message)
            raise KeyError(message)
