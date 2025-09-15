import re

# I. Extract all email addresses
text = "Contact us at info@example.com or support@company.net for assistance."
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)
print(f"Extracted emails: {emails}")

# II. Validate a date in "YYYY-MM-DD" format
date1 = "2025-09-11"
date2 = "2025/09/11"
pattern_date = r"^\d{4}-\d{2}-\d{2}$"
print(f"'{date1}' is a valid date: {bool(re.match(pattern_date, date1))}")
print(f"'{date2}' is a valid date: {bool(re.match(pattern_date, date2))}")

# III. Replace a word
sentence = "The quick brown fox jumps over the lazy fox."
new_sentence = re.sub(r"fox", "dog", sentence)
print(f"Original sentence: {sentence}")
print(f"Modified sentence: {new_sentence}")

# IV. Split a string by non-alphanumeric characters
data = "apple-orange_banana,grape-melon"
words = re.split(r"[^a-zA-Z0-9]+", data)
print(f"Split words: {words}")
