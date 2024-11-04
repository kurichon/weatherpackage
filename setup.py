from setuptools import setup, find_packages

setup(
    name="weather_package",
    version="0.1.1",
    description="A package to query weather based on location and date.",
    author="그리천",
    packages=find_packages(),  # Automatically finds packages in the directory
    install_requires=[
        "requests",
        "konlpy",
        "python-dotenv",
        "dateparser",
        "korean-romanizer"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)