"""Another unicode transliteration library.
"""
from setuptools import setup, find_packages

__version__ = '0.5.1'

setup(
    name="unitrans",
    version=__version__,
    author="Alexey Kinëv",
    author_email='rudy@05bit.com',
    url='https://github.com/05bit/python-unitrans',
    description=__doc__,
    # long_description=__doc__,
    license='MIT',
    zip_safe=False,
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT',
        'Programming Language :: Python :: 3',
    ],
)
