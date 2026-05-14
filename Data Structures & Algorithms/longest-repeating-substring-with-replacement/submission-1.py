class Solution:
  def characterReplacement(self, s: str, k: int) -> int:
    count = {}

    left = 0
    max_frequency = 0
    max_length = 0

    for right in range(len(s)):

        # thêm ký tự mới vào window
        count[s[right]] = count.get(s[right], 0) + 1

        # số lần xuất hiện lớn nhất trong window
        max_frequency = max(max_frequency, count[s[right]])

        window_size = right - left + 1

        # nếu cần replace quá k -> shrink
        while window_size - max_frequency > k:
            count[s[left]] -= 1
            left += 1

            window_size = right - left + 1

        # window hiện tại hợp lệ
        max_length = max(max_length, window_size)

    return max_length