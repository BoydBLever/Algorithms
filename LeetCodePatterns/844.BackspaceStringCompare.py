class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # This function returns the index of the next valid character. It accounts for backspace characters by skipping characters that would have been "deleted". Essentially, this function moves each pointer leftward until it finds a character that is not a backspace and hasn't been deleted by a preceding backspace. The returns the index of the next valid character, or -1 if there are no more valid characters.
        def nextValidChar(index, string):
            backspace_count = 0
            while index >= 0:
                if string[index] == '#':
                    backspace_count += 1
                elif backspace_count > 0:
                    backspace_count -= 1
                else:
                    return index
                index -= 1
            return index
        # Two pointers, i and j, start from the end of the strings
        # Because a backspace character affects the characters to its left
        i, j = len(s) - 1, len(t) - 1
        while i >= 0 or j >= 0:
            i = nextValidChar(i, s)
            j = nextValidChar(j, t)

            # If both strings are at valid characters, compare them
            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False

            # If only one of the strings has reached its end, they can't be the same
            elif i >= 0 or j >= 0:
                return False

            i -= 1
            j -= 1

        return True