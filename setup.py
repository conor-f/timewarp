from setuptools import (
    find_packages,
    setup
)

INSTALL_REQUIRES = [
    'python-dateutil'
]

setup(
    name='timewarp',
    description='datetime wrapper that allows you to specify datetimes using a succinct shorthand.',
    version='0.1.0',
    url='https://github.com/conor-f/timewarp',
    python_requires='>=3.6',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=INSTALL_REQUIRES,
    entry_points={
        'console_scripts': [
        ]
    }
)
