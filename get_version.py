from git import Repo
from setuptools_scm import get_version

branch = Repo().active_branch
if str(branch) == "master":
    v = get_version()
    v = ".".join(v.split(".")[0:3])
    print(".".join(v.split(".")[0:3]))
else:
    print("")
