# https://www.lintcode.com/problem/659/
def encode(self, strs):
    # Initialize an empty string to store the result
    res = ""
    
    # Iterate over each string in the list
    for s in strs:
        # Append the length of the string, followed by a '#' delimiter, and then the string itself
        res += str(len(s)) + "#" + s
    
    # Return the concatenated result
    return res

# @param: str: A string
# @return: decodes a single string to a list of strings

def decode(self, str):
    # Initialize an empty list for the result and a pointer 'i' at the beginning of the string
    res, i = [], 0
    
    # Continue decoding while there's more string to process
    while i < len(str):
        # Initialize 'j' to the current position of 'i'
        j = i
        
        # Move 'j' forward until the '#' delimiter is found
        while str[j] != "#":
            j += 1
        
        # Extract the length of the next string (which is before the '#' delimiter)
        length = int(str[i:j])
        
        # Append the string of the given length (after the delimiter) to the result list
        res.append(str[j + 1: j + 1 + length])
        
        # Move the pointer 'i' forward by the length of the string plus one (to skip the delimiter)
        i = j + 1 + length
    
    # Return the decoded list of strings
    return res