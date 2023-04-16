import setuptools
import datetime
from setuptools_scm import get_version

import setuptools_scm.version
import pkg_resources
version = pkg_resources.require("test_scm")[0].version

VERSION_DATE_FORMAT = "%Y.%-m.%-d"

def myversion():
    from setuptools_scm.version import guess_next_date_ver
    from setuptools_scm import get_version

    def get_next_version(version: setuptools_scm.version.ScmVersion):
        return version.format_next_version(guess_next_date_ver, fmt="{guessed}")

    return {
        'version_scheme': get_next_version,
        'local_scheme': 'no-local-version',
    }


setuptools.setup(
    name="test_scm",
    use_scm_version=myversion,
    packages=setuptools.find_packages(),
)

