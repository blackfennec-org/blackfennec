from setuptools import setup


setup(
    name='template',
    version='0.1.0',
    description='Extension Template',
    author='My Name',
    entry_points={
        'blackfennec.extension': [
            'template_extension = template_extension'
        ]
    })
