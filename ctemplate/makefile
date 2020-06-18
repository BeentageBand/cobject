INCS=$(wildcard *.h)

.PHONY : all clean $(MAKECMDGOALS:%=%.cmd)

all : install

install: ../$(OUT)/include/ctemplate/ $(INCS:%=../$(OUT)/include/ctemplate/%)
	@echo "install ctemplate.."

clean : 
	@echo "clean all-tst"
	rm -rf *.o *.lib

../$(OUT)/include/ctemplate/%.h : %.h
	cp -f $(realpath $^) $@;

../$(OUT)/include/ctemplate/ : 
	-mkdir -p $@;