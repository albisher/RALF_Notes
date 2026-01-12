"""
RALF Note - Setup Configuration
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README for long description
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

setup(
    name="ralf-notes",
    version="2.0.0",
    author="Abdulrahman Albisher",
    author_email="abalbisher@gmail.com",
    description="AI-powered documentation generator for Obsidian",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/albisher/RALF_Notes",
    packages=find_packages(exclude=["tests", "archive", "roadmap"]),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Documentation",
        "Topic :: Text Processing :: Markup :: Markdown",
        "License :: Other/Proprietary License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    install_requires=[
        "typer>=0.9.0",
        "rich>=13.0.0",
        "ollama>=0.1.0",
        "psutil>=5.9.0",
        "PyYAML>=6.0",
        "watchdog>=2.2.0",
    ],
    entry_points={
        "console_scripts": [
            "ralf-notes=ralf_notes.cli:app",
        ],
    },
    include_package_data=True,
    keywords="documentation, obsidian, ai, llm, markdown, code-analysis",
    project_urls={
        "Bug Reports": "https://github.com/albisher/RALF_Notes/issues",
        "Source": "https://github.com/albisher/RALF_Notes",
        "Documentation": "https://github.com/albisher/RALF_Notes#readme",
    },
)
