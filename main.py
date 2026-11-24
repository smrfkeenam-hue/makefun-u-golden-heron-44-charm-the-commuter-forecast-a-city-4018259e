import os

ENTRY = "Good morning, Natterby: drizzle falls upwards until noon, so carry your umbrella upside down and expect the 8:15 early for once."


def entry_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def write_entry(text):
    os.makedirs(os.path.dirname(entry_path()), exist_ok=True)
    with open(entry_path(), "w", encoding="utf-8") as f:
        f.write(text)


def main():
    path = entry_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
