from setuptools import setup, find_packages

setup(
    name='logging_package',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',  # Add any dependencies here
    ],
)