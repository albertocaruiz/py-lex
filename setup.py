from setuptools import setup
import json
from os import path
here = path.abspath(path.dirname(__file__))
package = json.load(open(path.join(here, 'package.json')))

setup(
    name=package['name'],
    version=package['version'],
    author='Christopher Brown',
    author_email='chrisbrown@utexas.edu',
    packages=['lexicons', 'lexicons.lib'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    entry_points={
        'console_scripts': [
            'liwc = lexicons.liwc:main'
        ]
    },
)
