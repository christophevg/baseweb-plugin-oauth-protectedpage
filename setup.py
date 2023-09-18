import os
import re
import setuptools

NAME             = "baseweb-plugin-oauth-protectedpage"
AUTHOR           = "Christophe VG"
AUTHOR_EMAIL     = "contact@christophe.vg"
DESCRIPTION      = "baseweb plugin providing an oauth protected page component"
LICENSE          = "MIT"
KEYWORDS         = "baseweb plugin oauth protected page component"
URL              = "https://github.com/christophevg/" + NAME
README           = "README.md"
CLASSIFIERS      = [
  "Intended Audience :: Developers",
  "Programming Language :: Python",
  "Development Status :: 4 - Beta",
  "Programming Language :: Python :: 3.8",
  "Programming Language :: Python :: 3.9",
  "Programming Language :: Python :: 3.10",
  "Programming Language :: Python :: 3.11",
  "License :: OSI Approved :: MIT License",
  "Environment :: Plugins",
  "Environment :: Web Environment",
  
]
INSTALL_REQUIRES = [
  "baseweb",
  "oatk",
  "flask-login",
  
]
ENTRY_POINTS = {
  
}
SCRIPTS = [
  
]

HERE = os.path.dirname(__file__)

def read(file):
  with open(os.path.join(HERE, file), "r") as fh:
    return fh.read()

VERSION = re.search(
  r'__version__ = [\'"]([^\'"]*)[\'"]',
  read(NAME.replace("-", "_") + "/__init__.py")
).group(1)

LONG_DESCRIPTION = read(README)

if __name__ == "__main__":
  setuptools.setup(
    name=NAME,
    version=VERSION,
    packages=setuptools.find_packages(),
    author=AUTHOR,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    license=LICENSE,
    keywords=KEYWORDS,
    url=URL,
    classifiers=CLASSIFIERS,
    install_requires=INSTALL_REQUIRES,
    entry_points=ENTRY_POINTS,
    scripts=SCRIPTS,
    include_package_data=True    
  )
