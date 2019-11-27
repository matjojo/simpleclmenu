import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simpleclmenu",
    packages=['simpleclmenu'],
    version="1.0.0",
    author="matjojo",
    author_email="",
    description="Simple commandline menu for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/matjojo/simpleclmenu",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
    ],
    python_requires='>=3.7',
)
