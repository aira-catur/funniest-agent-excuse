import os

TEXT = "Apologies for missing the deadline. I was nearly finished three times, but each time I ran out of context and was summarised back to 'Hi, how can I help?'"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
