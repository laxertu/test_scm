import datetime

import setuptools
import setuptools_scm.version


def myversion():
    from setuptools_scm.version import guess_next_date_ver
    from setuptools_scm import get_version

    def get_next_version(version: setuptools_scm.version.ScmVersion):
        version.time = datetime.datetime.now()
        # fallback_version="0.0.0"
        if version.distance is None:
            return get_version()
        else:
            return version.format_next_version(guess_next_date_ver)

    return {
        'version_scheme': get_next_version,
        #'local_scheme': 'no-local-version',
    }


setuptools.setup(
    name="test_scm",
    use_scm_version=myversion,
    packages=setuptools.find_packages(),
)
