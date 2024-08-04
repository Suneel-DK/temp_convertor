# setup.py
from setuptools import setup, find_packages

setup(
    name='temp_converter',
    version='0.1',
    author='Suneel D.K',
    author_email='suneelkaliyannan@gmail.com',
    description='A simple temperature converter library',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Suneel-DK/temp_convertor',  
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
