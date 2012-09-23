
from grammar.grammar import *



G = (r"""
Exp => Term [+-] Exp | Term
Term => Factor [*/] Term | Factor
Factor => Funcall | Var | Num | [(] Exp [)]
Funcall => Var [(] Exps [)]
Exps => Exp [,] Exps | Exp
Var => [a-zA-Z_]\w*
Num => [-+]?[0-9]+([.][0-9]*)?
""")



def test():
	""""""

	g = grammar(G)
	for key, value in g.items():
		print '{}: {}'.format(key, value)



if __name__ == '__main__':
	test()