from pprint import pprint

pprint(
    [{'bin': bin(n), 'dec': n, 'hex': hex(n), 'oct': oct(n)} for n in range(16)]
)