Jython
    В Δ от CPython ⊅ эффективной реализации конкатенации str в exp вида:
        a += b
        a = b + a
        # -> исп .join()

PyPy

IronPython

Pyrex

Psyco