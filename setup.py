from setuptools import setup

from beancount_bot_costflow import __VERSION__

with open("requirements.txt", "r") as f:
    install_requires = f.read().splitlines()

with open("README.md", "r", encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='beancount_bot_costflow',
    version=__VERSION__,
    packages=['beancount_bot_costflow'],
    package_data={'': ['costflow-parser.js']},
    url='https://github.com/kaaass/beancount_bot_costflow',
    install_requires=install_requires,
    license='GPLv3',
    author='KAAAsS',
    author_email='admin@kaaass.net',
    description='A plugin adds costflow syntax supports for beancount_bot',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
