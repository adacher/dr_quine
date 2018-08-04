import sys
import os
import subprocess

def main():
	i = 5
	file_name = os.path.basename(sys.argv[0])
	
	if file_name != 'Sully.py':
		i -= 1
	with open ('Sully_' + str(i) + '.py', 'w') as f:
		s='import sys{gd}import os{gd}import subprocess{gd}{gd}def main():{gd}{tab}i = {inti}{gd}{tab}file_name = os.path.basename(sys.argv[0]){gd}{gd}{tab}if file_name != {qt}Sully.py{qt}:{gd}{tab}{tab}i -= 1{gd}{tab}with open ({qt}Sully_{qt} + str(i) + {qt}.py{qt}, {qt}w{qt}) as f:{gd}{tab}{tab}s={qt}{quine}{qt}{gd}{tab}{tab}f.write(s.format(quine=s, inti=i, tab=chr(9), gd=chr(10), qt=chr(39))){gd}{tab}if i == 0:{gd}{tab}{tab}sys.exit(0){gd}{tab}run = {qt}python3 {qt} + {qt}Sully_{qt} + str(i) + {qt}.py{qt}{gd}{tab}subprocess.call(run.split()){gd}{gd}if __name__ == {qt}__main__{qt}:{gd}{tab}main()'
		f.write(s.format(quine=s, inti=i, tab=chr(9), gd=chr(10), qt=chr(39)))
	if i == 0:
		sys.exit(0)
	run = 'python3 ' + 'Sully_' + str(i) + '.py'
	subprocess.call(run.split())

if __name__ == '__main__':
	main()