 ACLOCAL_AMFLAGS = -I m4 --install
# Libraries
lib_LTLIBRARIES = libcobject-1.0.0.la
libcobject_1_0_0_la_SOURCES = cobject/cobject.c  cobject/cobject.h  cobject/ctemplate.h  cobject/xmac.h
libcobject_1_0_0_la_LDFLAGS = -version-info 0:0:0
nobase_include_HEADERS = cobject/cobject.h cobject/ctemplate.h cobject/xmac.h

# Unit Tests
check_PROGRAMS = unittest
unittest_SOURCES = \
tst/circle.c                 \
tst/circle.h                 \
tst/cobject-test.cc          \
tst/container-circle.c       \
tst/ctemplate-test.cc        \
tst/rectangle.c              \
tst/rectangle.h              \
tst/shape.c                  \
tst/shape.h

pkgconfig_DATA = cobject.pc

unittest_CPPFLAGS = $(libgmock_main_CFLAGS)
unittest_LDADD = $(lib_LTLIBRARIES) $(libgmock_main_LIBS)
unittest_LDFLAGS = -no-install

EXTRA_DIST = m4/NOTES
dist_doc = README.md LICENSE
