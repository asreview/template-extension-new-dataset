# Template for extending ASReview with a new dataset

<a href="https://github.com/asreview/asreview"><img
src="https://img.shields.io/badge/ASReview-v1.0-%23ffcb05" alt="ASReview v1.0"
/></a>

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
class, and adding it to ASReview. To use this template, fork it and modify the
following files:

- A BaseDataSet object is defined in
    [`asreviewcontrib/dataset_name/your_dataset.py`](asreviewcontrib/dataset_name/your_dataset.py).
    Modify the path and this file to add your own dataset.

- Adding your BaseDataSet object to ASReview is done via the
    [`asreviewcontrib/dataset_name/__init__.py`](asreviewcontrib/dataset_name/__init__.py)
    file. This file should import your new class

- Adjust [`setup.py`](setup.py) with information about your dataset, and define
    the dataset entrypoint.

- Add your dataset to the `data` folder of the template.

For advanced usage- (e.g. adding multiple groups), check out the
[`BaseDataGroup`](https://asreview.readthedocs.io/en/latest/reference.html#asreview.datasets.BaseDataGroup)
in the example and at the documentation.

## License

MIT license
