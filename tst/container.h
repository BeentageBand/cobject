#if !defined(CONTAINER_H) || defined(Container_Params)
#define CONTAINER_H

#include "ctemplate.h"

#define Container_T TEMPLATE(Container, Container_Params)
#define Container_Class TEMPLATE(Container, Container_Params, Class)
#define Get_Container_Class TEMPLATE(Get, Container, Container_Params, Class)
#define Container_populate TEMPLATE(Container, Container_Params, populate)
#define Container_get_shape TEMPLATE(Container, Container_Params, get_shape)
#define T T_Param(1, Container_Params)

#ifdef __cplusplus
extern "C" {
#endif

union Container_T;
union Container_Class {
    struct {
        struct Class Class;
        T (* _private get_shape)(union Container_T * const container);
    };
};

union Container_T
{
    union Container_Class * vtbl;
    struct
    {
      union Object Object;
      T _private shape;
    };
};

extern union Container_Class * Get_Container_Class(void);

extern void Container_populate(union Container_T * const container, T const shape);

extern T Container_get_shape(union Container_T * const container);

#ifdef __cplusplus
}
#endif

#undef Container_T
#undef Container_Class
#undef Get_Container_Class
#undef Container_populate
#undef Container_get_shape

#endif /* CONTAINER_H */
