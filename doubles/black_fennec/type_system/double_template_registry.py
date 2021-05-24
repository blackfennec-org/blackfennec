class TemplateRegistryMock:

    def __init__(self, templates=None):
        if templates is None:
            templates = set()
        self._templates = templates
        self.templates_getter_count = 0

        self.register_template_count = 0
        self.register_template_last_template = None

        self.deregister_template_count = 0
        self.deregister_template_last_template_type = None

    @property
    def templates(self):
        self.templates_getter_count += 1
        return self._templates

    def register_template(self, template):
        self.register_template_last_template = template
        self.register_template_count += 1

    def deregister_template(self, template_type):
        self.deregister_template_last_template_type = template_type
        self.deregister_template_count += 1
