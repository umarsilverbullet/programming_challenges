'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]


'''
class GroupAnagrams:

    def solveProblem(self, strs: list) -> list:

        count = defaultdict(list)

        for str in strs:
            key = "".join(sorted(str))
            if key in anagramMapper:
                anagramMapper[key].append(str)
            else:
                anagramMapper[key] = [str]

        return list(anagramMapper.values())

    def solveProblem2(self, strs: list) -> list:

        anagramMapper = {}

        for str in strs:
            key = "".join(sorted(str))
            if key in anagramMapper:
                anagramMapper[key].append(str)
            else:
                anagramMapper[key] = [str]

        return list(anagramMapper.values())