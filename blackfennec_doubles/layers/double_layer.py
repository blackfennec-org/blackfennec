

class LayerMock:
    def __init__(self, returns=None):
        self._layer = {}
        self.returns = returns

    def apply(self, structure):
        count = self._layer.get(structure, (0,))[0] + 1
        stats = (count, structure)
        self._layer[structure] = stats
        return self.returns
    
    def get_stats(self, subject_type_name):
        return self._layer.get(subject_type_name, (0, None))