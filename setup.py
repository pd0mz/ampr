import codecs
import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
with codecs.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='ampr',
    version='1.0.0',
    description='Amateur Packet Radio API client',
    long_description=long_description,
    url='https://github.com/pd0mz/ampr',
    author='Wijnand Modderman-Lenstra',
    author_email='maze@pyth0n.org',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
    ],
    keywords='ampr amateur packet radio api',
    py_modules=['ampr.py'],
    install_requires=['requests'],
)
