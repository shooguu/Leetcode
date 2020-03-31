class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = dict()
        answer = []
        for word in strs:
            merge = "".join(sorted(word))
            if merge not in result:
                result[merge] = [word]
            else:
                result[merge].append(word)
        
        for sorted_word in result:
            answer.append(result[sorted_word])
        return answer
                
