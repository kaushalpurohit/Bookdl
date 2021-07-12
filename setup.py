from setuptools import setup, find_packages

setup(
    name='Bookdl',
    packages=find_packages(),
    author='Kaushal Purohit',
    author_email='kpurohit43@gmail.com',
    description='Download books',
    long_description='Download books from pdfdrive.',
    url='http://github.com/kaushalpurohit/Bookdl',
    scripts=['scripts/Bookdl'],
    version='0.1.4',
    license='MIT',
    install_requires=['cloudscraper', 'bs4', 'html5lib', 'selenium', 'termcolor'],
)
