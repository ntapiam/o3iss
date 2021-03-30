Iterated-sums signature in Rust
===============================
This is an implementation of the one-dimensional iterated-sums signature in Rust,
with Python 3 bindings.

Installation
------------
First, clone the repository by running
`git clone https://github.com/ntapiam/o3iss.git`.

Then, install normally using `setuptools`:
```bash
cd o3iss
python3 ./setup.py install
```
Make sure the Python 3 packages `setuptools`, `setuptools-rust` and `wheel` are installed.

Once this is done, it suffices to import the `o3iss` package in Python as
```python
>> import o3iss
```

Usage
-----
FOr the moment, this implementation offers only a single function: `o3iss.compute` with signature `(np.ndarray, int) -> np.ndarray`
where both the input and ouput arrays are one-dimensional.

TO DO
=====
- [x] Produce a proper Python 3 package
