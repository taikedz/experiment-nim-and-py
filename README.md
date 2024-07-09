# Using nimpy

Using nimpy for bridging use of python and nim code together

See <https://github.com/yglukhov/nimpy> for example code for actually writing the files, then see below for the scenarios.

Nim is a language that compiles to a number of targets including JavaScript and others - as well as to machine code through cross-compilation to C.

What interests me here is the use of Nim with Python, both with Nim as a source to produce fast native libraries; as well as writing Nim programs serving as an engine that can then be scripted using python.

* Modules can be written in nim as desired, and leveraged directly from python
* Nim programs can be written with an interfacing to Python, using a locally installed python interpreter

Notice that in both cases, Nim can be used to leverage the wider C library space, compiling down to a module,
and then allowing a Python script to benefit from the arbitrarily exposed functions.

Benefit from C, without writing C.


## Creating a nim library called from python

Write the nim file, then compile with

```sh
nimpy-c() {
    local modname="${1%*.nim}"
    nim c --app:lib --out:"$modname".so --threads:on "$modname"
}

nimpy-c myfile.nim
```

## Calling python from nim

When building a nimpy program:

* ensure a local `*.nimble` file exists , run `nimble add nimpy`

When running nimpy program, you need

* `python3`
* `python3-pip`
* `pip install find_libpython`

This allows running a compiled engine written in nim, with scripting provided in python !

