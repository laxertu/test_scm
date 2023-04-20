import setuptools
import setuptools_scm.version
import pkg_resources


def myversion():
    from setuptools_scm.version import guess_next_date_ver

    def get_next_version(version: setuptools_scm.version.ScmVersion):
        return guess_next_date_ver(version)


    return {
        'version_scheme': get_next_version,
        'local_scheme': 'no-local-version',
    }


setuptools.setup(
    name="test_scm",
    use_scm_version=myversion,
    packages=setuptools.find_packages(),
)
