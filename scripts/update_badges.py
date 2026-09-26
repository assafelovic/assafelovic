import json
import os
import re
import urllib.request
from datetime import datetime, timezone

README = "README.md"
BADGES = "badges"
REPO = re.compile(r'alt="([\w.-]+/[\w.-]+) stars"')

GITHUB = "M8 0c4.42 0 8 3.58 8 8a8.013 8.013 0 0 1-5.45 7.59c-.4.08-.55-.17-.55-.38 0-.27.01-1.13.01-2.2 0-.75-.25-1.23-.54-1.48 1.78-.2 3.65-.88 3.65-3.95 0-.88-.31-1.59-.82-2.15.08-.2.36-1.02-.08-2.12 0 0-.67-.22-2.2.82-.64-.18-1.32-.27-2-.27-.68 0-1.36.09-2 .27-1.53-1.03-2.2-.82-2.2-.82-.44 1.1-.16 1.92-.08 2.12-.51.56-.82 1.28-.82 2.15 0 3.06 1.86 3.75 3.64 3.95-.23.2-.44.55-.51 1.07-.46.21-1.61.55-2.33-.66-.15-.24-.6-.83-1.23-.82-.67.01-.27.38.01.53.34.19.73.9.82 1.13.16.45.68 1.31 2.69.94 0 .67.01 1.3.01 1.49 0 .21-.15.45-.55.38A7.995 7.995 0 0 1 0 8c0-4.42 3.58-8 8-8Z"
STAR = "M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97.719 4.192a.751.751 0 0 1-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194L.818 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25Z"
FORK = "M5 5.372v.878c0 .414.336.75.75.75h4.5a.75.75 0 0 0 .75-.75v-.878a2.25 2.25 0 1 1 1.5 0v.878a2.25 2.25 0 0 1-2.25 2.25h-1.5v2.128a2.251 2.251 0 1 1-1.5 0V8.5h-1.5A2.25 2.25 0 0 1 3.5 6.25v-.878a2.25 2.25 0 1 1 1.5 0ZM5 3.25a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Zm6.75.75a.75.75 0 1 0 0-1.5.75.75 0 0 0 0 1.5Zm-3 8.75a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Z"
CLOCK = "M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Zm7-3.25v2.992l2.028.812a.75.75 0 0 1-.557 1.392l-2.5-1A.751.751 0 0 1 7 8.25v-3.5a.75.75 0 0 1 1.5 0Z"

YELLOW = "#E3B341"
WHITE = "#FFFFFF"

# Text is sized with textLength so the layout holds whatever font the viewer has.
CHAR_WIDTH = 8.2
PAD = 10
ICON = 14
GAP = 6


def fetch(repo):
    request = urllib.request.Request(f"https://api.github.com/repos/{repo}")
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        request.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(request) as response:
        return json.load(response)


def short(count):
    if count < 1000:
        return str(count)
    return f"{count / 1000:.1f}".rstrip("0").rstrip(".") + "K"


def ago(timestamp):
    days = (datetime.now(timezone.utc) - datetime.fromisoformat(timestamp.replace("Z", "+00:00"))).days
    if days < 1:
        return "TODAY"
    if days < 30:
        return f"{days} DAY{'S' if days > 1 else ''} AGO"
    if days < 365:
        months = days // 30
        return f"{months} MONTH{'S' if months > 1 else ''} AGO"
    years = days // 365
    return f"{years} YEAR{'S' if years > 1 else ''} AGO"


def badge(label, icons, text, background, color):
    x = PAD
    shapes = []
    for path, fill in icons:
        shapes.append(f'<svg x="{x}" y="7" width="{ICON}" height="{ICON}" viewBox="0 0 16 16"><path fill="{fill}" d="{path}"/></svg>')
        x += ICON + GAP
    text_width = round(len(text) * CHAR_WIDTH, 1)
    width = round(x + text_width + PAD, 1)
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="28" role="img" aria-label="{label}">'
        f"<title>{label}</title>"
        f'<rect width="{width}" height="28" fill="{background}"/>'
        + "".join(shapes)
        + f'<text x="{x}" y="18.5" fill="{color}" font-family="Verdana,DejaVu Sans,Geneva,sans-serif" '
        f'font-size="11" font-weight="bold" textLength="{text_width}" lengthAdjust="spacing">{text}</text>'
        "</svg>\n"
    )


def write(name, svg):
    with open(os.path.join(BADGES, name), "w") as f:
        f.write(svg)


def main():
    with open(README) as f:
        repos = REPO.findall(f.read())
    os.makedirs(BADGES, exist_ok=True)
    for repo in repos:
        data = fetch(repo)
        slug = repo.replace("/", "-")
        stars = short(data["stargazers_count"])
        forks = short(data["forks_count"])
        updated = ago(data["pushed_at"])
        write(f"{slug}-stars.svg", badge(f"{stars} stars", [(GITHUB, WHITE), (STAR, YELLOW)], stars, "#24292F", YELLOW))
        write(f"{slug}-forks.svg", badge(f"{forks} forks", [(FORK, WHITE)], forks, "#424A53", WHITE))
        write(f"{slug}-updated.svg", badge(f"Updated {updated.lower()}", [(CLOCK, WHITE)], updated, "#6E7781", WHITE))


if __name__ == "__main__":
    main()
