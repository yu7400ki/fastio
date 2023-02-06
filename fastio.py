def fastio(f):
    import builtins, functools, io, os, sys

    buf = io.BytesIO()
    builtin_print = builtins.print
    builtin_input = builtins.input

    def fast_print(arg, *args, sep=" ", end="\n", **_):
        sep = sep.encode()
        end = end.encode()
        buf.write(str(arg).encode())
        for arg in args:
            buf.write(sep)
            buf.write(str(arg).encode())
        buf.write(end)

    def fast_input():
        return sys.stdin.readline().rstrip()

    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        builtins.print = fast_print
        builtins.input = fast_input
        res = f(*args, **kwargs)
        os.write(1, buf.getvalue())
        buf.seek(0)
        buf.truncate(0)
        builtins.print = builtin_print
        builtins.input = builtin_input
        return res

    return wrapper

@fastio
def solve():
    pass

if __name__ == "__main__":
    solve()
