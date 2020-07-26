"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages
from os import path
from io import open as io_open


TEST_REQUIRES = [
        # testing and coverage
        'pytest', 'coverage', 'pytest-cov', 'coveralls',
    ]

INSTALL_REQUIRES = ['numpy>=1.11.0',
                    'scipy>=0.17.0',
                    'scikit-learn>=0.20.0',
                    'matplotlib>=2.0.0',
                    'vtk>=8.1.0',
                    'nibabel',
                    'pillow',
                    'pandas']


here = path.abspath(path.dirname(__file__))


# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

__version__ = None
version_file = path.join(here, 'python/enigmatoolbox/_version.py')
with io_open(version_file, mode='r') as fd:
    exec(fd.read())


setup(

    name='enigmatoolbox',
    version=__version__,
    description='enigma tools for good people',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url='https://github.com/saratheriver/ENIGMA',
    author='enigmators',
    author_email='saratheriver@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='enigma surface connectivity atrophy',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    python_requires='>=3.5',
    install_requires=INSTALL_REQUIRES,
    extras_require={
        'test': TEST_REQUIRES + INSTALL_REQUIRES,
    },
    include_package_data=True,
    zip_safe=False,
    project_urls={  # Optional
        'Documentation': 'https://enigma-toolbox.readthedocs.io',
        #'Bug Reports': 'https://github.com/saratheriver/ENIGMA/issues',
        'Source': 'https://github.com/saratheriver/ENIGMA',
    },
    download_url='https://github.com/saratheriver/ENIGMA/archive/0.0.1.tar.gz'
)