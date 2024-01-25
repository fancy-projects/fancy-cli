from setuptools import setup, find_packages

from setuptools import setup, find_packages

setup(
    name='src',
    version='1.0.0-b1',
    packages=find_packages(),
    install_requires=[
        'Click',
        'Pillow',
        'pyinstaller'
    ],
    package_data={'src': ['folders/*.icns']},
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'src = src.__init__:src',
        ],
    },
)
