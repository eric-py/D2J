from setuptools import setup, find_packages

setup(
    name="D2J",
    version="0.2.0",
    author="Eric",
    description="A module for converting dates between Gregorian and Jalali calendars.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/eric-py/D2J",  # Main project URL
    project_urls={
        "GitHub": "https://github.com/eric-py/D2J",
        "Bug Tracker": "https://github.com/eric-py/D2J/issues",
    },
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[],
    keywords=['jalali', 'shamsi', 'gregorian', 'date', 'conversion', 'calendar'],
)