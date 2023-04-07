from git import Repo
import setuptools_scm

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
    v = v.split("+")[0].replace("dev", "rc")

print("guessed", v)



