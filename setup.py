from forx.convert import __version__
from setuptools import setup


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="forx",
    version=__version__,
    author="Gabe Banks",
    author_email="gabriel.t.banks@gmail.com",
    description="a command line tool for checking exchange rates between currencies, both crypto and fiat.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    keywords="forx forex finance crypto exchange currency conversion",
    url="https://github.com/Gbox4/forx",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    packages=["forx"],
    install_requires=["requests"],
    entry_points={"console_scripts": ["forx=forx:main"]},
    python_requires=">=3.6",
)
