from setuptools import setup, find_packages

with open("requirements.txt", "r") as f:
    requirements = f.readlines()

setup(
    name="cultivate",
    version="1.0.1",
    description="Become a productive member of your local community!",
    url="https://github.com/Edward-Knight/cultivate",
    author="Davy, Steve, Noelle, Ed, and Glen",
    packages=find_packages(),
    entry_points={
        "gui_scripts": [
            "cultivate = cultivate.main:main",
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    python_requires=">=3.6",
)
