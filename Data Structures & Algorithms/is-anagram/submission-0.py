class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # edge cases to catch invalid anagrams early:
        if(len(s) != len(t)):
            return False

        dict_s = {}
        dict_t = {}
        
        for letter in s:
            # checking the condition if the letter doesn't exist in the dictionary eyt
            if letter not in dict_s:
                dict_s[letter] = 1
            else:
                dict_s[letter] += 1

        for letter in t:
            if letter not in dict_t:
                dict_t[letter] = 1
            else:
                dict_t[letter] += 1


        # now that we have our letters in our maps, we check if it's an anagram by checking
        # if both dictionary's keys have the same value.

        for key in dict_s:
            # if the key doesn't exist in string t's dictionary, return False.
            if key not in dict_t:
                return False

            if dict_s[key] != dict_t[key]:
                return False


        return True