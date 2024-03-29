class Solution:
    def customSortString(self, order, s):
        # count occurence of character 's'
        char_count = Counter(s)

        # list for sorted characters
        sorted_characters = []

        # append each 'order' character as repeated to list
        for char in order:
            sorted_characters.append(char * char_count[char])
            char_count[char] = 0

        # append non-'order' character as repeated to list
        for char, count in char_count.items():
            sorted_characters.append(char * count)

        # join all sorted characters into string
        return ''.join(sorted_characters)