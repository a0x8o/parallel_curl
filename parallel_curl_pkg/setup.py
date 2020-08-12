import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='parallel_curl',
     version='0.1',
     scripts=['parallel_curl'] ,
     description="Parallel cURL utility",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/a0x8o/parallel_curl",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
     ],
 )
