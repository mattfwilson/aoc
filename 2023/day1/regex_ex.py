import re

def find_match_from_end(pattern, text):
    # Compile the regular expression pattern
    regex = re.compile(pattern)

    # Search for the pattern in the reversed string
    match = regex.search(text[::-1])

    if match:
        # If a match is found, calculate the starting and ending indices
        start_index = len(text) - match.end()
        end_index = len(text) - match.start()

        # Return the match and indices
        return match.group(), start_index, end_index
    else:
        # Return None if no match is found
        return None

# Example usage
pattern = r'\d+'  # Example pattern to match digits
text = "abc123def456"

result = find_match_from_end(pattern, text)

if result:
    match, start, end = result
    print(f"Match: {match}, Start Index: {start}, End Index: {end}")
else:
    print("No match found.")
