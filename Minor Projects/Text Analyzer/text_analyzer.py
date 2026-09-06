"""
Text Analyzer
-------------
Analyzes a block of text or a text file: word count, character count,
most frequent words, sentence count, and estimated reading time.

Usage: python 11_text_analyzer.py
"""

import re
from collections import Counter

STOPWORDS = {
    "the", "a", "an", "and", "or", "but", "is", "are", "was", "were",
    "in", "on", "at", "to", "for", "of", "with", "as", "by", "it",
    "this", "that", "be", "have", "has", "i", "you", "he", "she",
    "they", "we", "his", "her", "their", "its", "not", "so", "if"
}


def analyze_text(text):
    words = re.findall(r"\b[a-zA-Z']+\b", text.lower())
    sentences = re.split(r"[.!?]+", text)
    sentences = [s for s in sentences if s.strip()]

    word_count = len(words)
    char_count = len(text)
    sentence_count = len(sentences)

    meaningful_words = [w for w in words if w not in STOPWORDS and len(w) > 2]
    most_common = Counter(meaningful_words).most_common(10)

    reading_time_minutes = word_count / 200  # avg reading speed

    return {
        "word_count": word_count,
        "char_count": char_count,
        "sentence_count": sentence_count,
        "most_common": most_common,
        "reading_time_minutes": reading_time_minutes,
    }


def print_report(stats):
    print("\n=== TEXT ANALYSIS REPORT ===")
    print(f"Word count: {stats['word_count']}")
    print(f"Character count: {stats['char_count']}")
    print(f"Sentence count: {stats['sentence_count']}")
    print(f"Estimated reading time: {stats['reading_time_minutes']:.1f} min")

    print("\nTop 10 most frequent words:")
    if not stats["most_common"]:
        print("  (not enough meaningful words)")
    for word, count in stats["most_common"]:
        print(f"  {word}: {count}")


def main():
    print("=== TEXT ANALYZER ===")
    print("1. Paste text directly")
    print("2. Analyze a text file")
    choice = input("Choose an option (1-2): ").strip()

    if choice == "2":
        path = input("Enter file path: ").strip()
        try:
            with open(path, "r", encoding="utf-8") as f:
                text = f.read()
        except FileNotFoundError:
            print("File not found.")
            return
    else:
        print("Paste your text below. Press Enter twice when done:")
        lines = []
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)
        text = "\n".join(lines)

    if not text.strip():
        print("No text provided.")
        return

    stats = analyze_text(text)
    print_report(stats)


if __name__ == "__main__":
    main()
