from git import Repo
import setuptools_scm

repo = Repo()

tags = [t.name for t in repo.tags]

v = setuptools_scm.get_version()
if str(repo.active_branch) == "master":
    v = ".".join(v.split(".")[0:3])
    if v in tags:
        v = ""
else:
    v = ""

print(v)




