A=0
B=0

def main():
	#1
	s='A=0{gd}B=0{gd}{gd}def main():{gd}{tab}#1{gd}{tab}s={qt}{quine}{qt}{gd}{tab}with open({qt}Grace_kid.py{qt}, {qt}w{qt}) as f:{gd}{tab}{tab}f.write(s.format(quine=s, tab=chr(9), gd=chr(10), qt=chr(39))){gd}{gd}C=main{gd}{gd}if __name__ == {qt}__main__{qt}:{gd}{tab}C()'
	with open('Grace_kid.py', 'w') as f:
		f.write(s.format(quine=s, tab=chr(9), gd=chr(10), qt=chr(39)))

C=main

if __name__ == '__main__':
	C()