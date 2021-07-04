from includes.constants import NLTK_DATA

import os
import pathlib
import subprocess
import shlex

from typing import List

from setuptools import setup
from setuptools.command.install import install as _install


def parse_reqs(requirements_file: str) -> List[str]:
    """Get requirements as a list of strings from the file."""
    with open(requirements_file) as reqs:
        return [r for r in reqs if not r.startswith("#")]

REQUIREMENTS = parse_reqs("requirements.txt")


class CustomInstallCommand(_install):
    def run(self):
        _install.do_egg_install(self)
        import nltk

        dependencies = ["stopwords", "averaged_perceptron_tagger", "wordnet"]
        for d in dependencies:
            nltk.download(d, download_dir=NLTK_DATA)


setup(
    name="sentence_to_noun",
    install_requires=REQUIREMENTS,
    version="0.0.1",
    description="Sentence to noun task for Silver Bullet",
    author="Ivan Gerov",
    license="",
    cmdclass={"install": CustomInstallCommand},
    setup_requires=["nltk"],
)
