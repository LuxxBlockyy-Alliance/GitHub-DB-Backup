import git
import os
import time


def commit_and_push(file, commit_message, private_repo_url):
    git.repo.fun.update_environment(GIT_CONFIG_PARAMETERS={"core.fileMode": False})
    repo = git.Repo("./KillerHaseWorld/source")
    repo.git.add(file)
    repo.git.commit(m=commit_message)
    access_token = os.environ.get("GITHUB_ACCESS_TOKEN")
    if not access_token:
        access_token = input("Enter your Github Access Token: ")

    private_repo_url = private_repo_url.replace("https://", f"https://{access_token}@")
    repo.git.push(url=private_repo_url)


def run_function_daily():
    while True:
        commit_and_push("world.db", "Ein Testcommit", "https://github.com/LuxxBlockyy-Alliance/db_backup.git")
        time.sleep(86400)


if __name__ == "__main__":
    run_function_daily()
