import os
import re


def salted(text):
    key_letters = "АЕЁИОУЫЭЮЯаеёиоуыэюя"
    result = []
    for letter in text:
        result.append(letter)
        if letter in key_letters:
            result.append("c" + letter.lower())
    return "".join(result)


def akkords(path):

    akkords_pattern = r"\b[A-H]m?\b"
    with open(path, encoding="utf-8") as f:
        found_akkords = re.findall(akkords_pattern, f.read())
    return set(found_akkords)


def rename_files(
    dir,
    old_pattern,
    new_pattern=None,
    sample_names=None,
    to_replace=False,
):
    for f_name in os.listdir(dir):
        if old_pattern not in f_name:
            continue

        old_path = os.path.join(dir, f_name)
        name = f_name

        if new_pattern is not None:
            new_name = name.replace(old_pattern, new_pattern)

        if sample_names:
            for old_sample, rep_sample in sample_names.items():
                if old_sample in new_name:
                    new_name = new_name.replace(old_sample, rep_sample)

        if new_name == f_name:
            continue

        new_path = os.path.join(dir, new_name)

        if to_replace:
            os.replace(old_path, new_path)
        else:
            with open(old_path, "rb") as old, open(new_path, "wb") as new:
                new.write(old.read())
