from setuptools_scm import get_version
print(get_version(local_scheme="no-local-version"))
"""
import pkg_resources
version = pkg_resources.require("test_scm")[0].version
print(version)
"""