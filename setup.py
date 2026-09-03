from setuptools import setup, find_packages


setup(

    name="autodiag-pro",

    version="1.0",

    packages=find_packages("src"),

    package_dir={
        "": "src"
    }

)
