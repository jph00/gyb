# gyb
A pip-installable version of Apple's gyb python-based templating tool. To install:

    pip install gyb

To learn how to use it, see this great [blog post](https://nshipster.com/swift-gyb/).

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
