import numpy as np

############################################################################
# Selection functions.
############################################################################

def weighted_fitness_selection(P, scores):
  """Selects parents from population with probability weighted by total scores.

  Arguments: P: a list of strategy strings
             scores: numpy array.
  Returns: A list of strategy strings."""
  # Normalize and translate scores so that they are all positive.
  #normalized_score = (scores + 2*64*(len(P)-1))/(sum(scores + 2*64*(len(P)-1)))
  # Alternate weighting/normalizing to give greater weight to higher scores
  normalized_score = 1.002**scores / sum(1.002**scores)
  chosen = np.random.choice(P, size = len(P), replace = True,
                            p = normalized_score)
  return chosen


def tournament_selection(P, f, tournament_size):
  """Selects a new population from population P using tournament selection."""
  new_P = np.zeros_like(P)
  for i in range(len(new_P)):
    new_P[i] = _tournament_select_one(P, f, tournament_size)
  return new_P


def _tournament_select_one(P, scores, tournament_size):
  """Select 1 parent from population P using a tournament of size
  tournament_size.
  """
  candidates = np.random.randint(0, len(P), tournament_size)
  best = scores[candidates].argmax()
  index = candidates[best]
  return P[index]

############################################################################
# Crossover functions.
############################################################################

def crossover_pair_onepoint(parent_1, parent_2):
  """One-point crossover on a pair of parents."""
  x = np.random.randint(len(parent_1))
  child_1 = parent_1[:x] + parent_2[x:]
  child_2 = parent_2[:x] + parent_1[x:]
  return child_1, child_2


def crossover_pair_random(parent_1, parent_2):
  """Random crossover on a pair of parents."""
  dim = len(parent_1)
  # Convert parents to numpy arrays.
  parent_1 = np.array(list(parent_1))
  parent_2 = np.array(list(parent_2))
  child_1 = np.array(['0'] * dim)
  child_2 = np.array(['0'] * dim)

  # Make random array of 0s and 1s to determine which parts come from each
  # parent.
  x = np.random.randint(0, 2, dim)
  child_1[x==1] = parent_1[x==1]
  child_1[x==0] = parent_2[x==0]
  child_2[x==1] = parent_2[x==1]
  child_2[x==0] = parent_1[x==0]

  # Convert children to strings and return.
  return ''.join(child_1), ''.join(child_2)


def crossover(P, crossover_pair_function, prob_crossover):
  """Crossover on whole population.
  
  Have a choice of either one point or random crossover.
  """
  new_P = np.zeros_like(P)
  for i in range(0, len(P), 2):
    if np.random.rand() < prob_crossover:
      new_P[i], new_P[i+1] = crossover_pair_function(P[i], P[i+1])
    else:
      new_P[i], new_P[i+1] = P[i], P[i+1]
  return new_P

# Tests
#child_1, child_2 = crossover_pair_random('11111', '00000', 5, 1)

############################################################################
# Mutation functions.
############################################################################

def mutation(P, prob_mutation):
  """Mutation on whole population."""
  new_P = np.zeros_like(P)
  for i in range(len(P)):
    new_P[i] = _mutate_one(P[i], prob_mutation)
  # for x in new_P: assert(len(x) == 85)
  return new_P

def _mutate_one(strategy, prob_mutation):
  """Bit-flip mutation on one parent."""
  for i in range(len(strategy)):
    if np.random.rand() < prob_mutation:
      strategy = strategy[:i] + str(1-int(strategy[i])) + strategy[i+1:]
  return strategy
