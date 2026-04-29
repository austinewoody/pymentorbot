from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pymentorbot",
    version="0.1.1",
    author="Austine Onwubiko",
    description="A beginner-friendly Python concept explainer for keywords, built-ins, errors, and programming features.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/austinewoody/pymentorbot",
    packages=find_packages(),
    py_modules=["pymentorbot_cli"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Intended Audience :: Education",
        "Topic :: Education",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "pymentorbot=pymentorbot_cli:main",
        ]
    },
)
