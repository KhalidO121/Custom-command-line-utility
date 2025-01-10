from setuptools import setup

setup(
    name="custom-wc-tool",
    author="KhalidO",
    version="0.0.1",
    entry_points={
        "console_scripts": [
            "ccwc = main:main",
        ]
    },
)
