import json
import os
import re
import urllib.request

README = "README.md"
BADGE = re.compile(
    r'(<img src="https://img\.shields\.io/badge/)([^-"]+)'
    r'(-[0-9A-F]{6}\?style=for-the-badge&logo=(?:github|git)&logoColor=white" alt="([\w.-]+/[\w.-]+) (stars|forks)"/>)'
)
PREFIX = {"stars": "%E2%98%85%20", "forks": "FORKS%20"}
FIELD = {"stars": "stargazers_count", "forks": "forks_count"}


def fetch(repo, cache={}):
    if repo not in cache:
        request = urllib.request.Request(f"https://api.github.com/repos/{repo}")
        token = os.environ.get("GITHUB_TOKEN")
        if token:
            request.add_header("Authorization", f"Bearer {token}")
        with urllib.request.urlopen(request) as response:
            cache[repo] = json.load(response)
    return cache[repo]


def short(count):
    if count < 1000:
        return str(count)
    return f"{count / 1000:.1f}".rstrip("0").rstrip(".") + "K"


def replace(match):
    repo, kind = match.group(4), match.group(5)
    return match.group(1) + PREFIX[kind] + short(fetch(repo)[FIELD[kind]]) + match.group(3)


def main():
    with open(README) as f:
        text = f.read()
    updated = BADGE.sub(replace, text)
    if updated != text:
        with open(README, "w") as f:
            f.write(updated)


if __name__ == "__main__":
    main()
