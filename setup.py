from setuptools import setup
from setuptools import find_namespace_packages

setup(
    name='asreview-template-dataset-extension',
    version='1.0',
    description='Example dataset extension',
    url='https://github.com/asreview/template-extension-new-dataset',
    author='ASReview team',
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
    include_package_data=True,
    python_requires='~=3.6',
    install_requires=[
        'asreview>=1.0',
    ],
    entry_points={
        "asreview.datasets": [
            "example_group = asreviewcontrib.dataset_name:ExampleDatasetGroup", # noqa
        ]

    },
    project_urls={
        'Bug Reports': 'https://github.com/asreview/template-extension-new-dataset/issues',  # noqa
        'Source': 'https://github.com/asreview/template-extension-new-dataset/',  # noqa
    },
)
