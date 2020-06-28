from setuptools import setup, find_packages

setup(
    name='in-the-air-tonight',
    version='1.0.0',
    description='Finds Covid-19 Contact Tracing protocol',
    author='Ben Smith',
    author_email='bensmith83',
    license='Copyright (C) 2020 Ben Smith',
    packages=find_packages(),
    install_requires=[
        'bluepy'
    ],
    entry_points={
        'console_scripts': [
            'in-the-air-tonight=in_the_air_tonight.in_the_air_tonight:main'
        ]
    },
)
