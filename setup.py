from setuptools import setup

classifiers = []

setup(
    name="binary_fractions",
    version="1.0.1",
    description="A Python package for floating-point binary fractions. Do math in base 2!",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Jonny-exe/binary-fractions",
    author="Jonny-exe",
    author_email="",
    license="GPL3+",
    classifiers=classifiers,
    keywords="binary fractions python python3 floating-point high-precision base-2 floating-point-arithmetic binary-fractions twos-complement",
    install_requires=[""],
    packages=["binary_fractions"]
)
