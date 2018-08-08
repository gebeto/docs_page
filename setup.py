import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="docs_page",
    version="0.0.1",
    author="Slavik Nychkalo",
    author_email="slavik.nychkalo@gmail.com",
    description="Generate docs page from docstring",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gebeto/docs_page",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)