import unittest
from models import Review


class ReviewTest(unittest.TestCase):

    def test_review_initialization(self):
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_review_attributes(self):
        review = Review()
        review.place_id = "12345"
        review.user_id = "67890"
        review.text = "Great experience, highly recommended!"

        self.assertEqual(review.place_id, "12345")
        self.assertEqual(review.user_id, "67890")
        self.assertEqual(review.text, "Great experience, highly recommended!")


if __name__ == '__main__':
    unittest.main()
