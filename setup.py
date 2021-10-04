from setuptools import setup
from setuptools import find_namespace_packages

setup(
    name='asreview-filled-example-dataset-extension',
    version='0.2',
    description='Filled example dataset extension',
    url='https://github.com/JTeijema/Test-Dataset-Extension',
    author='JTeijema',
    author_email='asreview@uu.nl',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='systematic review',
    packages=find_namespace_packages(include=['asreviewcontrib.*']),
    python_requires='~=3.6',
    install_requires=[
        'asreview>=0.16',
    ],

    entry_points={
        "asreview.datasets": [
            "filledDataSet = asreviewcontrib.dataset_name.your_dataset:YourDataGroup"
        ]

    },

    project_urls={
        'Bug Reports': 'https://github.com/asreview/template-extension-new-dataset/issues',
        'Source': 'https://github.com/asreview/template-extension-new-dataset/',
    },
)
