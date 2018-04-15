from __future__ import division

# Author: Robby Costales
# Date: 2018-04-09
# Language: Python 3

# Purpose: Main file for Viterbi algorithm implementation

import random
import numpy


def calc_last(seq):
    global N, B, S, P, V
    global T

    # prevs = []
    # for i in range(len(N)):
    #     # don't worry about checking if equal to None first
    #     # will always be None at tiem of calculation
    #     T[i][-1] = calc_cell(seq, i, len(seq)-1)
    #     prevs.append(T[i][-1])



def most_likely_states(seq):
    """
    Given a sequence of values, what is the most likely sequence of states?

    USES DYNAMIC PROGRAMMING

    Args:
        seq : sequence
    Return:
        states as list of state indices
    """
    global N, B, S, P, V
    global T

    T = [[None for j in range(len(seq))] for i in range(len(N))]

    # dynamic programming
    x = calc_last(seq)

    return T



def generate_sequence(n=50):
    """
    Generates "dice-roll" sequence of length n

    Args:
        n : (int) length of sequence
    Return:
        Sequence as list of values
    """
    global N, B, S, P, V

    # initialize final sequence (will contain values)
    sequence = [-1 for i in range(n)]
    # initialize states (will contain 0, 1, 2, ... k where k+1 is number of possible states--or number of die)
    states = [-1 for i in range(n)]

    for i in range(0, n):
        # assign current Die
        if i == 0:
            # if no prevD
            curD = int(numpy.random.choice(N, p=B))
            states[i] = curD
        else:
            prevD = states[i-1]
            curD = int(numpy.random.choice(N, p=S[prevD]))
            states[i] = curD

        # roll with current Die
        sequence[i] = int(numpy.random.choice(V[states[i]], size=1, p=P[states[i]]))

    return sequence, states



if __name__ == "__main__":
    # d0 is fair
    # d1 is weighted
    global N, B, S, D, V

    # dice indices
    N = [0, 1]

    # beginning probabilities
    B = [1, 0]

    # switching probabilities
    S =    [[0.9, 0.1],
             [0.4, 0.6]]

    # die probabilities
    P =    [[1/6, 1/6, 1/6, 1/6, 1/6, 1/6],
            [1/10, 1/10, 1/10, 1/10, 1/10, 1/2]]

    # die values
    V =     [[1, 2, 3, 4, 5, 6],
            [1, 2, 3, 4, 5, 6]]

    # generate sequences
    S1 = generate_sequence(50)

    print(S1[0])
    print(S1[1])

    # find most likely sequence using dynamic programming
    # L = most_likely_states(S1[0])
