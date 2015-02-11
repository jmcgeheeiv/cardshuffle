Cardshuffle is a card shuffling game given to me as an interview question.

Specification
---------------

The game goes like this:

1. Start with a specified number of cards in your hand
1. Move the top card in your hand to the bottom of the stack of cards in your hand   
1. Move the top card in your hand to the bottom of the stack of cards on the table
1. After the cards in your hand are exhausted, this is one "round"
1. Pick up the cards on the table and examine them.  If they are not in the same order as when you started, repeat anther round.  If they have returned to their original order, report the number of rounds that were performed.

Source Code
-------------------

* The functional code is in `cardshuffle.py`
* The unit test is in `cardshuffle_test.py`

Documentation
-----------------

The Cardshuffle API documentation is in `cardshuffle/doc/_build/html/index.html`.

Ordinarily, such generated files should not be added to the repository.  In this case I did since this repository is the sole deployment.

Running Cardshuffle
--------------------

Cardshuffle is implemented as a Python API that runs this simulation.  It is demonstrated in file
`cardshuffle_test.py`.  Run this demonstration (actually unit test) with the UNIX shell
commands:

    PYTHONPATH=/path/to/cardshuffle/:$PYTHONPATH 
    python -m unittest cardshuffle_test