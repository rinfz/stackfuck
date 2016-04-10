"""
Set of instructions for Stackfuck
"""

INSTRUCTIONS = (
    'P', # Push character onto stack (xxx - Number, xC - Character)
    'T', # Set variable to top of stack (xxxxx)
    'V', # Push variable value to top of stack (xxxxx)
    'C', # Create new buffer
    'S', # Select buffer (xxxxx)
    'O', # Print current buffer
    'I', # Read line and set to buffer
    'G', # Goto xxxxx if top is non-zero
    'g', # Relative goto (xxxxx)
    'N', # Goto xxxxx if top is zero
    'n', # Relative goto (xxxxx)
    'L', # Goto label xxxxx if top is non-zero
    'l', # Goto label xxxxx if top is zero
    'K', # Unconditionally goto label xxxxx
    'X', # Exit with signal xxxxx
    'x', # Exit with signal s
    '$', # Create label here xxxxx
    'A', # Concatenate buffer with xxxxx
    'a', # Put buffer onto stack
    '?', # Copy buffer xxxxx to current
    ')', # Clear stack
    '(', # Pop one from stack
    ';', # Move stack into selected buffer
    ':', # Move stack into selected buffer, reversed
    '+', # Add s-1 and s
    '-', # Subtract s from s-1
    '/', # Divide s-1 by s
    '*', # Multiply s-1 by s
    '^', # Xor s-1 with s
    '|', # BOr s-1 with s
    '&', # BAnd s-1 with s
    '\\', # LOr s-1 with s
    '7', # LAnd s-1 with s
    'Z', # Copy s-xxxxx to the top
    '<', # GT s-1 with s
    '>', # LT s-1 with s
    '.', # GE s-1 with s
    ',', # LE s-1 with s
    '=', # == s-1 with s
    '!', # != s-1 with s
    'E', # Checks if selected buffer is equal to xxxxx
)

# keyword: arglen
INSTRUCTIONS_WITH_ARGS = {
    'P': [2, 3],
    'T': 5,
    'V': 5,
    'S': 5,
    'G': 5,
    'g': 5,
    'N': 5,
    'n': 5,
    'L': 5,
    'l': 5,
    'K': 5,
    'X': 5,
    '$': 5,
    'A': 5,
    '?': 5,
    'Z': 5,
    'E': 5,
}
