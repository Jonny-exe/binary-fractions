from setuptools import setup, find_packages

classifiers = []

setup(
    name="Binary fractions",
    version="0.0.1",
    description="A package to handle binary fractions",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Jonny-exe/binary-fractions",
    author="Jonny-exe",
    author_email="",
    license="MIT",
    classifiers=classifiers,
    keywords="binary fractions binary-fractions",
    packages=find_packages(),
    install_requires=[""],
)
