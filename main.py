from collections import Counter
from pathlib import Path


def load_text(path: str) -> str:
    original_path = Path(path)
    raw_text = original_path.read_text(encoding="utf-8")
    return raw_text

def get_words(text: str) -> list[str]:
    cleaned_text = text.strip().lower()
    return [cleaned for word in cleaned_text.split() if (cleaned := word.strip(".!?,"))]

def count_words(words: list[str]) -> Counter[str]:
    return Counter(words)

def print_stats(counts: Counter[str]) -> None:
    total_words = sum(counts.values())
    unique_words = len(counts)
    common_words = counts.most_common(3)

    print(f"Total Words: {total_words}")
    print(f"Unique Words: {unique_words}")
    print("Common Words:\n")
    for word, count in common_words:
        print(f"\t{word} - {count} instances")



def main():
    raw_text = load_text("./sample.txt")
    clean_words = get_words(raw_text)
    word_counts = count_words(clean_words)
    print_stats(word_counts)

if __name__ == "__main__":
    main()