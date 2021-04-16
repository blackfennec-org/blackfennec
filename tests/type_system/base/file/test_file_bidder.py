import unittest

from doubles.dummy import Dummy
from src.interpretation.auction import Offer
from src.structure.map import Map
from src.structure.string import String
from src.type_system.base.file.file import File
from src.type_system.base.file.file_bidder import FileBidder
from src.type_system.core.map.map_bidder import MapBidder


class FileBidderTestSuite(unittest.TestCase):
    def test_can_construct(self):
        FileBidder()

    def test_offer_equal_map_offer(self):
        bidder = FileBidder()
        subject = {}
        expected_offer = Offer(subject, 1, Map(), Dummy())
        offer = bidder.bid(subject)
        self.assertEqual(offer, expected_offer)

    def test_offer_file_like_structure(self):
        map_bidder = MapBidder()
        file_bidder = FileBidder()
        subject = Map({
            File.FILE_PATH_KEY: String('file_path'),
            File.FILE_TYPE_KEY: String('file_type')
        })
        map_offer = map_bidder.bid(subject)
        file_offer = file_bidder.bid(subject)
        self.assertGreater(file_offer, map_offer)
