"""Lecture 01 practice problems.

Implement each function below so tests pass.
Rules:
- Do not change function names/signatures.
- Keep implementations pure unless the function explicitly needs I/O.
- Use only the Python standard library.
"""

from __future__ import annotations
from collections import Counter, defaultdict, deque


def normalize_username(name: str) -> str:
    name = name.strip().lower()
    return "_".join(name.split())


def is_valid_age(age: int) -> bool:
    return 18 <= age <= 120


def truthy_values(values: list[object]) -> list[object]:
    result = []
    for value in values:
        if value:
            result.append(value)
    return result


def sum_until_negative(numbers: list[int]) -> int:
    total = 0
    for number in numbers:
        if number < 0:
            break
        total += number
    return total


def skip_multiples_of_three(numbers: list[int]) -> list[int]:
    result = []
    for number in numbers:
        if number % 3 != 0:
            result.append(number)
    return result


def first_even_or_none(numbers: list[int]) -> int | None:
    for number in numbers:
        if number % 2 == 0:
            return number
    return None


def squares_of_even(numbers: list[int]) -> list[int]:
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(number * number)
    return result


def word_lengths(words: list[str]) -> dict[str, int]:
    result = {}
    for word in words:
        result[word] = len(word)
    return result


def zip_to_pairs(keys: list[str], values: list[int]) -> list[tuple[str, int]]:
    result = []
    for key, value in zip(keys, values):
        result.append((key, value))
    return result


def build_user(name: str, role: str = "student", active: bool = True) -> dict[str, object]:
    return {"name": name, "role": role, "active": active}


def append_tag_safe(tag: str, tags: list[str] | None = None) -> list[str]:
    if tags is None:
        tags = []
    tags.append(tag)
    return tags


def invert_dict(mapping: dict[str, int]) -> dict[int, str]:
    result = {}
    for key, value in mapping.items():
        result[value] = key
    return result


def unique_sorted_tags(tags: list[str]) -> list[str]:
    return sorted(set(tags))


def count_words(words: list[str]) -> dict[str, int]:
    return dict(Counter(words))


def group_scores(records: list[tuple[str, int]]) -> dict[str, list[int]]:
    result = defaultdict(list)
    for name, score in records:
        result[name].append(score)
    return dict(result)


def rotate_queue(items: list[str], steps: int) -> list[str]:
    d = deque(items)
    d.rotate(steps)
    return list(d)


def safe_int(value: str) -> int | None:
    try:
        return int(value)
    except:
        return None


def read_lines(path: str) -> list[str]:
    result = []
    with open(path, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                result.append(line)
    return result


def top_n_scores(scores: list[int], n: int = 3) -> list[int]:
    return sorted(scores, reverse=True)[:n]


def all_passed(scores: list[int], threshold: int = 50) -> bool:
    for score in scores:
        if score < threshold:
            return False
    return True