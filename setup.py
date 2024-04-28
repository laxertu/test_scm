import datetime

import setuptools
import setuptools_scm.version


def myversion():
    from setuptools_scm.version import guess_next_date_ver
    from setuptools_scm import get_version

    def get_next_version(version: setuptools_scm.version.ScmVersion):
        version.time = datetime.datetime.now()
        # fallback_version="0.0.0"
        return get_version(version_scheme=guess_next_date_ver) \
            if version.branch == "master" else \
            version.format_next_version(guess_next_date_ver, fmt='%Y.%m.%d')


    return {
        'version_scheme': get_next_version,
        'local_scheme': 'no-local-version',
    }


setuptools.setup(
    name="test_scm",
    use_scm_version=myversion,
    packages=setuptools.find_packages(),
)
