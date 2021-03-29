Iterated-sums signature in Rust
===============================
This is an implementation of the one-dimensional iterated-sums signature in Rust,
with Python 3 bindings.

Installation
------------
First, clone the repository by running
`git clone https://github.com/ntapiam/o3iss.git`.

Build with
`cargo build --release`.
Depending on your system, this will produce a file named `libo3iss.dylib` (macOS), `libo3iss.so` (Unix) or `libo3iss.dll`.

To use the library, it needs to reside in the Python 3 path under the name `o3iss.so` (all systems).
So the file produced by `cargo` needs to be renamed and moved as needed.

Once this is done, it suffices to import the `o3iss` package in Python as
```python
import o3iss
```

Usage
-----
FOr the moment, this implementation offers only a single function: `o3iss.compute` with signature `(np.ndarray, int) -> np.ndarray`
where both the input and ouput arrays are one-dimensional.

TO DO
=====
[] Produce a proper Python package
