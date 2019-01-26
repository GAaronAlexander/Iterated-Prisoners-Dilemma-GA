### Run iterated prisoner's dilemma with default settings 
from Prisoners_GA import *
from process_output import *
from results_plotting import *
from premade_strategies import *
from IPD_functions import *
from GA_functions import *

run_folder = run_prisoners_ga(seed = 0, data_folder = None)
process_output(run_folder)
plot_results(run_folder)



