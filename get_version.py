from setuptools_scm import get_version
print(".".join(get_version(local_scheme="no-local-version").split(".")[:-1]))
"""
import pkg_resources
version = pkg_resources.require("test_scm")[0].version
print(version)
"""