import datetime

import setuptools
import setuptools_scm.version


def myversion():
    from setuptools_scm.version import guess_next_date_ver
    from setuptools_scm import get_version

    def calculate(version: setuptools_scm.version.ScmVersion):
        # fallback_version="0.0.0"
        if version.distance is None:
            return get_version()
        else:
            return version.format_next_version(guess_next_date_ver, date_fmt="%Y.%m.%d")

    return {
        'version_scheme': calculate
    }


setuptools.setup(
    name="test_scm",
    use_scm_version=myversion,
    packages=setuptools.find_packages(),
)
