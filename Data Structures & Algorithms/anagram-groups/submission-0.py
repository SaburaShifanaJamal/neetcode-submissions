class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        gr={}
        for i in strs:
            key="".join(sorted(i))
            if key not in gr:
                gr[key]=[]
            gr[key].append(i)
        return list(gr.values())