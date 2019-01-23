from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import csv


def process_output(run_folder):
  """Process the 'raw output' produced by run_prisoners_ga().

  Arguments:
    run_folder should be a Path object. Typically, this will be the Path
        returned by run_prisoners_ga().

  File organization:
    <run_folder>/                   Specified by run_folder argument.
      parameter_summary.csv         Record of arguments for the run.
      raw_output/                   Contains results from this function.
        gen_0.csv
        gen_1.csv
        ...
      results_summary.csv           File produced by process_output().
  """
  # Major changes required for generalizing number of players. (Need to decide
  # what analysis makes sense. Smaller changes needed for when other currently
  # hard-coded values become arguments to run_prisoners_ga().
  raw_data_folder = run_folder / 'raw_output'
  # finds all files from a run and sorts them by generation
  file_names = sorted(raw_data_folder.glob('gen_*.csv'), key=_key_func)
  
  # initialize arrays of metrics for each generation throughout evolution
  averages = np.zeros(len(file_names))
  diff_bits = np.zeros(len(file_names))
  continue_cooperate = np.zeros(len(file_names))
  provocable = np.zeros(len(file_names))
  accept_apology = np.zeros(len(file_names))
  accept_rut = np.zeros(len(file_names))
  unique = np.zeros(len(file_names))
  begin_cooperate = np.zeros(len(file_names))
  unique_scores = np.zeros(len(file_names))

  # Loop through each generation/file and calculate metrics
  for i,file_name in enumerate(file_names):
    scores = []
    population = []
    with open(file_name, 'r') as csvFile:
      reader = csv.reader(csvFile)
      for row in reader:
        if row == []:
          continue
        else:
          scores.append(float(row[1]))
          population.append(row[0])
    averages[i] = np.average(np.asarray(scores))
    diff_bits[i], continue_cooperate[i], begin_cooperate[i], provocable[i], \
        accept_apology[i], accept_rut[i] = _population_qualities(population)
    unique[i] = len(set(population))
    unique_scores[i] = len(set(scores))

  # normalize scores by maximum average population score
  norm_averages = averages/_max_score(len(population), 64)
  results = np.stack([norm_averages, unique, unique_scores, diff_bits, continue_cooperate, begin_cooperate, 
                      provocable, accept_apology, accept_rut])
  # save summary file
  with open(run_folder / 'results_summary.csv', 'w+', newline = '\n') as csv_file:
    csv_writer = csv.writer(csv_file) 
    csv_writer.writerows(results)

###############################################################################

def _max_score(population_size, length_of_interaction):
  # This depends on hard-coded values that will become arguments to
  # run_prisoners_ga() in the next version.
  return (population_size-1) * 3 * length_of_interaction


def _key_func(x):
  """Returns the generation number portion of filename."""
  return int(x.stem[len('gen_') : ])


def _population_qualities(population):
  # Takes in array of strategies, quantifies the proportion of them that 
  # exhibit these qualities: continuing cooperation, being provocable, 
  # cooperating when mutual cooperation is restored (accept apology), 
  # and accepting a rut of defections
  
  continue_cooperate = 0
  provocable = 0
  accept_apology = 0
  accept_rut = 0
  begin_cooperate = 0
  strategy_arr = np.zeros((len(population), 85))
  
  for i, strategy in enumerate(population):
    if strategy[int('111111',2)]=='1':
        continue_cooperate +=1
    if strategy[64 + int('1111',2)]=='1' and strategy[80 + int('11',2)]=='1' and strategy[84]=='1':
        begin_cooperate += 1
    if strategy[int('111110',2)]=='0':
        provocable += 1
    if strategy[int('101111',2)]=='1' or strategy[int('100111',2)]=='1':
        accept_apology += 1
    if strategy[0]=='0':
        accept_rut += 1
    strategy_arr[i,:] = np.array(list(strategy))
  #calculate proportions of qualities in population
  # number of bits that not all of the population members have in common (eg.
  # sums of bits that are not either 0 or 20)
  diff_bits = np.sum(np.all([np.sum(strategy_arr,axis = 0) < 20, 
                             np.sum(strategy_arr,axis = 0)>0], axis = 0))
  continue_cooperate = continue_cooperate/len(population)
  begin_cooperate = begin_cooperate/len(population)
  provocable = provocable/len(population)
  accept_apology = accept_apology/len(population)
  accept_rut = accept_rut/len(population)
  return(diff_bits, continue_cooperate, begin_cooperate, provocable, 
         accept_apology, accept_rut)
  
# Tests
#population = [always_defect(), tit_for_tat()]
#continue_cooperate, begin_cooperate, provocable, accept_apology, accept_rut = _population_qualities(population)
