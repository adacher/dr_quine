NAME 			= Colleen Grace Sully

COLLEEN 		= Colleen
GRACE 			= Grace
SULLY 			= Sully

OBJCOLLEEN		= Colleen.o
OBJGRACE		= Grace.o
OBJSULLY		= Sully.o 

SRCCOLLEEN 		= Colleen.c
SRCGRACE 		= Grace.c
SRCGRACEKID		= Grace_kid.c
SRCSULLY 		= Sully.c

ALLOBJ			= Colleen.o Grace.o Sully.o
ALLSULLY 		= Sully_*.c Sully Sully_0 Sully_1 Sully_2 Sully_3 Sully_4 Sully_5

TMPCOLLEEN 		= tmp_colleen

all: $(NAME)

Colleen:
		Clang -Wall -Werror -Wextra -c $(SRCCOLLEEN)
		Clang -Wall -Werror -Wextra	$(OBJCOLLEEN) -o $(COLLEEN)
Grace:
		Clang -Wall -Werror -Wextra -c $(SRCGRACE)
		Clang -Wall -Werror -Wextra	$(OBJGRACE) -o $(GRACE)
Sully:
		Clang -Wall -Werror -Wextra -c $(SRCSULLY)
		Clang -Wall -Werror -Wextra	$(OBJSULLY) -o $(SULLY)
clean:
		rm -f $(ALLOBJ)

fclean: clean
		rm -f $(COLLEEN)
		rm -f $(GRACE)
		rm -f $(SRCGRACEKID)
		rm -f $(ALLSULLY)
		rm -f $(TMPCOLLEEN)

re: 	fclean all

.PHONY: all clean fclean re