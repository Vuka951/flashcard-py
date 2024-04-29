import unittest
from tkinter import Tk
from flashcard import FlashcardApp

class TestFlashcardApp(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.app = FlashcardApp(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_initialization(self):
        self.assertTrue(isinstance(self.app.master, Tk))
        self.assertEqual(self.app.current_card, 0)
        self.assertEqual(len(self.app.cards), 4)

    def test_show_front(self):
        self.app.show_front()
        # Check that the card counter updated - Maybe better to move to a different test?
        expected_text = f"{self.app.current_card + 1}/{len(self.app.cards)}"
        actual_text = self.app.card_counter_label.cget("text")
        self.assertEqual(actual_text, expected_text)

    def test_show_back(self):
        self.app.show_back()
        # Check that the button has been disabled
        self.assertEqual(self.app.show_button.state()[0], "disabled")

    def test_next_card(self):
        initial_card = self.app.current_card
        self.app.next_card()
        self.assertEqual(self.app.current_card, (initial_card + 1) % len(self.app.cards))

    def test_previous_card(self):
        initial_card = self.app.current_card
        self.app.previous_card()
        self.assertEqual(self.app.current_card, (initial_card - 1) % len(self.app.cards))


if __name__ == '__main__':
    unittest.main()
