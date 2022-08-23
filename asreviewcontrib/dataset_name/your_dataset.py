"""This module shows example dataset classes for creating your own dataset."""

from pathlib import Path

from asreview.datasets import BaseDataSet
from asreview.datasets import BaseDataGroup


class ExampleDatasetGroup(BaseDataGroup):
    """This is an example dataset group."""

    group_id = "example_group"
    description = "Example dataset group"

    def __init__(self):
        """Initialize the dataset group."""

        example_dataset_local = BaseDataSet(
                dataset_id="example_dataset_local",
                filepath=str(Path(Path(__file__).parent, 'data', 'your_dataset.csv')),  # noqa
                title="Example dataset (local)",
                description="This is an example dataset that is stored locally.",
                authors='Teijema, J.J. (2022)',
                topic='example datasets',
                link='ASReview.ai',
                reference=None,
                img_url=None,
                license='MIT',
                year='2022'
            )

        example_dataset_remote = BaseDataSet(
                dataset_id="example_dataset_remote",
                filepath='https://raw.githubusercontent.com/asreview/systematic-review-datasets/master/datasets/van_de_Schoot_2017/output/van_de_Schoot_2017.csv',  # noqa
                title="Example dataset (remote)",
                description="This is an example dataset that is stored remotely.",
                authors='Teijema, J.J. (2022)',
                topic=None,
                link=None,
                reference=None,
                img_url=None,
                license=None,
                year=None
            )

        super().__init__(example_dataset_local, example_dataset_remote)
