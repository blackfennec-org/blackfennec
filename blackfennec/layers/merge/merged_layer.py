from blackfennec.structure.structure import Structure
import blackfennec.layers.merge.merger as m

class MergedLayer:
    def __init__(self) -> None:
        self._layer = {}
        self._factory = m.MergerFactory(self)

    def apply(self, underlay: Structure, overlay: Structure) -> Structure:
        if (underlay, overlay) in self._layer:
            return self._layer[(underlay, overlay)]
        
        merger = self._factory.create(overlay)
        encaps = merger.merge(underlay)

        self._layer[(underlay, overlay)] = encaps
        return encaps