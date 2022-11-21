class FactoryBaseVisitorMock:
    def __init__(self, returns=None):
        self._visited = {}
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
        self.visit_null_count = 0
        self.null = None
        self._metadata_storage = dict()
        self._returns = returns
        
    def get_stats(self, subject_type_name):
        return self._visited.get(subject_type_name, (0, None))

    def visit_string(self, subject_string):
        self.visit_string_count += 1
        self.string = subject_string
        self._visited['String'] = (self.visit_string_count, self.string)
        return self._returns or subject_string

    def visit_number(self, subject_number):
        self.visit_number_count += 1
        self.number = subject_number
        self._visited['Number'] = (self.visit_number_count, self.number)
        return self._returns or subject_number

    def visit_boolean(self, subject_boolean):
        self.visit_boolean_count += 1
        self.boolean = subject_boolean
        self._visited['Boolean'] = (self.visit_boolean_count, self.boolean)
        return self._returns or subject_boolean

    def visit_reference(self, subject_reference):
        self.visit_reference_count += 1
        self.reference = subject_reference
        self._visited['Reference'] = (self.visit_reference_count, self.reference)
        return self._returns or subject_reference

    def visit_list(self, subject_list):
        self.visit_list_count += 1
        self.list = subject_list
        self._visited['List'] = (self.visit_list_count, self.list)
        return self._returns or subject_list

    def visit_map(self, subject_map):
        self.visit_map_count += 1 
        self.map = subject_map
        self._visited['Map'] = (self.visit_map_count, self.map)
        return self._returns or subject_map

    def visit_null(self, subject):
        self.visit_null_count += 1
        self.null = subject
        self._visited['Null'] = (self.visit_null_count, self.null)
        return self._returns or subject

    @property
    def metadata_storage(self):
        return self._metadata_storage