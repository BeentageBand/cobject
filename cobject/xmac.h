#ifndef XMAC_H_
#define XMAC_H_

#define PRIMITIVE_CAT(a, ...) a##__VA_ARGS__
#define CAT(a, ...) PRIMITIVE_CAT(a, __VA_ARGS__)

#define PRIMITIVE_STR(a) #a
#define STR(a) PRIMITIVE_STR(a)

#define IFF(c) PRIMITIVE_CAT(IFF_, c)
#define IFF_0(t, ...) __VA_ARGS__
#define IFF_1(t, ...) t

#define COMPL(x) PRIMITIVE_CAT(COMPL_, x)
#define COMPL_0 1
#define COMPL_1 0

#define CHECK_N(x, n, ...) n
#define CHECK(...) CHECK_N(__VA_ARGS__, 0, )
#define PROBE(x) x, 1,

#define NOT(x) CHECK(PRIMITIVE_CAT(NOT_, x))
#define NOT_0 PROBE(~)

#define BOOL(c) COMPL(NOT(c))
#define IF(c) IFF(BOOL(c))

#define EAT(...)
#define EXPAND(...) __VA_ARGS__
#define WHEN(c) IF(c)(EXPAND, EAT)

#define EMPTY()
#define DEFER(i) i EMPTY()
#define OBSTRUCT(...) __VA_ARGS__ DEFER(EMPTY)()

#define EVAL(...) EVAL1(EVAL1(EVAL1(__VA_ARGS__)))
#define EVAL1(...) EVAL2(EVAL2(EVAL2(__VA_ARGS__)))
#define EVAL2(...) EVAL3(EVAL3(EVAL3(__VA_ARGS__)))
#define EVAL3(...) EVAL4(EVAL4(EVAL4(__VA_ARGS__)))
#define EVAL4(...) EVAL5(EVAL5(EVAL5(__VA_ARGS__)))
#define EVAL5(...) __VA_ARGS__

#define WHILE(pred, macro, ...)                                                \
  IF(pred(__VA_ARGS__))                                                        \
  (OBSTRUCT(WHILE_INDIRECT)()(pred, macro, macro(__VA_ARGS__)), __VA_ARGS__)

#define WHILE_INDIRECT() WHILE

#define DEC(num) CAT(DEC_, num)

#define DEC_1 0
#define DEC_2 1
#define DEC_3 2
#define DEC_4 3
#define DEC_5 4
#define DEC_6 5
#define DEC_7 6
#define DEC_8 7
#define DEC_9 8
#define DEC_10 9

#endif /*XMAC_H_*/
