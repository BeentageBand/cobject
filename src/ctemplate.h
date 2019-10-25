#ifndef CTEMPLATE_H_
#define CTEMPLATE_H_

#include "cobject.h"

#define TEMPLATE(...) EVAL4(WHILE(CHECK, TEMPLATE_CAT, __VA_ARGS__, dummy))
#define TEMPLATE_CAT(a, ...) CAT(a, IF( CHECK(__VA_ARGS__) )(CAT(_, __VA_ARGS__), ) )

#define Member_Name(...) TEMPLATE(__VA_ARGS__)
#define Method_Name(...) TEMPLATE(__VA_ARGS__)

#define SELECT_PARAM(num, t, ...) \
  IF(DEC(num)) \
  ( \
      OBSTRUCT(INDIRECT_SELECT) () \
      ( \
        DEC(num), __VA_ARGS__ \
      ) \
      , \
      t \
  )

#define INDIRECT_SELECT() SELECT_PARAM

#define T_Param(num, ...) CAT(EVAL4(SELECT_PARAM(num, __VA_ARGS__)), _T)

#endif /*CTEMPLATE_H_*/
