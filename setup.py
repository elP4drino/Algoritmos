from setuptools import setup, find_packages

setup(
    name='algoritmos',
    version='1.0',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'ply',
        'matplotlib'
    ],
    author=['Ruben Vazquez'],
    author_email=['developerrv1024@gmail.com'],
    description='Algorithms for Machine Learning',
    license='MIT',
    keywords='algorithms  machine-learning programming',
    url='https://github.com/elP4drino/Algoritmos.git',
)