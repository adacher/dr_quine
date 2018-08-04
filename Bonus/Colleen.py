#1
def function():
	pass
def main():
	#2
	s='#1{gd}def function():{gd}{tab}pass{gd}def main():{gd}{tab}#2{gd}{tab}s={qt}{quine}{qt}{gd}{tab}function(){gd}{tab}print(s.format(quine=s, tab=chr(9), gd=chr(10), qt=chr(39)), end={qt}{qt}){gd}{gd}if __name__== {qt}__main__{qt}:{gd}{tab}main()'
	function()
	print(s.format(quine=s, tab=chr(9), gd=chr(10), qt=chr(39)), end='')

if __name__== '__main__':
	main()