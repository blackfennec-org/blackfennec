import unittest

from doubles.dummy import Dummy
from src.base.types.file.file import File
from src.base.types.file.file_bidder import FileBidder
from src.core.auction import Offer
from src.core.types.map import Map
from src.core.types.map.map_bidder import MapBidder
from src.core.types.string import String


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
