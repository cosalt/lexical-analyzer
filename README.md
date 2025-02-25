# Lexical Analyzer

A simple Lexical Analyzer built in Python that tokenizes source code based on predefined keywords and symbols.

## Features
- Reads source code from a file (`sourcecode.txt`).
- Ignores comments (lines starting with `#`) and empty lines.
- Uses a predefined keyword table to assign hexadecimal values to keywords and operators.
- Maintains a symbol table for identifiers and assigns unique hexadecimal values dynamically.
- Outputs the tokenized list of hexadecimal values.

## How It Works
1. The program reads `sourcecode.txt` and strips out comments and blank lines.
2. It splits each line into individual tokens (words, symbols, numbers, etc.).
3. Keywords and operators are mapped to predefined hexadecimal values.
4. Identifiers are stored in the symbol table and assigned unique hexadecimal values starting from `0x50`.
5. The final tokenized representation is printed in hexadecimal format.

## Keyword Table
The analyzer recognizes the following keywords and operators:

| Keyword/Operator | Hex Value |
|-----------------|-----------|
| `if`           | `0x01`    |
| `input`        | `0x02`    |
| `int`          | `0x03`    |
| `for`          | `0x04`    |
| `def`          | `0x05`    |
| `return`       | `0x06`    |
| `while`        | `0x07`    |
| `print`        | `0x08`    |
| `+`           | `0x09`    |
| `=`           | `0x10`    |
| `*`           | `0x11`    |
| `/`           | `0x12`    |
| `(`           | `0x13`    |
| `)`           | `0x14`    |
| `:`           | `0x15`    |
| `,`           | `0x16`    |

## Installation & Usage
1. Clone this repository:
   ```sh
   git clone https://github.com/cosalt/lexical-analyzer.git
   cd lexical-analyzer
   ```
2. Ensure you have Python installed.
3. Place your source code in `sourcecode.txt`.
4. Run the script:
   ```sh
   python lexical_analyzer.py
   ```
5. View the tokenized output in the terminal.

## Example
### Input (`sourcecode.txt`):
```
if x == 5:
    print("Hello")
```

### Output:
```
1 50 10 51 15
8 52
```

## Future Improvements
- Add support for more complex tokenization, including numbers and string literals.
- Implement a full lexical analysis with error handling.
- Provide a structured output format (e.g., JSON, CSV).

## Contributing
Feel free to fork the repository and submit pull requests for improvements!

## License
This project is open-source under the MIT License.

