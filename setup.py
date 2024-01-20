from setuptools import setup, find_packages

setup(
    name='fancy',
    version='1.0.0-b1',
    packages=find_packages(),
    package_data={'': ['fancy/folders/*.icns']},
    include_package_data=True,
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