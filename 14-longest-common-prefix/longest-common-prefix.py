class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:#bs??
        pre=""
        for i in range(len(strs[0])):
            pre += strs[0][i]
            print(pre)
            for j in range(len(strs)):
                print(strs[j])
                if len(pre) <= len(strs[j]):
                    if pre != strs[j][:len(pre)]:
                        return pre[:len(pre)-1]
                else:
                    return pre[:len(pre)-1]
        return pre


        