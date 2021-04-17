class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub('[^\w]', ' ', paragraph)
            .lower().split()
                if word not in banned]
        
        counts = collections.defaultdict(int)
        
        for word in words: 
            counts[word] += 1
        
        c = collections.Counter(words)
        
        print(c.most_common(1))
            
        return max(counts, key=counts.get)
        
#         counts = collections.Counter(words)
        
#         return counts.most_common(1)[0][0]