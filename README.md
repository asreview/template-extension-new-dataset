# Template for extending ASReview with a new dataset

ASReview has support for extensions, which enable you to seemlessly integrate
your own programs with the ASReview framework. This template can extent ASReview
with new data.

See the section [Extensions](https://asreview.readthedocs.io/en/latest/API/extensions_dev.html?highlight=extension) 
on ReadTheDocs for more information on writing extensions.

## Getting started

Click the `Use this template` button and add/modify the algorithms. Install 
your new dataset with

```bash
pip install .
```

or

```bash
pip install git+https://github.com/{USER_NAME}/{REPO_NAME}.git
```

and replace `{USER_NAME}` and `{REPO_NAME}` by your own details. 


## Usage

The new dataset is defined in
[`asreviewcontrib/dataset_name/your_dataset.py`](asreviewcontrib\dataset_name\your_dataset.py)
and can be used as a new dataset. 

By supplying the `from_config()` method with a
config object, a new DataSet object is created, and integrated to ASReview. See
[asreview.datasets.BaseDataSet.from_config](https://asreview.readthedocs.io/en/latest/API/generated/asreview.datasets.BaseDataSet.html#asreview.datasets.BaseDataSet.from_config)
for more information on this function.

[`setup.py`](setup.py) contains the code needed for integration into ASReview.

[`asreviewcontrib/dataset_name/__init__.py`](asreviewcontrib/dataset_name/__init__.py) 
contains directions for loading the dataset module.

## License

MIT license
