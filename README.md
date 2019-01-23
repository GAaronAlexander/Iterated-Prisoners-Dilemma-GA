# Evolving Strategies for Iterated Prisoner's Dilemma

Uses a genetic algorithm to evolve strategies for playing iterated prisoner's dilemma against other evolving strategies to model the dynamics of a population of individuals "learning" to maximize their individual gain.

## Usage

**Required Libraries:** NumPy, MatPlotLib, Glob, CSV, Pandas

**Workflow:**

1. Run the GA
```
run_prisoners_ga(0, max_gen = 20000)

```
2. Run IPD_output_process to take outputs from GA and turn into summary file with metrics on each generation throughout evolution.

3. Run results_analysis to plot metrics in summary file

![image](https://user-images.githubusercontent.com/44376656/51433561-ec820600-1c01-11e9-9f16-2561234b2713.png)
