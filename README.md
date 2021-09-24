# Template for extending ASReview with a new dataset

ASReview has support for extensions, which enable you to seemlessly integrate
your own programs with the ASReview framework. This template can extent ASReview
with new data.

See the section [Extensions](https://asreview.readthedocs.io/en/latest/extensions/extension_development.html?highlight=extension) 
on ReadTheDocs for more information on writing extensions.

## Getting started

Click the `Use this template` button and add/modify the algorithms. Install 
your new classifier with

```bash
pip install .
```

or

```bash
pip install git@github.com:{USER_NAME}/{REPO_NAME}.git
```

and replace `{USER_NAME}` and `{REPO_NAME}` by your own details. 


## Usage

The new dataset is defined in
[`asreviewcontrib\dataset_name\your_dataset.py`](asreviewcontrib\dataset_name\your_dataset.py) 
and can be used as a new dataset.

`setup.py` contains the code needed for integration into ASReview.

`__init__.py` contains directions for loading the dataset module.

## License

MIT license
