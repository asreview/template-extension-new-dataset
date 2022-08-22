# Template for extending ASReview with a new dataset

![Badge](https://img.shields.io/badge/ASReview-v1.0-%23ffcb05)

ASReview has support for extensions, which enable you to seemlessly integrate
your own programs with the ASReview framework. This template can extent ASReview
with new data.

See the section
[Extensions](https://asreview.readthedocs.io/en/latest/extensions_dev.html#dataset-extensions)
on ReadTheDocs for more information on writing extensions.

## Getting started

Click the `Use this template` button and add/modify the algorithms. Install your
new dataset with

```bash
pip install .
```

or

```bash
pip install git+https://github.com/{USER_NAME}/{REPO_NAME}.git
```

and replace `{USER_NAME}` and `{REPO_NAME}` by your own details. 


## Usage

Adding a dataset to ASReview is done by extending the
[`BaseDataSet`](https://asreview.readthedocs.io/en/latest/reference.html#BaseDataSet)
class, adding it to a `BaseDataGroup` and finally, adding it to ASReview. To use
this template, fork it and modify the following files:

- A `BaseDataSet` object and a `BaseDataGroup` are defined in
    [`asreviewcontrib/dataset_name/your_dataset.py`](asreviewcontrib/dataset_name/your_dataset.py).
    Modify this file to add your own datasets. The `BaseDataSet` class should
    always be added to a `BaseDataGroup` object.

- Adding your `BaseDataGroup` object to ASReview is done via the
    [`asreviewcontrib/dataset_name/__init__.py`](asreviewcontrib/dataset_name/__init__.py)
    file. This file should import your `BaseDataGroup`.

- Adjust [`setup.py`](setup.py) with information about your dataset, and define
    the dataset entrypoint by adding your `BaseDataGroup`.

- Add your dataset to the `data` folder of the template.

For advanced usage, check out the
[`BaseDataGroup`](https://asreview.readthedocs.io/en/latest/reference.html#asreview.datasets.BaseDataGroup)
in the example and the documentation.

## License

MIT license
