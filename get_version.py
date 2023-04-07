from git import Repo
import setuptools_scm

repo = Repo()

tags = [t.name for t in repo.tags]

v = setuptools_scm.get_version()
if str(repo.active_branch) == "master":
    v_clean = ".".join(v.split(".")[0:3])
    tmp = v_clean.split(".")
    v = f"{tmp[0]}.{tmp[1]}.{int(tmp[2]) + 1}"

else:
    v = ""
print(v)
