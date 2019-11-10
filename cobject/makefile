SRCS=$(wildcard *.c)
LIBS=libcobject.a
INCS=$(wildcard *.h)

.PHONY : all clean $(MAKECMDGOALS:%=%.cmd)

all : install

install: ../$(OUT)/include/cobject/ $(LIBS:%=../$(OUT)/lib/%) $(INCS:%=../$(OUT)/include/cobject/%)
	@echo "install cobject.."

clean : 
	@echo "clean all-tst"
	rm -rf *.o *.lib

$(LIBS) : $(SRCS:.c=.o)
	@echo "compiling $(LIBS)";
	$(AR) -rcs $@ $^;

$(LIBS:%=../$(OUT)/lib/%): $(LIBS)
	cp -sf $(realpath $^) $@;

../$(OUT)/include/cobject/%.h : %.h
	cp -sf $(realpath $^) $@;

../$(OUT)/include/cobject : 
	-mkdir -p $@;

%.o : %.c
	$(CXX) $(CFLAGS) $(SUBDIRS:%= -I ../%) -o $@ -c $^
