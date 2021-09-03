import setuptools
from setuptools import find_packages
import os


try:
    # https://stackoverflow.com/questions/4519127/setuptools-package-data-folder-location
    os.symlink(os.path.join(os.pardir, 'v1-dev'), 'fire/data')
    setuptools.setup(
        name='fire-spark',
        version='1.0',
        author='Antoine Amend',
        author_email='antoine.amend@databricks.com',
        description='Mapping fire model into spark operations',
        long_description_content_type='text/markdown',
        url='https://github.com/SuadeLabs/fire',
        packages=find_packages(where='.', include=['fire']),
        package_data={'fire': ['data/*.json']},
        include_package_data=True,
        classifiers=[
            'Programming Language :: Python :: 3',
            'Operating System :: OS Independent',
        ],
    )
finally:
    os.unlink('fire/data')
