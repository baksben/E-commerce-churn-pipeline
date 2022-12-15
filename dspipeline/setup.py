from setuptools import setup, find_packages
#######
# Only needed if the version is imported from the library
# import os
# import sys

# base_dir = os.path.dirname(__file__)
# src_dir = os.path.join(base_dir, 'src')
# sys.path.insert(0, src_dir)

# import library_example
#######

def get_requirements(requirements_path='requirements.txt'):
    with open(requirements_path) as fp:
        return [x.strip() for x in fp.read().split('\n') if not x.startswith('#')]

# for the version you can either put here a string with the version number
# or you can create a variable called __version__ inside the __init__.py from
# the src/your_library folder that has a string with the version as a string.
setup(
    version='0.1.0',
    description='Module to predict diabetes melitus',
    author='Ben | David ',
    name='dspipeline',
    license='MIT',
    packages=find_packages(where='diabetesoop', exclude=['tests']),
    # package_dir={'': 'diabetes'},
    install_requires=get_requirements(),
    setup_requires=['pytest-runner', 'wheel'],
    url='',
    classifiers=[
        'Programming Language :: Python :: 3.7.10'
    ]
)
