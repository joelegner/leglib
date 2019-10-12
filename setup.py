import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="leglib",
    version="0.1.0",
    author="Joseph M. Legner",
    author_email="joelegner@gmail.com",
    description="My package of personal code librarites",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/joelegner/leglib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires = ['numpy', 'jinja2'],
    python_requires='>=3.6',
)
