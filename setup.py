from setuptools import setup

setup(
    name='fancy',
    version='1.0.0b1',
    py_modules=['fancy'],
    install_requires=[
        'Click',
        'Pillow'
    ],
    entry_points={
        'console_scripts': [
            'fancy = fancy.__init__:fancy',
        ],
    },
)