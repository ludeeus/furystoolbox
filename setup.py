"""Setup configuration."""
import setuptools
from furystoolbox import __version__

with open("README.md", "r") as fh:
    LONG = fh.read()
setuptools.setup(
    name="furystoolbox",
    version=__version__,
    author="Joakim Sorensen",
    author_email="ludeeus@gmail.com",
    description="A collection of tools.",
    long_description=LONG,
    long_description_content_type="text/markdown",
    url="https://github.com/ludeeus/furystoolbox",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
