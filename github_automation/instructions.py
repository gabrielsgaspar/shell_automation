#!/usr/bin/env python

# Import library
import os
import sys
from github import Github
from dotenv import load_dotenv

# Load dotenv
load_dotenv()

def project():
    # Setup environmental variables
    path = os.getenv("PROJECT_PATH")
    user = os.getenv("USER")
    password = os.getenv("PASSWORD")
    # Create new folder for project
    os.makedirs(path + "/" + str(sys.argv[1]))
    # Setup using username and password
    g = Github(user, password)
    # Create new repo
    user = g.get_user()
    repo = user.create_repo(str(sys.argv[1]))

if __name__ == "__main__":
    project()
