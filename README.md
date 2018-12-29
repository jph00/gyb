# gyb
A pip-installable version of Apple's gyb python-based templating tool. To install:

    pip install gyb

For help (assuming that the pip installed binaries path is in your `PATH`):

    gyb -h

To use:

    gyb file.ext.gyb -o file.ext

For details, see this great [blog post](https://nshipster.com/swift-gyb/).

## Summary (from `gyb -h`)

A GYB template consists of the following elements:

- Literal text which is inserted directly into the output
- `%%` or `$$` in literal text, which insert literal '%' and '$' symbols respectively.
- Substitutions of the form `${<python-expression>}`. The Python expression is converted to a string and the result is inserted into the output.
- Python code delimited by `%{...}%`. Typically used to inject definitions (functions, classes, variable bindings) into the evaluation context of the template. Common indentation is stripped, so you can add as much indentation to the beginning of this code as you like
- Lines beginning with optional whitespace followed by a single '%' and Python code. %-lines allow you to nest other constructs inside them. To close a level of nesting, use the `%end` construct.
- Lines beginning with optional whitespace and followed by a single '%' and the token "end", which close open constructs in %-lines.

## Some examples

Create implementations of all the math operators:

```
% for op,f in zip('+-*/', 'add sub mul div'.split()):
  public static func ${op}  (lhs:Self, rhs:Self  ) -> Self { return lhs.${f}( rhs) }
% end
```

Define a variable:

```
%{ types = ('Float', 'Double') }%
```
