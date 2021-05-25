import unittest

from doubles.black_fennec.structure.double_map import MapMock
from doubles.double_dummy import Dummy
from doubles.black_fennec.interpretation.double_interpretation_service import InterpretationServiceMock
from src.black_fennec.interpretation.auction.offer import Offer
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.string import String
from src.visualisation.base.file.file_bidder import FileBidder
from src.visualisation.base.image.image import Image
from src.visualisation.base.image.image_bidder import ImageBidder
from src.visualisation.core.map.map_bidder import MapBidder


class ImageBidderTestSuite(unittest.TestCase):
    def test_can_construct(self):
        ImageBidder()

    def test_offer_equal_map_offer(self):
        bidder = ImageBidder()
        subject = MapMock({})
        expected_offer = Offer(subject, 2, Image.TEMPLATE, Dummy())
        offer = bidder.bid(subject)
        self.assertEqual(offer, expected_offer)

    def test_offer_image_like_structure_of_map(self):
        map_bidder = MapBidder(InterpretationServiceMock([]))
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