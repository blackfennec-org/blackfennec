import blackfennec.layers.merge.merger as m


class DeepMerge:
    @staticmethod
    def merge(underlay, overlay):
        merger: m.Merger = overlay.accept(m.MergerFactory())
        return merger.merge(underlay)
