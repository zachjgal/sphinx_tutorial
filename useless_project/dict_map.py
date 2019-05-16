def dict_map(f, d): 
    """ Pretty cool one-liner, eh? I didn't even copy it from Stack Overflow.
    """
    return {k: f(v) if not isinstance(v, dict) else dict_map(f, v) for k, v in d.items()}
