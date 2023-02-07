# Importing the library for the shift amount
import shift_lib
encodeLib = shift_lib.encode_lib

inp = input()
shift = input()

# Turning the inputted shift amount to an integer
shift = int(shift) * 1

# Making sure shift is between 1 and 10
if shift > 10:
    shift = 10
elif shift < 1:
    shift = 1

# Gets the character that will determine the shift amount when decoding
shift_character = encodeLib.get(shift, None)

# Splitting the input into a list so that each character can be shifted
input_split = list(inp)

# Converts the characters to ascii
ascii_codes = [ord(char) for char in input_split]

# Shifts up the ascii codes by shift amount
# Doesnt shift if the character is a space
shifted_ascii = [int + shift if int != 32 else 32 for int in ascii_codes]

# If a ascii is to large, round to 33
shifted_ascii_corrected = [33 if int > 126 else int for int in shifted_ascii]

# Convert back to text
text_coded_output = [chr(int) for int in shifted_ascii_corrected]

# Combines the shift character with the coded text
full_coded_output = shift_character + ' ' + ''.join(text_coded_output)

print(full_coded_output)