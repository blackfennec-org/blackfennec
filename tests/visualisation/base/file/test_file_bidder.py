import unittest

from doubles.black_fennec.structure.double_map import MapMock
from doubles.double_dummy import Dummy
from doubles.black_fennec.interpretation.double_interpretation_service import InterpretationServiceMock
from src.black_fennec.interpretation.auction.offer import Offer
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.string import String
from src.visualisation.base.file.file import File
from src.visualisation.base.file.file_bidder import FileBidder
from src.visualisation.core.map.map_bidder import MapBidder


class FileBidderTestSuite(unittest.TestCase):
    def test_can_construct(self):
        FileBidder()

    def test_offer_equal_map_offer(self):
        bidder = FileBidder()
        subject = MapMock({})
        expected_offer = Offer(subject, 1, File.TEMPLATE, Dummy())
        offer = bidder.bid(subject)
        self.assertEqual(offer, expected_offer)

    def test_offer_file_like_structure(self):
        map_bidder = MapBidder(InterpretationServiceMock([]))
        file_bidder = FileBidder()
        subject = Map({
            File.FILE_PATH_KEY: String('file_path'),
            File.FILE_TYPE_KEY: String('file_type')
        })
        map_offer = map_bidder.bid(subject)
        file_offer = file_bidder.bid(subject)
        self.assertGreater(file_offer, map_offer)
