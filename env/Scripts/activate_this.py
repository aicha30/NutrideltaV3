"""Activate virtualenv for current interpreter:

Use exec(open(this_file).read(), {'__file__': this_file}).

This can be used when you must use an existing Python interpreter, not the virtualenv bin/python.
"""
import environ
import site
import sys

try:
    __file__
except NameError:
    raise AssertionError("You must use exec(open(this_file).read(), {'__file__': this_file}))")

# prepend bin to PATH (this file is inside the bin directory)
bin_dir = environ.path.dirname(environ.path.abspath(__file__))
environ.environ["PATH"] = environ.pathsep.join([bin_dir] + environ.environ.get("PATH", "").split(environ.pathsep))

base = environ.path.dirname(bin_dir)

# virtual env is right above bin directory
environ.environ["VIRTUAL_ENV"] = base

# add the virtual environments site-package to the host python import mechanism
IS_PYPY = hasattr(sys, "pypy_version_info")
IS_JYTHON = sys.platform.startswith("java")
if IS_JYTHON:
    site_packages = environ.path.join(base, "Lib", "site-packages")
elif IS_PYPY:
    site_packages = environ.path.join(base, "site-packages")
else:
    IS_WIN = sys.platform == "win32"
    if IS_WIN:
        site_packages = environ.path.join(base, "Lib", "site-packages")
    else:
        site_packages = environ.path.join(base, "lib", "python{}".format(sys.version[:3]), "site-packages")

prev = set(sys.path)
site.addsitedir(site_packages)
sys.real_prefix = sys.prefix
sys.prefix = base

# Move the added items to the front of the path, in place
new = list(sys.path)
sys.path[:] = [i for i in new if i not in prev] + [i for i in new if i in prev]
