from collections import Counter

class Solution:
  def minWindow(self, s: str, t: str) -> str:
    need = Counter(t)
    window = {}

    have = 0
    need_count = len(need)

    left = 0

    res = [-1, -1]
    res_len = float("inf")

    for right in range(len(s)):
      c = s[right]

      if c not in window:
        window[c] = 1
      else:
        window[c] += 1
      
      if c in need and window[c] == need[c]:
        have += 1
      
      while have == need_count:

        # update
        window_len = right - left + 1

        if window_len < res_len:
          res = [left, right]
          res_len = window_len

        # thu nhỏ
        window[s[left]] -= 1

        if s[left] in need and window[s[left]] < need[s[left]]:
          have -= 1
        
        left += 1 

    left, right = res

    return s[left:right+1] if res_len != float("inf") else ""