import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="EM100-NanoExplorer", # Replace with your own username
    version="1.0",
    author="Christopher Rooney",
    author_email="ctr44@cornell.edu",
    description="Tool for reading data files from the Extech EM100",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NanoExplorer/EM100-Reader",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    scripts=[
        'em100/extechread'
    ],
    python_requires='>=3.8',
    include_package_data=True,
    install_requires=[
        "numpy",
        "pandas"
    ]
)