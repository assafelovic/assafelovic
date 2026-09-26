import json
import os
import re
import urllib.request

README = "README.md"
BADGE = re.compile(
    r'(<img src="https://img\.shields\.io/badge/%E2%98%85%20)([^-"]+)'
    r'(-24292F\?style=for-the-badge&logo=github&logoColor=white" alt="([\w.-]+/[\w.-]+) stars"/>)'
)


def stars(repo):
    request = urllib.request.Request(f"https://api.github.com/repos/{repo}")
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        request.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(request) as response:
        return json.load(response)["stargazers_count"]


def short(count):
    if count < 1000:
        return str(count)
    return f"{count / 1000:.1f}".rstrip("0").rstrip(".") + "K"


def main():
    with open(README) as f:
        text = f.read()
    updated = BADGE.sub(lambda m: m.group(1) + short(stars(m.group(4))) + m.group(3), text)
    if updated != text:
        with open(README, "w") as f:
            f.write(updated)


if __name__ == "__main__":
    main()
