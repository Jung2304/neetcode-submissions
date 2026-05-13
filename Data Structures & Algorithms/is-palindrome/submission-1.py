class Solution:
  def isPalindrome(self, s: str) -> bool:
    new_string = s.replace(" ", "").lower()

    clean_string = "".join(c for c in new_string if c.isalnum())

    reverse_string = clean_string[::-1]

    return clean_string == reverse_string