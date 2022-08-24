from setuptools import find_packages, setup

# basic setup, to be improved in the future
setup(
    name="pynlp-lib",
    packages=find_packages(),
    version='0.1.3',
    description="A Comprehensive NLP Library for Python",
    author="Yujian Tang",
    license="MIT",
    install_requires=["requests", "deepgram-sdk"],
    setup_requires=[],
    tests_requires=[],
    test_suites='tests',
    keywords='nlp text processing transcription ai nlu nlg asr'
)