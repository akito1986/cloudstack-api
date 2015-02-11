# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os
import shutil

VERSION = '0.1.1'

setup(name='cstack-api',
      version=VERSION,
      packages=['cstack','cstack.compute'],
      include_package_data=True,
      install_requires=['setuptools',
                        'httplib2',
                        'simplejson',
                        'argparse',
                        'prettytable==0.5',
                        'parsedatetime==0.8.7',
                        'lxml',
                        ],
      entry_points={
        'console_scripts': [
            'cstack-api = cstack.compute.shell:main'
            ]
        }
      )
