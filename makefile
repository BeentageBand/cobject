export CXX=gcc
export CPP=g++
export TEST_DEPS=gmock_main gtest gmock
export DEPS=
export LDFLAGS=$(shell pkg-config --libs --static $(DEPS) $(TEST_DEPS))
export CXXFLAGS=-std=gnu++11 $(shell pkg-config --cflags $(DEPS) $(TEST_DEPS)) 
export CFLAGS=-std=gnu11 $(shell pkg-config --cflags $(DEPS) $(TEST_DEPS)) 
export OUT=out
export SUBDIRS=cobject ctemplate
ifndef test
test=dummy-test
endif

TEST_LDFLAGS=$(shell pkg-Config --libs --static $(TEST_DEPS))

.PHONY: all clean install test $(SUBDIRS:%=%-all) $(SUBDIRS:%=%-clean) tst-all tst-clean

all : install test

install : $(OUT)/bin $(OUT)/lib $(SUBDIRS:%=%-all)

clean : $(SUBDIRS:%=%-clean) tst-clean

clobber : clean
	-rm -rf $(OUT)

test : tst-all
	@$(OUT)/bin/unit-test;

$(OUT) $(OUT)/bin $(OUT)/lib $(SUBDIRS:%=$(OUT)/include/%) : 
	-mkdir -p $@;

$(SUBDIRS:%=%-all) tst-all : 
	make all -C $(@:%-all=%);

$(SUBDIRS:%=%-clean) tst-clean :
	make clean -C $(@:%-clean=%);
