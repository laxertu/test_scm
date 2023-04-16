import setuptools
import datetime

import setuptools_scm.version

VERSION_DATE_FORMAT = "%Y.%-m.%-d"

def myversion():
    from setuptools_scm.version import guess_next_date_ver
    from setuptools_scm import get_version

    def get_next_version(version: setuptools_scm.version.ScmVersion):
        if str(version.tag) == '0.0':

            v = f"{datetime.datetime.now().strftime(VERSION_DATE_FORMAT)}.1"
            return v

        if version.branch == 'master':
            if version.distance > 0:
                v = guess_next_date_ver(version)
        else:
            v = get_version()
        return v

    return {
        'version_scheme': get_next_version,
        'local_scheme': 'no-local-version',
    }


setuptools.setup(
    name="test_scm",
    use_scm_version=myversion,
    author="Luca Stretti",
    author_email="laxertu@gmail.com",
    packages=setuptools.find_packages()
)

