from pathlib import Path

OUTPUT = Path("/output/entry.txt")

def main():
    line = "I just get the thing done, the code is cleaner than when I started, and you don\u2019t have to chase me."
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(line + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
