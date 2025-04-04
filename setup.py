from setuptools import setup, find_packages

setup(
    name="image_processing_package",
    version="0.0.1",
    author="Priscila Souza",
    author_email="priscilamsouza1826@gmail.com",
    description="Um pacote para processamento de imagens.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/pri-souza22/image-processing-package",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "opencv-python",
        "matplotlib"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License : MIT ",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
