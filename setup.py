from pathlib import Path

from setuptools import setup

__VERSION__ = "1.1.0"

root = Path(__file__).parent
long_description = (root / "README.md").read_text()

setup(
    name='beancount_bot_costflow',
    version=__VERSION__,
    packages=['beancount_bot_costflow'],
    package_data={'': ['costflow-parser.js']},
    url='https://github.com/kaaass/beancount_bot_costflow',
    install_requires=[
        'beancount_bot>=1.0.1',
    ],
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
