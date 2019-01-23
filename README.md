# Evolving Strategies for Iterated Prisoner's Dilemma

Uses a genetic algorithm to evolve strategies for playing iterated prisoner's dilemma against other evolving strategies to model the dynamics of a population of individuals "learning" to maximize their individual gain.

## Usage

**Required Libraries:** NumPy, MatPlotLib, Glob, CSV, Pandas

**Example Run:**
Uses default settings (random initial population, population size of 20, runs for 100 generations, a probability of crossover of 0.8 and a probability of mutation of 0.001, tournament selection with tournament size of 2, and one-point crossover).
```
run_folder = run_prisoners_ga(seed = 0, data_folder = Path('IPD_outputs'))
process_output(run_folder)
plot_results(run_folder)

```
![image](https://user-images.githubusercontent.com/44376656/51590907-718a4b00-1ea0-11e9-92ce-def500fddb0a.png)

