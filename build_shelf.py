#!/usr/bin/env python3
"""Build the Shelf listing data from the media consumption tracker.

Reads the tracker's mcribb.yaml and writes two Quarto listing data files into
the repo root:
  - shelf.yml      everything, for shelf.qmd (the full library)
  - currently.yml  in-progress items, for the "Currently" widget on culture.qmd

This is a MANUAL step: run it after you log media, then commit the generated
*.yml so the site builds self-contained in CI.

  python build_shelf.py
  python build_shelf.py --source "C:/dev/repos/sandbox/consumption/mcribb.yaml"
"""
from __future__ import annotations

import argparse
from pathlib import Path

import yaml

DEFAULT_SOURCE = Path(r"C:\dev\repos\sandbox\consumption\mcribb.yaml")
HERE = Path(__file__).parent

TYPE_LABELS = {"book": "Book", "movie": "Movie", "tv_show": "TV", "video_game": "Game"}
STATUS_LABELS = {"not_started": "Want to", "in_progress": "In progress", "finished": "Finished"}
# date field varies by type; everything else uses watched_date
DATE_FIELDS = {"book": "finished_date", "video_game": "played_date"}
CREATOR_KEYS = ["author", "director", "developer", "showrunner", "screenplay", "based_on"]


def primary_creator(creators: dict | None) -> str:
    if not creators:
        return ""
    for key in CREATOR_KEYS:
        if creators.get(key):
            return str(creators[key])
    return str(next(iter(creators.values())))


def consumed_date(entry: dict) -> str:
    field = DATE_FIELDS.get(entry.get("type", ""), "watched_date")
    return str(entry.get(field) or "")


def external_link(entry: dict) -> str | None:
    ids = entry.get("identifiers") or {}
    t = entry.get("type")
    if t in ("movie", "tv_show") and ids.get("imdb"):
        return f"https://www.imdb.com/title/{ids['imdb']}/"
    if t == "book":
        isbn = ids.get("ISBN_13") or ids.get("ISBN_10")
        if isbn:
            return f"https://openlibrary.org/isbn/{str(isbn).replace('-', '')}"
    return None


def to_item(entry: dict) -> dict:
    t = entry.get("type", "")
    title = str(entry.get("title", "Untitled"))
    if t == "tv_show" and entry.get("season"):
        title = f"{title} — Season {entry['season']}"
    rating = entry.get("personal_rating")
    item = {
        "title": title,
        "creator": primary_creator(entry.get("creators")),
        "type": TYPE_LABELS.get(t, t.title()),
        "year": entry.get("release_year"),
        "rating": f"{rating}/10" if rating is not None else "",
        "status": STATUS_LABELS.get(entry.get("status", ""), ""),
        "date": consumed_date(entry),
        "categories": [x for x in (TYPE_LABELS.get(t), STATUS_LABELS.get(entry.get("status", ""))) if x],
    }
    link = external_link(entry)
    if link:
        item["path"] = link
    if entry.get("notes"):
        item["description"] = str(entry["notes"])
    return item


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE,
                        help="Path to the tracker's mcribb.yaml")
    args = parser.parse_args()

    data = yaml.safe_load(args.source.read_text(encoding="utf-8")) or {}
    entries = data.get("entries", [])
    items = [to_item(e) for e in entries]
    items.sort(key=lambda i: i.get("date") or "", reverse=True)

    dump = lambda obj: yaml.safe_dump(obj, allow_unicode=True, sort_keys=False)
    (HERE / "shelf.yml").write_text(dump(items), encoding="utf-8")
    current = [i for i in items if i["status"] == "In progress"]
    (HERE / "currently.yml").write_text(dump(current), encoding="utf-8")

    print(f"Wrote shelf.yml ({len(items)} items) and currently.yml ({len(current)} items)")


if __name__ == "__main__":
    main()
