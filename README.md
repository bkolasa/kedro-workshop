
# Kedro project including experiment tracking
## Prerequisites
The main branch of this project contains the content of a finished workshop. If we want to start workshop from scratch firstly we need to switch to `start_from_scratch` git branch.
```
git switch start_from_scratch
```

We will be using *pipenv* virtual environment. Let's install it first
```
pip install pipenv
```

Then we want to install all of required dependencies.
```
pipenv install
```
This command will install `kedro`,'kedro-viz` and other required packages. 
Finally, we can enter the virtual env shell.
```
pipenv shell
```

## Bootstrapping a new Kedro project
During the workshop we will work on an example project provided by Kedro. We can initialize it by executinh following command.
```
kedro new --starter=spaceflights
```

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
kedro run --pipeline data_processing
```
`--to-outputs` runs the whole path of operations required to produce given output. 
```
kedro run --to-outputs="evaluation_plot"
```
`--from-inputs` runs the whole path starting from given dataset node
```
kedro run --from-inputs=model_input_table
```

As well, we can modify parameters configured in the *parameters.yml* file 
```
kedro run --params model_options.test_size=0.1
```

### Tasks

1. Add a new parameter to linear regression model in data science pipeline (ex. `n_jobs` parameter of `LinearRegressor`)
Check how kedro viz diagram has changed and that you can specify it via command line. (10 min.)

## Tracking experiments

Starting experiment tracking in Kedro requires modifying the project. Firstly, we need to setup the store for our experiment.

1. Paste this snippet into `settings.py`
```python
from kedro_viz.integrations.kedro.sqlite_store import SQLiteStore
from pathlib import Path

SESSION_STORE_CLASS = SQLiteStore
SESSION_STORE_ARGS = {"path": str(Path(__file__).parents[2] / "data")}
```
2. Create directory for tracking artifacts
```
mkdir -p data/09_tracking
```
3. Add metric artifacts into the catalog
```
metrics:
  type: tracking.MetricsDataSet
  filepath: data/09_tracking/metrics.json

companies_columns:
  type: tracking.JSONDataSet
  filepath: data/09_tracking/companies_columns.json
```
4. Modify the pipeline and nodes. See https://docs.kedro.org/en/stable/experiment_tracking/index.html#modify-your-nodes-and-pipelines-to-log-metrics for more.

### Tasks
1. Register more parameters 
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
