from setuptools import setup, find_packages

setup(
    name='phpparser',
    version='1.0',
    packages=find_packages(exclude=['examples']),
    include_package_data=True
)