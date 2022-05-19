
# Kedro project including MLFlow experiment tracking
## Prerequisites
We will be using *pipenv* virtual environment. Let's install it first
```
pip install pipenv
```

Then we want to create a new project and install required dependencies
```
pipenv install
```
This command will install `kedro`, `mlflow`, 'kedro-viz` and other required packages.
Finally, we can enter the virtual env shell.
```
pipenv shell
```

## Data input for workshop
We will work on transaction credit risk data which can be downloaded from [here](https://github.com/Fraud-Detection-Handbook/simulated-data-transformed/tree/main/data)

# Working with Kedro
```
kedro viz
```



```
kedro run
```

```
kedro run --pipeline de
```

```
kedro run --to-outputs="evaluation_plot"
```

```
kedro run --params contamination_value:0.02
```

## Tracking experiments with MLFlow
```
kedro mlflow init
```

```
kedro mlflow ui
```


# Deploying your model 
```
kedro package 
```

```
kedro docker init
```

```
kedro docker build
```


Challenges:
Add plot as artifact
Add new metric
Add simple grid search in notebook
```
```
