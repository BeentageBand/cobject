#ifndef CONTAINER_T_H
#define CONTAINER_T_H
#include "cobject/ctemplate.h"

#ifdef CONTAINER_T_IMPLEMENTATION
#define _private
#else
#define _private const
#endif 

#ifndef Container_Params
#error "Container does not have any params"
#endif

#define Container_T TEMPLATE(Container, Container_Params)
#define T T_Param(1, Container_Params)
#define Container_T_Class TEMPLATE(Container, Container_Params, Class)
#define Container_T_populate TEMPLATE(Container, Container_Params, populate)
#define Container_T_get_shape TEMPLATE(Container, Container_Params, get_shape)
#define Get_Container_T_Class TEMPLATE(Get, Container, Container_Params, Class)

#ifdef __cplusplus
extern "C" {
#endif

union Container_T;
union Container_T_Class
{
    
    struct
    {
    struct Class Class;
    T (* _private get_shape)(union Container_T * const container);

    };
};

union Container_T
{
    union Container_T_Class * vtbl;
        struct
    {
      union Object Object;
      T _private shape;

    };
};

extern union Container_T_Class * Get_Container_T_Class(void);

extern void Container_T_populate(union Container_T * const container, T const shape);

extern T Container_T_get_shape(union Container_T * const container);

#ifdef __cplusplus
}
#endif
#undef Get_Container_T_Class
#undef Container_T_get_shape
#undef Container_populate
#undef Container_T_Class
#undef T
#undef Container_T
#undef _private
#endif /* defined(CONTAINER_H) || defined(Container_Params) */
