from setuptools import setup


setup(
    name='my_extension',
    version='0.1.0',
    description='My Extension',
    author='My Name',
    entry_points={
        'blackfennec.extension': [
            'my_extension = my_extension'
        ]
    })
