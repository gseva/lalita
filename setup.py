#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    # metadata
    name='lalita',
    version='0.1',
    author='laliputienses',
    description='Yet another IRC bot, one where new functionality is simple ' \
                'to create just adding easy-to-write plugins.',
    license='GNU GPL v3 ',
    keywords='irc bot twisted plugin',
    url='https://launchpad.net/lalita/',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Framework :: Twisted',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python',
        'Topic :: Communications :: Chat :: Internet Relay Chat',
    ],

    # content
    package_dir={'': 'src'},
    packages=find_packages('src',
        exclude=['*.tests', '*.tests.*', 'tests.*', 'tests']),
    package_data={'lalita.plugins.randomer_utils': ['#pyar.log']},

    # scripts
    scripts=['src/lalita/ircbot.py'],

    # dependencies
    install_requires=[
        'beautifulsoup>=3.1.0.1',
        'chardet',
        'pyopenssl',
        'pysqlite',
        'twisted',
    ],
)
