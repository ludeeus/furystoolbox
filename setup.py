"""Setup configuration."""
import setuptools
from furystoolbox import __version__

with open("README.md", "r") as fh:
    LONG = fh.read()

REQUIRES = ['click>=7.0',
            'requests>=2.21.0',
            'PyGithub>=1.43.4']

setuptools.setup(
    name="furystoolbox",
    version=__version__,
    author="Joakim Sorensen",
    author_email="ludeeus@gmail.com",
    description="A collection of tools.",
    long_description=LONG,
    long_description_content_type="text/markdown",
    url="https://github.com/ludeeus/furystoolbox",
    install_requires=REQUIRES,
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    entry_points={
        'console_scripts': [
            'fury = furystoolbox.cli.cli:CLI'
        ]
    }
)
