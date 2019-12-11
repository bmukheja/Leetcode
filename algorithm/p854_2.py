class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        # The idea is to treat A as src node and B as dest node, all the swaps between them are
        # edges of a directed graph
        A_chars, B_chars = [],[]
        for a,b in zip(A,B):
            if a!=b:
                A_chars.append(a), B_chars.append(b)
        A = "".join(A_chars)
        B = "".join(B_chars)

        def nbrs(x: str):
            # We check how far from the start are x and B similar, then start to do the swapping after that
            for i in range(len(x)-1):
                if x[i] == B[i]:
                    continue

                for j in range(i+1,len(x)):
                    if x[j]!=B[j] and x[i] == B[j]:
                        yield x[:i]+x[j] + x[i+1:j] + x[i] + x[j+1:]
                break

        k = 0
        queue = [(k,A)]
        visited = set()
        for k,cur in queue:
            if cur == B:
                return k
            if cur in visited:
                continue
            visited.add(cur)
            for nbr in nbrs(cur):
                if nbr not in visited:
                    queue.append((k+1,nbr))


print(Solution().kSimilarity("ab","ba"))
print(Solution().kSimilarity("abc","bca"))
print(Solution().kSimilarity("abac","baca"))
print(Solution().kSimilarity("aabc","abca"))
print(Solution().kSimilarity("abccaacceecdeea","bcaacceeccdeaae"))



