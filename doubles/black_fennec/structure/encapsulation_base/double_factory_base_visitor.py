class FactoryBaseVisitorMock:
    def __init__(self):
        self.visit_structure_count = 0
        self.structure = None
        self.visit_root_count = 0
        self.root = None
        self.visit_string_count = 0
        self.string = None
        self.visit_number_count = 0
        self.number = None
        self.visit_boolean_count = 0
        self.boolean = None
        self.visit_reference_count = 0
        self.reference = None
        self.visit_list_count = 0
        self.list = None
        self.visit_map_count = 0
        self.map = None
        self._metadata_storage = dict()
        
    def visit_structure(self, subject_structure):
        self.visit_structure_count += 1
        self.structure = subject_structure
        return subject_structure

    def visit_root(self, subject_root):
        self.visit_root_count += 1
        self.root = subject_root
        return subject_root

    def visit_string(self, subject_string):
        self.visit_string_count += 1
        self.string = subject_string
        return subject_string

    def visit_number(self, subject_number):
        self.visit_number_count += 1
        self.number = subject_number
        return subject_number

    def visit_boolean(self, subject_boolean):
        self.visit_boolean_count += 1
        self.boolean = subject_boolean
        return subject_boolean

    def visit_reference(self, subject_reference):
        self.visit_reference_count += 1
        self.reference = subject_reference
        return subject_reference

    def visit_list(self, subject_list):
        self.visit_list_count += 1
        self.list = subject_list
        return subject_list

    def visit_map(self, subject_map):
        self.visit_map_count += 1 
        self.map = subject_map
        return subject_map

    @property
    def metadata_storage(self):
        return self._metadata_storage