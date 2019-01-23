import numpy as np
import pandas
import matplotlib.pyplot as plt

def plot_results(run_folder):
  # plots results from results summary file
  results = pandas.read_csv(run_folder / 'results_summary.csv', header = None)
  norm_averages = np.array(results.iloc[0])
  unique = np.array(results.iloc[1])
  unique_scores = np.array(results.iloc[2])
  diff_bits = np.array(results.iloc[3])
  continue_cooperate = np.array(results.iloc[4])
  begin_cooperate = np.array(results.iloc[6])
  provocable = np.array(results.iloc[5])
  accept_apology = np.array(results.iloc[7])
  accept_rut = np.array(results.iloc[8])
  
  gen = np.arange(0,len(norm_averages))
  plt.plot(gen,norm_averages)
  plt.xlabel('Generation')
  plt.ylabel('Normalized Average Score')
  plt.show()
  plt.hist(unique)
  plt.xlabel('Count')
  plt.ylabel('Number of Unique Strategies')
  plt.show()
  plt.hist(diff_bits, bins = np.arange(0,85,5))
  plt.xlabel('Count')
  plt.ylabel('Number of Different Bits')
  plt.show()
  plt.hist(unique_scores, bins = np.arange(0,20,1))
  plt.xlabel('Count')
  plt.ylabel('Number of Unique Scores')
  plt.show()
  
  gs = plt.GridSpec(3, 4)
  fig = plt.gcf()
  ax1 = fig.add_subplot(gs[0, 0:2])
  ax2 = fig.add_subplot(gs[0,2:], sharey = ax1)
  ax3 = plt.subplot(gs[1,0:2])
  ax4 = plt.subplot(gs[1,2:])
  ax5 = plt.subplot(gs[2,1:3])
  gs.tight_layout(fig)
  ax1.plot(gen, norm_averages, gen, continue_cooperate)
  ax1.set_title('Continue Cooperating')
  ax2.plot(gen, norm_averages, gen, begin_cooperate)
  ax2.set_title('Begins Cooperating')
  ax3.plot(gen, norm_averages, gen, provocable)
  ax3.set_title('Provocable')
  ax3.set_xlabel('Generation')
  ax3.set_ylabel('Proportion of Population/Average Score')
  ax4.plot(gen, norm_averages, gen, accept_apology)
  ax4.set_title('Accepts Apologies')
  ax4.set_xlabel('Generation')
  ax5.plot(gen, norm_averages, gen, accept_rut)
  ax5.set_title('Accepts Ruts')
  ax5.set_xlabel('Generation')




