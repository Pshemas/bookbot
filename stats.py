def count_words(text: str) -> int:
    return len(text.split())


def count_chars(text: str) -> dict:
    char_cnt = {}
    for char in text:
        current_char = char.lower()
        if current_char in char_cnt:
            char_cnt[current_char] += 1
        else:
            char_cnt[current_char] = 1
    return char_cnt


def create_char_stats(char_cnts: dict) -> list[dict]:
    stats = []
    for char_cnt in char_cnts.items():
        stats.append({"char": char_cnt[0], "num": char_cnt[1]})
    stats.sort(reverse=True, key=lambda items: items["num"])
    return stats
