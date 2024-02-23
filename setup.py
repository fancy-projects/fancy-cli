from setuptools import setup, find_packages

from setuptools import setup, find_packages

setup(
    name='fancy',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'Typer[all]',
        'Pillow',
        'numpy'
    ],
    package_data={'fancy': ['folders/*.icns']},
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'fancy = fancy.__init__:app',
        ],
    },
)
