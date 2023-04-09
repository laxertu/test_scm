from git import Repo
import setuptools_scm

repo = Repo()

print("Tags:")
for t in repo.tags:
    print(t.name)
    print(t.tag)
print("")

#tags = sorted(repo.tags, key=lambda t: t.tag.tagged_date)

v = setuptools_scm.get_version()
print("On branch", repo.active_branch)
print("Raw version", v)
if str(repo.active_branch) == "master":
    v = ".".join(v.split(".")[0:3])
else:
    v = v.split("+")[0].replace("dev", "rc")

print("Next Stable version", v)

