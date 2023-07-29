from setuptools import setup

setup(
    name='flask-server',
    version='1.0.0',
    py_modules=['flask-server'],
    install_requires=[
        'flask==2.3.2',
        'flask-restx==1.1.0'
    ],
    entry_points={
    })
