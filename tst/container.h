#ifndef CONTAINER_T_H
#define CONTAINER_T_H
#include "cobject/ctemplate.h"

#ifdef CONTAINER_T_IMPLEMENTATION 
#define container_t_private
#else
#define container_t_private const
#endif 

#ifdef __cplusplus
extern "C" {
#endif

union Container_T;
union Container_T_Class
{
    
    struct
    {
    struct Class Class;
    T (* container_t_private get_shape)(union Container_T * const container_t);

    };
};

union Container_T
{
    union Container_T_Class * vtbl;
        struct
    {
      union Object Object;
      T container_t_private shape;

    };
};

extern union Container_T_Class * Get_Container_T_Class(void);

extern void Container_T_populate(union Container_T * const container_t, T const shape);

extern T Container_T_get_shape(union Container_T * const container_t);

#ifdef __cplusplus
}
#endif
#endif /*CONTAINER_T_H*/
