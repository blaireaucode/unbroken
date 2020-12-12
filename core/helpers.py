from inspect import currentframe


# for translate within fstring
def ff(s):
    frame = currentframe().f_back
    return eval(f"f'{s}'", frame.f_locals, frame.f_globals)
