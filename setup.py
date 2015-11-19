from setuptools import setup

setup(
   name = "rockwell",
   packages = ["rockwell"],
   version = "0.0.1",
   description = "Watching since 1984",
   author = "Dan Wagner",
   author_email = "danwagnerco@gmail.com",
   url = "https://github.com/danwagnerco/rockwell",
   install_requires = ["requests>=2.7.0"],
   classifiers = [
       "Development Status :: 3 - Alpha",
       "Environment :: Console",
       "Intended Audience :: Developers",
       "Operating System :: OS Independent",
       "Programming Language :: Python"
       ],
   keywords = "rockwell"
)

