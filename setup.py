from setuptools import setup

setup(
    name='cgsearch',
    version='0.1',
    long_description=__doc__,
    scripts=['scripts/parse_cghub_metadata.py'],
    zip_safe=False,
    install_requires=[
        'lxml',
        'requests',
    ],
)
