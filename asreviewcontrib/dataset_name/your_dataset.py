from asreview.datasets import BaseDataSet
from asreview.datasets import BaseDataGroup

class YourDataGroup(BaseDataGroup):
    group_id = "your_data_group"
    description = "A new data group with my awesome datasets."

    def __init__(self):

        dataset = BaseDataSet.from_config({
            "dataset_id": "your_data_id",
            "url": "",
            "reference": "",
            "link": "",
            "license": "",
            "title": "Your Data",
            "authors": [
            "Jane Doe",
            "John Doe"
            ],
            "year": 2021,
            "topic": "Your topic",
            "final_inclusions": True,
            "title_abstract_inclusions": False
        }
        )

        super(YourDataGroup, self).__init__(dataset)
        # pass multiple datasets to init if there are more datasets
