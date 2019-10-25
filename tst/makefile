CSRCS=$(wildcard *.c)
CCSRCS=$(wildcard *.cc)
TEST=unit-test

.PHONY : all clean 

all : ../$(OUT)/bin/$(TEST)
	@echo "compiling all-tst";

clean : 
	@echo "clean all-tst";
	rm -rf $(CSRCS:.c=.o) $(CCSRCS:.cc=.o)

../$(OUT)/bin/$(TEST) : $(TEST)
	-cp -sf $(realpath $^) $@;

$(TEST) : $(CSRCS:.c=.o) $(CCSRCS:.cc=.o)
	$(CPP) $(CXXFLAGS) $(SUBDIRS:%=-I ../%) $(LDFLAGS) -L ../$(OUT)/lib -lcobject -o $@ $^;

%.o : %.cc
	$(CPP) $(CXXFLAGS) $(SUBDIRS:%= -I ../%) -o $@ -c $^;

%.o : %.c
	$(CXX) $(CFLAGS) $(SUBDIRS:%= -I ../%) -o $@ -c $^;
