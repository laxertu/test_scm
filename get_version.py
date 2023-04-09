from git import Repo
from setuptools_scm import get_version

branch = Repo().active_branch
v = get_version()
if str(branch) == "master":
    tmp = ".".join(v.split(".")[0:3])
    v = ".".join(v.split(".")[0:3])

print("packege version", v)
