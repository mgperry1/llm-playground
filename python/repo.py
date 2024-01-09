import requests
from git import Repo
import os


def download_and_upload_file(url, file_path, git_repo_path, pat_token):
    # Download the file from the URL
    response = requests.get(url)
    with open(file_path, "wb") as file:
        file.write(response.content)

    # Check if the Git repository already exists
    if not os.path.exists(git_repo_path):
        # Clone the remote repository
        Repo.clone_from("https://github.com/mgperry1/devops-config.git", git_repo_path)

    # Initialize the Git repository
    repo = Repo(git_repo_path)

    # Add the file to the repository
    repo.index.add([file_path])

    # Commit the changes
    repo.index.commit("Added file")

    # Push the changes to the remote repository using the PAT token
    origin = repo.remote()
    origin.push(refspec="master", force=True, credentials=("x-access-token", pat_token))
