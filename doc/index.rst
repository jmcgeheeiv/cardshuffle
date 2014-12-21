.. cardshuffle documentation master file, created by
   sphinx-quickstart on Sat Dec 20 17:25:42 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


Cardshuffle Documentation
=======================================

.. _specification:

Cardshuffle is a card shuffling game given to me as an interview question.  The game goes like this:

#. Start with a specified number of cards in your hand
#. Move the top card in your hand to the bottom of the stack of cards in your hand
#. Move the top card in your hand to the bottom of the stack of cards on the table.
#. After the cards in your hand are exhausted, this is one "round".
#. Pick up the cards on the table and examine them.  If they are not in the same \
   order as when you started, repeat anther round.  If they have returned to \
   their original order, report the number of rounds that were performed.
   
Cardshuffle is implemented as a Python API that runs this simulation.  It is demonstrated in file
`cardshuffle/cardshuffle_test.py`.  Run this demonstration (actually unit test) with the UNIX shell
commands::

    PYTHONPATH=/path/to/cardshuffle/:$PYTHONPATH 
    python -m unittest cardshuffle_test

Contents:

.. toctree::
   :maxdepth: 4

   cardshuffle


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

