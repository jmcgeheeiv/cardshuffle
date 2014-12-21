# CardShuffle Interview question.
#
# This is a card game where numbered cards are shuffled in a deterministic
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

import collections

class Shuffler(object):
    '''
    Play the game according to the `specification <index.html>`_.  The number of cards is
    specified to the constructor.  The :py:func:`play` method plays the game
    and returns the number of rounds (iterations of shuffling) that were
    required:
    
    >>> import cardshuffle
    >>> game = cardshuffle.Shuffler(0)
    >>> game.play()
    0
    >>> game = cardshuffle.Shuffler(5)
    >>> game.play()
    5
    >>> game = cardshuffle.Shuffler(52)
    >>> game.play()
    840
    '''
    def __init__(self, ncards):        
        self._hand_stack = CardStack(ncards)
        self._table_stack = CardStack(0)
        
        self._original_stack = CardStack(ncards)
    
    def play(self):
        '''
        Shuffle the cards until the order of the cards in hand is the same as
        when the game commenced.  Return the number of rounds of shuffling that
        were required.
        '''
        if not len(self._hand_stack):
            # Cannot shuffle zero cards even once
            return 0
        
        self._shuffle_one_round()
        nrounds = 1        

        while self._hand_stack != self._original_stack:
            self._shuffle_one_round()
            nrounds += 1
        return nrounds
            
    def _shuffle_one_round(self):
        '''
        Shuffle the stack in hand onto the stack on the table and then swap the
        two in preparation for the next round of shuffling.
        
        >>> game = Shuffler(0)
        >>> game._shuffle_one_round()
        >>> game._hand_stack
        []
        >>> game._table_stack
        []
        
        >>> game = Shuffler(1)
        >>> game._shuffle_one_round()
        >>> game._hand_stack
        [0]
        >>> game._table_stack
        []
        
        >>> game = Shuffler(2)
        >>> game._shuffle_one_round()
        >>> game._hand_stack
        [1, 0]
        >>> game._table_stack
        []
        
        >>> game = Shuffler(3)
        >>> game._shuffle_one_round()
        >>> game._hand_stack
        [1, 0, 2]
        >>> game._table_stack
        []
        
        >>> game = Shuffler(4)
        >>> game._shuffle_one_round()
        >>> game._hand_stack
        [1, 3, 2, 0]
        >>> game._table_stack
        []
        
        >>> game = Shuffler(5)
        >>> game._shuffle_one_round()
        >>> game._hand_stack
        [1, 3, 0, 4, 2]
        >>> game._table_stack
        []
        '''
        try:
            while True:
                # Move the top card in the hand stack to the bottom of the
                # hand stack
                card = self._hand_stack.remove()
                self._hand_stack.add(card)
                # Move the top card in the hand stack to the bottom of the
                # stack on the table
                card = self._hand_stack.remove()
                self._table_stack.add(card)
        except IndexError:
            # Ran out of cards, which is fine.
            None

        self._hand_stack, self._table_stack = self._table_stack, self._hand_stack
    
    def __repr__(self):
        '''
        String that uniquely represents this instance.
        
        >>> repr(Shuffler(3))
        'Hand: [0, 1, 2] Table: [] Original: [0, 1, 2]'
        '''
        return 'Hand: {} Table: {} Original: {}'.format(self._hand_stack,
                      self._table_stack, self._original_stack)
        
        
class CardStack(object):
    '''
    A FIFO stack of numbered cards.  Cards are added to the bottom of the
    stack, and removed from the top of the stack.
    
    In this implementation, a card is an integer, but nothing prevents
    this from becoming an instance that has, say, a suit and a number.

    If initialized with a nonzero number of cards, the card values are
    sequential:
    
    >>> stack = CardStack(3)
    >>> stack.remove()
    0
    >>> stack.remove()
    1
    >>> stack.remove()
    2
    
    The first card added to the bottom is the first card to be removed
    from the top:
    
    >>> stack = CardStack(0)
    >>> stack.add(0)
    >>> stack.add(1)
    >>> stack.add(2)
    >>>
    >>> stack.remove()
    0
    >>> stack.remove()
    1
    >>> stack.remove()
    2
    
    If no cards remain, :py:func:`remove` raises an :py:class:`IndexError`
    exception:
    
    >>> stack = CardStack(0)
    >>> stack.remove() 
    Traceback (most recent call last):
        ...
    IndexError: pop from an empty deque
    '''
    def __init__(self, ncards):
        self._cards = collections.deque(range(ncards))
    
    def add(self, card):
        '''
        Add a card to the bottom of the stack.  In this implementation, the
        bottom is the right side of the `_cards` deque.
    
        >>> stack = CardStack(0)
        >>> stack.add(0)
        >>> stack.add(1)
        >>> stack.add(2)
        >>>
        >>> stack.remove()
        0
        >>> stack.remove()
        1
        >>> stack.remove()
        2
        '''
        self._cards.append(card)
        
    def remove(self):
        '''
        Remove a card from the top of the stack and return it.  In this
        implementation, the top is the left side of the `_cards` deque.
        
        If no elements are present, this raises an IndexError.
    
        >>> stack = CardStack(0)
        >>> stack.add(0)
        >>> stack.add(1)
        >>> stack.add(2)
        >>>
        >>> stack.remove()
        0
        >>> stack.remove()
        1
        >>> stack.remove()
        2
        '''
        return self._cards.popleft()

    def __eq__(self, other):
        '''
        Equality operator:
        
        >>> stack1 = CardStack(2)
        >>> stack2 = CardStack(0)
        >>> stack1 == stack2   
        False
        >>> stack2.add(0)
        >>> stack1 == stack2   
        False
        >>> stack2.add(1)
        >>> stack1 == stack2   
        True
        '''
        if isinstance(other, CardStack):
            return self._cards == other._cards
        return NotImplemented
    
    def __ne__(self, other):
        '''Inequality operator.
                
        >>> stack1 = CardStack(2)
        >>> stack2 = CardStack(0)
        >>> stack1 != stack2   
        True
        >>> stack2.add(0)
        >>> stack1 != stack2   
        True
        >>> stack2.add(1)
        >>> stack1 != stack2   
        False
        '''
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        return not result
    
    def __len__(self):
        '''
        Return the number of cards in the stack.
        
        >>> stack = CardStack(0)
        >>> len(stack)
        0
        
        >>> stack = CardStack(1)
        >>> len(stack)
        1
        
        >>> stack = CardStack(2)
        >>> len(stack)
        2
        '''
        return len(self._cards)
        
        
    def __repr__(self):
        '''String that uniquely represents this instance.
        
        >>> repr(CardStack(5))
        '[0, 1, 2, 3, 4]'
        '''
        return repr(list(self._cards))
        