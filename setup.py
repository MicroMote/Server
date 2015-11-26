from setuptools import setup

project = "MicroMote"

setup(
    name=project,
    version="indev",
    url="https://github.com/MicroMote",
    description="A remote for your TV using a RPi",
    packages=["MicroMote"],
    test_suite="tests",
    zip_safe=False,
)

