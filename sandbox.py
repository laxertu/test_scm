from git import Repo
import setuptools_scm
def myversion(v: setuptools_scm.ScmVersion):
    return setuptools_scm.version.guess_next_version(v)

repo = Repo()

print("tags:")
for t in repo.tags:
    print(t.name)
print("")

v = setuptools_scm.get_version()
print("on branch", repo.active_branch)
print("raw version", v)
if str(repo.active_branch) == "master":
    v = ".".join(v.split(".")[0:3])
else:
    tmp = v.split("+")
    v = tmp[0]

print("guessed", v)






exit(0)

print("--")




#print(version("autoversion"))


# rorepo is a Repo instance pointing to the git-python repository.
# For all you know, the first argument to Repo is a path to the repository
# you want to work with
repo = Repo()
print(repo.active_branch)
#print(repo.tags)
for t in repo.tags:
    print(t.name)

exit(0)
def myversion():
    from setuptools_scm.version import SEMVER_MINOR, guess_next_simple_semver, release_branch_semver_version

    def my_release_branch_semver_version(version):
        v = release_branch_semver_version(version)
        if v == version.format_next_version(guess_next_simple_semver, retain=SEMVER_MINOR):
            return version.format_next_version(guess_next_simple_semver, fmt="{guessed}", retain=SEMVER_MINOR)
        return v

    return {
        'version_scheme': my_release_branch_semver_version,
        'local_scheme': 'no-local-version',
    }


print(myversion())


