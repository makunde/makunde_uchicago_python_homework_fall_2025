from pypdf import PdfReader
import re

SAFE_TO_IGNORE = "t.a.binkowski"


def extract_key_words(filename, common_words_filename):
    reader = PdfReader(filename)
    common_words_file = open(common_words_filename)
    common_words_list = common_words_file.read().splitlines()
    key_words = {}
    word_pattern = re.compile(r"\b[\w']+\b")

    for page in reader.pages:
        text = page.extract_text() or ""
        words = word_pattern.findall(text.lower())
        for word in words:
            if word in common_words_list or word in SAFE_TO_IGNORE:
                continue
            key_words[word] = key_words.get(word, 0) + 1
    return key_words


def sort_keywords_by_frequency(key_words_dict):
    return sorted(key_words_dict.items(), key=lambda x: x[1], reverse=True)


def write_keywords_to_index(ordered_keyword_list, filename):
    index_filename = filename.replace(".pdf", "_index.txt")
    with open(index_filename, "w", encoding="utf-8") as f:
        for keyword, freq in ordered_keyword_list:
            f.write(f"{keyword}: {freq}\n")
