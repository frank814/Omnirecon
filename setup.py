"""
Setup script for OmniRecon
Author: Frank Arthur
Version: 3.0.0
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README for long description
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

setup(
    name="omnirecon",
    version="3.0.0",
    author="Frank Arthur",
    author_email="frank814@github.com",
    description="Modular Open Source Intelligence Framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/frank814/omnirecon",
    project_urls={
        "Bug Reports": "https://github.com/frank814/omnirecon/issues",
        "Source": "https://github.com/frank814/omnirecon",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Topic :: Security",
        "Topic :: System :: Networking",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.31.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.0.0",
        ],
        "api": [
            "fastapi>=0.100.0",
            "uvicorn>=0.23.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "omnirecon=omnirecon.main:main",
        ],
    },
    keywords="osint security intelligence reconnaissance cybersecurity",
    license="MIT",
)
