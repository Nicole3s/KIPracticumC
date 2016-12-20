# Pieter Abbeel (pabbeel@cs.berkeley.edu).


######################
# ANALYSIS QUESTIONS #
######################

# Set the given parameters to obtain the specified policies through
# value iteration.
#  voor parallel exercise
# For exercise 4
# discount parameters analysis for
#  0.5 -> attempted to cross the bridge by only going to the first square and going back to the start terminal state (west) and ended with reward 1.
# It took action west
# 0.25 -> The same at 0.5
# 0.75 -> the same at 0.5
#  1 -> attempted to cross the bridge by only going to the first square (east) but exit the bridge by going south
# 0.1 -> the same at 0.5
# noise parameters analysis for
# 0.1 -> the same at 0.5 discount
# 0.01 -> It crosses the bridge by going east till he reaches the end state
# 0.005 -> It crosses the bridge by going east till he reaches the end state
# 0.001 -> It crosses the bridge by going east till he reaches the end state
# 0 -> It crosses the bridge by going east till he reaches the end state
# 0.02 -> The same at 0.1
def question2():
    answerDiscount = 0.9
    answerNoise = 0
    return answerDiscount, answerNoise

def question3a():
    answerDiscount = 0.1
    answerNoise = 0
    #alles onder 0.0001 werkt
    answerLivingReward = 0.5
    #alles onder 0.8 werkt
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3b():
    answerDiscount = 0.1
    answerNoise = 0.01
    answerLivingReward = 0
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3c():
    answerDiscount = 0.9
    answerNoise = 0.001
    answerLivingReward = 0
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3d():
    answerDiscount = 0.9
    answerNoise = 0.2
    answerLivingReward = 0.1
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3e():
    answerDiscount = 1
    answerNoise = 0
    answerLivingReward = 0
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question6():
    answerEpsilon = None
    answerLearningRate = None
    return 'NOT POSSIBLE'
    # If not possible, return 'NOT POSSIBLE'

if __name__ == '__main__':
    print 'Answers to analysis questions:'
    import analysis
    for q in [q for q in dir(analysis) if q.startswith('question')]:
        response = getattr(analysis, q)()
        print '  Question %s:\t%s' % (q, str(response))
