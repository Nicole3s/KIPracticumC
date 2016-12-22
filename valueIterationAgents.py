# valueIterationAgents.py
# -----------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


import mdp, util

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0

        # Write value iteration code here
        "*** YOUR CODE HERE ***"
        counter = 0
        copyvalues = self.values.copy()

        while self.iterations != counter:
          copyvalues = util.Counter()
          for s in mdp.getStates():
           maxq = None
            #get highest q value if there is no value give maxq the value 0
           for a in self.mdp.getPossibleActions(s):
             q = self.computeQValueFromValues(s, a)
             if maxq == None or maxq < q:
              maxq = q
           if maxq == None:
            maxq = 0

           copyvalues[s] = maxq

          self.values = copyvalues

          counter += 1
# update de hele grid niet per state
# 1e vraag was de formule uit de slide van hc gebruiken en niet van Berkley

# self state

#
    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        # de Bellman equation hier doen
        # next state
        q =0
        nextstate = self.mdp.getTransitionStatesAndProbs(state, action)[0]
        for nextstate, prob in self.mdp.getTransitionStatesAndProbs(state, action):
          q += prob * (self.mdp.getReward(state, action, nextstate) + (self.discount * self.getValue(nextstate)))
        return q

        util.raiseNotDefined()

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        #if there are no possible actions return none
        if len(self.mdp.getPossibleActions(state)) == 0:
            return None
        qmax = None
        policy = None
        #get highest qvalue, if qmax is lower than q (or none) the policy is a(the possible action it computed q for)
        for a in self.mdp.getPossibleActions(state):
            q = self.computeQValueFromValues(state, a)
            if qmax == None or qmax < q:
                qmax =q
                policy = a
        return policy

        util.raiseNotDefined()

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
