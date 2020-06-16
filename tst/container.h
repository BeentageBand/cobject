#ifndef CONTAINER_H
#define CONTAINER_H
#include "cobject/cobject.h"

#ifdef CONTAINER_IMPLEMENTATION 
#define _private
#else
#define _private const
#endif 

#ifdef __cplusplus
extern "C" {
#endif

union Container;
union Container_Class
{
    
    struct
    {
    struct Class Class;
    T (* _private get_shape)(union Container * const container);

    };
};

union Container
{
    union Container_Class * vtbl;
        struct
    {
      union Object Object;
      T _private shape;

    };
};

extern union Container_Class * Get_Container_Class(void);

extern void Container_populate(union Container * const container, T const shape);

extern T Container_get_shape(union Container * const container);

#ifdef __cplusplus
}
#endif
#endif /* CONTAINER_H */