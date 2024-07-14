import re

# Regular expression to detect function names, function pointers, and static
# constants
regex = (
    r"\b(?:static\s+const\s+[a-zA-Z_][a-zA-Z0-9_]*\s+"
    r"[a-zA-Z_][a-zA-Z0-9_]*\s*\[\]\s*=\s*\{[^}]*\};?)|"
    r"(?<!\belse\s)\b(?:[a-zA-Z_][a-zA-Z0-9_]*\s+)"
    r"?(?:\*?\(*\*?[a-zA-Z_][a-zA-Z0-9_]*\)?)\s*\([^)]*\)\s*"
    r"(?:\([^)]*\))?\s*\{"
)

# Sample code from different languages, including function pointers and static
# constants
# Sample code from different languages, including function pointers and static
# constants
sample_code = """
void myFunction() {
    // function body
}

int (*functionFactory)(int n) (int, int) {
    // function pointer body
}

int (*functionFactory)(int n) (int, int) {
    // another function pointer body
}

int computeSum(int a, int b) {
    return a + b;
}

int add(int a, int b) {
    return a + b;
}

const computeValue = (a, b) => {
    return a + b;
};

def my_python_function(param1, param2):
    pass

static const unsigned char saved_pac[] = {};

int fun() {}
else if (hello){}
"""

# Find all matches
matches = re.findall(regex, sample_code)

# Print the matches
for match in matches:
    print(match)
