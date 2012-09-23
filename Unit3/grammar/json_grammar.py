JSON_GRAMMAR = """
object => { members } | {}
members => pair , members | pair
pair => string : value
array => \[ elements \] | \[\]
elements => value , elements | value
value => string | object | array | number | true | false | null
string => \"[^\"]*?\"
char => [a-zA-Z]+
number => int frac exp | int exp | int frac | int
int => -?[0-9]+
frac => \.[0-9]+
exp => e[+-][0-9]+
"""