from asreview.datasets import BaseDataSet
from asreview.datasets import BaseDataGroup
from pathlib import Path


class example_dataset_local(BaseDataSet):
    """
    This is an example dataset that is stored locally.
    """

    import os
    __filepath__ = os.getcwd()

    def __init__(self):
        super().__init__(
            dataset_id="example_dataset_local",
            filepath=Path(self.__filepath__, 'data', 'your_dataset.csv'),
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


class example_dataset_remote(BaseDataSet):
    """
    This is an example dataset that is stored remotely.
    """

    def __init__(self):
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


class example_dataset_group(BaseDataGroup):
    """
    This is an example dataset group.
    """

    group_id = "example_dataset_group"
    description = "Example dataset group"

    def __init__(self):
        super().__init__()

        self.append(example_dataset_local())
        self.append(example_dataset_remote())


class example_dataset_group_2(BaseDataGroup):
    """
    This is an example dataset group.
    """

    group_id = "example_dataset_group_2"
    description = "Example dataset group"

    def __init__(self):
        super().__init__(example_dataset_local(), example_dataset_remote())