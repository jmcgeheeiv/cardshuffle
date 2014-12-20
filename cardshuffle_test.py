# CardShuffle Interview question.
# Tnis is a card game where numbered cards are shuffled in a deterministic
# fashion.  The program simulates the shuffle, and counts how many iterations
# ("rounds") are required to return the deck of cards to its original order.
#
# Copyright 1014 John McGehee
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


"""
Test the operation of the :py:class`CardShuffle` module as a whole.
"""

import unittest
import doctest
import cardshuffle

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(cardshuffle))
    return tests

class TestShuffler(unittest.TestCase): # pylint: disable=R0904
    '''Test the cardshuffle module.'''

    def setUp(self):
        None

    def tearDown(self):
        None
        
    def test_play(self):
        '''
        Test the CardShuffle game API as a whole.  :py:CardShuffle.play takes
        the number of cards in the game and returns the number of rounds in
        the game'''
        game = cardshuffle.Shuffler()
        self.assertEqual(game.play(0), 0)
        self.assertEqual(game.play(1), 1)
        self.assertEqual(game.play(2), 2)
        self.assertEqual(game.play(3), 2)
        self.assertEqual(game.play(4), 4)
        

if __name__ == "__main__":
    unittest.main()
