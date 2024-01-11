from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    current_word = []
    min_length = float("Inf")
    for string in strs:
        min_length = min(min_length, len(string))
    print(min_length)
    for i in range(min_length):
        current_word.append(strs[0][i])
        print(i, current_word)
        for word in strs:
            if word[i] != current_word[i]:
                current_word.pop()
                break

    return "".join(current_word)


longestCommonPrefix(["flower", "flow", "flight"])
