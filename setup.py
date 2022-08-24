from setuptools import find_packages, setup

# basic setup, to be improved in the future
setup(
    name="pynlpl",
    packages=find_packages(),
    version='0.1.1',
    description="A Comprehensive NLP Library for Python",
    author="Yujian Tang",
    license="MIT",
    install_requires=["requests", "deepgram-sdk"],
    setup_requires=[],
    tests_requires=[],
    test_suites='tests'
)