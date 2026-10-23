from collections import Counter
from pathlib import Path


def load_text(path: str):
    originalPath = Path(path)
    rawText = originalPath.read_text(encoding="utf-8")
    cleanText = rawText.strip().lower()
    cleanText = cleanText.replace(".", "").replace(",", "").replace("!", "").replace("?", "").replace("'s", " is").replace("n't", " not")
    return cleanText

def get_words(text: str):
    counts = Counter(text.split())
    return counts

def printStats(counts: dict):
    totalWords = 0
    uniqueWords = 0
    commonWords = []
    for word, count in counts.items():
        totalWords += count
        uniqueWords = uniqueWords + 1
        if len(commonWords) < 3:
            commonWords.append(word)
        else:
            minLesserWord = word
            for key in commonWords:
                if counts.get(key) < counts.get(minLesserWord):
                    minLesserWord = key

            if minLesserWord != word:
                commonWords.remove(minLesserWord)
                commonWords.append(word)

    ordered = sorted(commonWords, key=lambda word: counts[word], reverse=True)

    print(f"Total Words: {totalWords}")
    print(f"Unique Words: {uniqueWords}")
    print("Common Words:\n")
    for word in ordered:
        print("\t" + word + f" - {counts.get(word)} instances")



def main():
    cleanText = load_text("./sample.txt")
    printStats(get_words(cleanText))

if __name__ == "__main__":
    main()