#ifndef Container_Params
#error "Container_Params is not defined"
#endif

#define Container_T TEMPLATE(Container, Container_Params)
#define Container_T_Class TEMPLATE(Container, Container_Params, Class)
#define Get_Container_T_Class TEMPLATE(Get, Container, Container_Params, Class)
#define Container_T_get_shape TEMPLATE(Container, Container_Params, get_shape)
#define container_t_override TEMPLATE(container, Container_Params, override)
#define container_t_get_shape TEMPLATE(container, Container_Params, get_shape)
#define Container_T_populate TEMPLATE(Container, Container_Params, populate)

#define T T_Param(1, Container_Params)

#include "container.c"

#undef Container_T
#undef Container_T_Class
#undef Get_Container_T_Class
#undef Container_T_get_shape
#undef container_t_override
#undef container_t_get_shape
#undef Container_T_populate

#undef T
