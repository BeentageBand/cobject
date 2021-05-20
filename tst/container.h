#ifndef CONTAINER_T_H
#define CONTAINER_T_H
#include "cobject/cobject.h"

#ifdef CONTAINER_T_IMPLEMENTATION
#define _private
#else
#define _private const
#endif

#ifdef __cplusplus
extern "C" {
#endif

union Container_T;
union Container_T_Class {

  struct {
    struct Class Class;
    T (*_private get_shape)(union Container_T *const container_t);
  };
};

union Container_T {
  union Container_T_Class *vtbl;
  struct {
    union Object Object;
    T _private shape;
  };
};

extern union Container_T_Class *Get_Container_T_Class(void);

extern void Container_T_populate(union Container_T *const container_t,
                                 T const shape);

extern T Container_T_get_shape(union Container_T *const container_t);

#ifdef __cplusplus
}
#endif
#undef _private
#endif /*CONTAINER_T_H*/