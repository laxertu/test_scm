import setuptools
import setuptools_scm.version


def myversion():
    from setuptools_scm.version import guess_next_date_ver

    def get_next_version(version: setuptools_scm.version.ScmVersion):
        return guess_next_date_ver(version, date_fmt='%Y.%m.%d')# if version.branch == 'master' else setuptools_scm.get_version()


    return {
        'version_scheme': get_next_version,
        'local_scheme': 'no-local-version',
    }


setuptools.setup(
    name="test_scm",
    use_scm_version=myversion,
    packages=setuptools.find_packages(),
)
