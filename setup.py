import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='sessions',  
     version='1.0.0',
     scripts=['sessions.py'] ,
     author="PurplyBTW",
     author_email="purplybtw.main@gmail.com",
     description="Did you want to store data easly on a text file and get it using a command? Try this..!",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/PurplyBTW/Sessions",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
