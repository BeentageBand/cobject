export CXX=gcc
export CPP=g++
export TEST_DEPS=gmock_main gtest gmock
export DEPS=
export LDFLAGS=$(shell pkg-config --libs --static $(DEPS) $(TEST_DEPS))
export CXXFLAGS=-std=gnu++11 $(shell pkg-config --cflags $(DEPS) $(TEST_DEPS)) 
export CFLAGS=-std=gnu11 $(shell pkg-config --cflags $(DEPS) $(TEST_DEPS)) 
export OUT=out
export SUBDIRS=$(OUT)/include/cobject
ifndef test
test=dummy-test
endif

INSTALL_LIB=libcobject.lib
INSTALL_INC=cobject.h xmac.h

TEST_LDFLAGS=$(shell pkg-Config --libs --static $(TEST_DEPS))

.PHONY: all clean install test $(SUBDIRS:%=%-clean)

all : install test

install : $(OUT)/bin $(OUT)/lib
	@make all -C src;

clean : src-clean tst-clean

clobber : clean
	-rm -rf $(OUT)

test : 
	@make all -C tst;
	@$(OUT)/bin/unit-test;


$(OUT) $(OUT)/bin $(OUT)/lib $(OUT)/include/cobject : 
	-mkdir -p $@;

%-clean : %
	-make clean -C $^;
