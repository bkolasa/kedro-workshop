
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

Let's start from vizualizing our pipeline in order to investigate what we actually do.
The following command opens us a kedro viz instance and redirects us into the browser.
```
kedro viz
```

As a next step let's run ou full model training pipeline and create artifacts
```
kedro run
```
`Kedro run` command is highly customizable and we can choose what to run.
For example the `--pipeline` argument runs only a selected pipeline.
```
kedro run --pipeline de
```
`--to-outputs` runs the whole path of operations required to produce given output. 
```
kedro run --to-outputs="evaluation_plot"
```
As well, we can modify parameters configured in the *parameters.yml* file 
```
kedro run --params contamination_value:0.02
```

### Tasks

1. Add a new parameter to *IsolationForest* model in data science pipeline
Check how kedro viz diagram has changed and that you can specify it via command line. (10 min.)

## Tracking experiments with MLFlow

As a next step let's plug in the support for experiment tracking using MLFlow.
```
pipenv install kedro-mlflow
```

In order to start the work we need to generate a proper `mlflow.yml` file that stores the configuration 
and informs the *kedro-mlflow* plugin to send all the information into MLFlow database
```
kedro mlflow init
```

Let's run the MLFlow server and see how it looks like 
```
kedro mlflow ui
```

### Tasks

1. Add MLFlow support to project by installing *kedro-mlflow* plugin and initializing the MLFlow support. (5 min.)
2. Register *auc* score metric by adding new *kedro_mlflow.io.metrics.MlflowMetricDataSet* to data catalog (5 min.)
3. Add artifacts to experiments by using *type: kedro_mlflow.io.artifacts.MlflowArtifactDataSet* (5 min.)

# Deploying your model 

Kedro in the basic version offers building python *.whl* and *.egg* packages
```
kedro package 
```

However, we can leverage the container support by using *kedro-docker* plugin.
The following command generates for us a *Dockerfile*.
```
kedro docker init
```
Later, we can create an image that we can distribute.
```
kedro docker build
```

### Tasks
1. Package the Kedro project and try to load it as a Python module (5 min.)
2. Remove MlFlow support from our project by adjusting *catalog.yml* and create a docker image 
with the Kedro project and try to run it. (10 min.)
