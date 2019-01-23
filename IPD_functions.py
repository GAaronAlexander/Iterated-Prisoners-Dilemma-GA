import numpy as np

def match_score(strategy1, strategy2):
  """Returns the scores of two strategies (input as binary strings) after
  playing through a match of 64 rounds between them.

  Indices 0-63 of strategy array contain player's response to all possible 
  histories when there is a history of 3 games (6 moves -> 2^6 = 64).
  Indices 64-79 contain player responses to all possible histories when there
  is a history of 2 (4 moves -> 2^4 = 16).
  Indices 80-83 contain responses to all possible histories of 1 (2 moves = 4
  possibilities).
  Index 84 contains the player initial move.
  """
  # Initial round.
  P1_move = strategy1[84]
  P2_move = strategy2[84]
  # Each player's "history" displays first their move and then the other 
  # player's move (e.g. if in the last round, P1 defects, and P2 cooperates, 
  # p1 sees this round as '01' and p2 sees it as '10'). The full history will
  # be a string with both player's moves alternating.
  History1 = P1_move + P2_move
  History2 = P2_move + P1_move
  # Second round.
  P1_move = strategy1[80 + int(History1,2)]
  P2_move = strategy2[80 + int(History2,2)]
  History1 = History1 + P1_move + P2_move
  History2 = History2 + P2_move + P1_move
  # Third round.
  P1_move = strategy1[64 + int(History1,2)]
  P2_move = strategy2[64 + int(History2,2)]
  History1 = History1 + P1_move + P2_move
  History2 = History2 + P2_move + P1_move
  # Now that we have a history of 3, loop from 3rd to 64th move.
  for i in range(6,128,2):
    P1_move = strategy1[int(History1[i-6:i],2)]
    P2_move = strategy2[int(History2[i-6:i],2)]
    History1 = History1 + P1_move + P2_move
    History2 = History2 + P2_move + P1_move
  # Add up scores for each player.
  History1_array = np.zeros(128)
  History2_array = np.zeros(128)
  # Convert binary strings to numpy array so elements can be summed.
  for i in range(len(History1_array)):
    History1_array[i] = int(History1[i],10)
    History2_array[i] = int(History2[i],10)
    # Each players receives a benefit of 5 when the other player cooperates
    # and a cost of -2 when they cooperate
  P1_score = np.sum(History1_array[0:127:2])*-2 \
                    + np.sum(History2_array[0:127:2])* 5
  P2_score = np.sum(History2_array[0:127:2])*-2 \
                    + np.sum(History1_array[0:127:2])* 5
  return P1_score, P2_score


def total_scores(population):
  """Plays every strategy in population against every other strategy once
  (strategies don't play against themselves), and returns total score of 
  each strategy.
  """
  scores = np.zeros(len(population)) # initialize population scores array
  for i in range(len(population)):
    j = 0
    while j < i:
      # play a match between each strategy and every other strategy in 
      # population
      P1_score, P2_score = match_score(population[i], population[j])
      scores[i] += P1_score
      scores[j] += P2_score
      j += 1
  return scores


# Tests
#from premade_strategies import *
#P1_score, P2_score = round_score(always_defect(), tit_for_tat())
#pop = [always_defect(), always_cooperate()]
#scores = total_scores(pop)
