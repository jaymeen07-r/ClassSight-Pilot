"""
ClassSight-Pilot: AI-Based Automatic Report & Document Generator
Setup configuration for package distribution
"""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="classsight-pilot",
    version="1.0.0",
    author="Jaymeen N. Vaghela",
    author_email="jaymeenvaghela07@gmail.com",
    description="AI-Based automatic report generation system for schools and colleges",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jaymeen07-r/ClassSight-Pilot",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Education",
        "Topic :: Education",
    ],
    python_requires=">=3.11",
    install_requires=[
        "pandas>=2.1.4",
        "numpy>=1.26.3",
        "sqlalchemy>=2.0.23",
        "fastapi>=0.109.0",
        "pydantic>=2.5.3",
        "python-jose>=3.3.0",
        "passlib>=1.7.4",
        "python-dotenv>=1.0.0",
    ],
)
