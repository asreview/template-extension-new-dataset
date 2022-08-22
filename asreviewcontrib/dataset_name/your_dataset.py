"""This module shows example dataset classes for creating your own dataset."""

import os
from pathlib import Path

from asreview.datasets import BaseDataSet
from asreview.datasets import BaseDataGroup


class ExampleDatasetLocal(BaseDataSet):
    """This is an example dataset that is stored locally."""

    __filepath__ = os.getcwd()

    def __init__(self):
        """Initialize the dataset."""
        super().__init__(
            dataset_id="example_dataset_local",
            filepath=str(Path(self.__filepath__, 'data', 'your_dataset.csv')),
            title="Example dataset (local)",
            description="This is an example dataset that is stored locally.",
            authors=None,
            topic=None,
            link=None,
            reference=None,
            img_url=None,
            license=None,
            year=None
        )


class ExampleDatasetRemote(BaseDataSet):
    """This is an example dataset that is stored remotely."""

    def __init__(self):
        """Initialize the dataset."""
        super().__init__(
            dataset_id="example_dataset_remote",
            filepath='https://raw.githubusercontent.com/asreview/systematic-review-datasets/master/datasets/van_de_Schoot_2017/output/van_de_Schoot_2017.csv',  # noqa
            title="Example dataset (remote)",
            description="This is an example dataset that is stored remotely.",
            authors='van de Schoot, J. (2017)',
            topic=None,
            link=None,
            reference=None,
            img_url=None,
            license=None,
            year=None
        )


class ExampleDatasetGroup(BaseDataGroup):
    """This is an example dataset group."""

    group_id = "example_dataset_group"
    description = "Example dataset group"

    def __init__(self):
        """Initialize the dataset group."""
        super().__init__(ExampleDatasetLocal(), ExampleDatasetRemote())
