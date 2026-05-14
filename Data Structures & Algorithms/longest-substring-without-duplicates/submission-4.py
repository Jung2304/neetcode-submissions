class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    left, right = 0, 1
    se = set()
    max_len = 1

    if s == "":
      return 0
    else:
      se.add(s[left])

    while right < len(s):
      while s[right] in se:
        se.remove(s[left])
        left += 1
      
      if s[right] not in se:
        se.add(s[right])
        max_len = max(max_len, right - left + 1)
        right += 1
    
    return max_len