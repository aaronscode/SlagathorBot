#!/bin/python

#

from collections import defaultdict, Counter
from numpy import cumsum, sum, searchsorted
from numpy.random import rand

class MarkovChain():
    def __init__(self, order=1):
        """
        Initializes a Markov Chain of the given order.
        """
        self._transitions = defaultdict(int)
        self._order = order

    def train(self, sequence):
        """
        Trains the model using sequence.
        """
        self._symbols = list(set(sequence))
        for i in range(len(sequence)-self._order):
            self._transitions[sequence[i:i+self._order], sequence[i+self._order]] += 1

    def predict(self, symbol):
        """
        Takes in input a string and predicts the next character.
        """
        if len(symbol) != self._order:
            raise ValueError('Expected string of %d chars, got %d' % (self._order, len(symbol)))
        probs = [self._transitions[(symbol, s)] for s in self._symbols]
        return self._symbols[self._weighted_pick(probs)]

    def generate(self, start, n):
        """
        Generates n characters from start.
        """
        result = start
        for i in range(n):
            new = self.predict(start)
            result += new
            start = start[1:] + new
        return result

    @staticmethod
    def _weighted_pick(weights):
        """
          Weighted random selection returns n_picks random indexes.
          The chance to pick the index i is given by weights[i].
        """
        return searchsorted(cumsum(weights), rand()*sum(weights))

# end markov class definition

configFile = 'config.txt'

def main():
    
    inputFile = ''
    chat = ''
    with open(configFile) as config:
        for line in config:
           inputFile = line.rstrip()

    with open(inputFile) as chatMsgs:
        chat = chatMsgs.read()

    '''
    mc1 = MarkovChain(order=1)
    print("Training first order markov chain")
    mc1.train(chat)
    print("Text from MC1:\n" + mc1.generate('t', 100) + '\n')

    mc2 = MarkovChain(order=2)
    print("Training second order markov chain")
    mc2.train(chat)
    print("Text from MC2:\n" + mc2.generate('th', 100) + '\n')

    mc3 = MarkovChain(order=4)
    print("Training fourth order markov chain")
    mc3.train(chat)
    print("Text from MC3:\n" + mc3.generate('that', 100) + '\n')

    mc4 = MarkovChain(order=6)
    print("Training sixth order markov chain")
    mc4.train(chat)
    print("Text from MC4:\n" + mc4.generate('that d', 100) + '\n')

    mc5 = MarkovChain(order=8)
    print("Training eighth order markov chain")
    mc5.train(chat)
    print("Text from MC5:\n" + mc5.generate('that dam', 100) + '\n')
    '''

    mc5 = MarkovChain(order=8)
    print("Training eighth order markov chain")
    mc5.train(chat)
    print("Text from MC5:\n" + mc5.generate('snickers', 4000) + '\n')
if __name__ == "__main__":
    main()

