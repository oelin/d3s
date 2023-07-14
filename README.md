# Daily Dose of Data Science (d3s)

Get easily digestible summaries of data science topics straight to your terminal. d3s pulls from a list of over [5K topics](https://github.com/oelin/d3s-topics) in machine learning, statistics and probability theory. 

## Installation

You can install d3s with pip.

```sh
pip install d3s
```

## Usage

To get a random summary just run `d3s` in your terminal.

```sh
d3s
```

To get summaries every time you open your terminal, you could (for example), append `d3s` to your `~/.bashrc` file.

```sh
echo d3s >> ~/.bashrc
```

## Examples

```
Polynomial Regression
---------------------
In statistics, polynomial regression is a form of regression analysis
in which the relationship between the independent variable x and the
dependent variable y is modelled as an nth degree polynomial in x.
Polynomial regression fits a nonlinear relationship between the value
of x and the corresponding conditional mean of y, denoted E(y |x).
Although polynomial regression fits a nonlinear model to the data, as
a statistical estimation problem it is linear, in the sense that the
regression function E(y | x) is linear in the unknown parameters that
are estimated from the data.  For this reason, polynomial regression
is considered to be a special case of multiple linear regression. The
explanatory (independent) variables resulting from the polynomial
expansion of the "baseline" variables are known as higher-degree
terms. Such variables are also used in classification settings.
```

```
Raking
------
Raking (also called "raking ratio estimation" or "iterative
proportional fitting") is the statistical process of adjusting data
sample weights of a contingency table to match desired marginal
totals.
```

```
Kernel Method
-------------
In machine learning, kernel machines are a class of algorithms for
pattern analysis, whose best known member is the support-vector
machine (SVM). These methods involve using linear classifiers to solve
nonlinear problems. The general task of pattern analysis is to find
and study general types of relations (for example clusters, rankings,
principal components, correlations, classifications) in datasets.
```


## Coming Soon

* `.d3s` configuration file.
* LLM integrations.
* LaTeX formatting.
* Topic-specific summaries.
