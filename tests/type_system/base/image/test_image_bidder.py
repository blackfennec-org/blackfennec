import unittest

from doubles.dummy import Dummy
from src.interpretation.auction import Offer
from src.structure.map import Map
from src.structure.string import String
from src.type_system.base.file.file_bidder import FileBidder
from src.type_system.base.image.image import Image
from src.type_system.base.image.image_bidder import ImageBidder
from src.type_system.core.map.map_bidder import MapBidder


class ImageBidderTestSuite(unittest.TestCase):
    def test_can_construct(self):
        ImageBidder()

    def test_offer_equal_map_offer(self):
        bidder = ImageBidder()
        subject = {}
        expected_offer = Offer(subject, 2, Map(), Dummy())
        offer = bidder.bid(subject)
        self.assertEqual(offer, expected_offer)

    def test_offer_image_like_structure_of_map(self):
        map_bidder = MapBidder()
        image_bidder = ImageBidder()
        subject = Map({
            Image.FILE_PATH_KEY: String('image_path'),
            Image.FILE_TYPE_KEY: String('image_type')
        })
        map_offer = map_bidder.bid(subject)
        image_offer = image_bidder.bid(subject)
        self.assertLess(image_offer, map_offer)

    def test_offer_image_like_structure_of_file(self):
        file_bidder = FileBidder()
        image_bidder = ImageBidder()
        subject = Map({
            Image.FILE_PATH_KEY: String('image_path'),
            Image.FILE_TYPE_KEY: String('image/mock')
        })
        file_offer = file_bidder.bid(subject)
        image_offer = image_bidder.bid(subject)
        self.assertGreater(image_offer, file_offer)

    def test_offer_file_like_structure_of_image(self):
        file_bidder = FileBidder()
        image_bidder = ImageBidder()
        subject = Map({
            Image.FILE_PATH_KEY: String('image_path'),
            Image.FILE_TYPE_KEY: String('image_type')
        })
        file_offer = file_bidder.bid(subject)
        image_offer = image_bidder.bid(subject)
        self.assertLess(image_offer, file_offer)
