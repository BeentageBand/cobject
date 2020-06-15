#ifndef Container_Params
#error "Container does not have any params"
#endif

#define Container_T TEMPLATE(Container, Container_Params)
#define T T_Param(1, Container_Params)
#define Container_T_Class TEMPLATE(Container, Container_Params, Class)
#define Get_Container_T_Class TEMPLATE(Get, Container, Container_Params, Class)
#define Container_T_populate TEMPLATE(Container, Container_Params, populate)
#define Container_T_get_shape TEMPLATE(Container, Container_Params, get_shape)

#define container_t_override TEMPLATE(container, Container_Params, override)
#define container_t_delete TEMPLATE(container, Container_Params, delete)
#define container_t_copy TEMPLATE(container, Container_Params, copy)
#define container_t_compare TEMPLATE(container, Container_Params, compare)
#define container_t_get_shape TEMPLATE(container, Container_Params, get_shape)

#include "container-internal.h"

static T container_t_get_shape(union Container_T * const container);

void container_t_override(union Container_T_Class * const clazz) {
    clazz->get_shape = container_t_get_shape;
}

void container_t_delete(union Container_T * const container) {
//  _delete(&container->shape);
}

T container_t_get_shape(union Container_T * const container) {
  return container->shape;
}

void Container_T_populate(union Container_T * const container, T const shape) {
    Object_populate(&container->Object, &Get_Container_T_Class()->Class);
    _copy(&container->shape, &shape);
}

#undef container_t_override
#undef container_t_delete
#undef container_t_copy
#undef container_t_compare
#undef container_t_get_shape

#undef Container_T_get_shape
#undef Container_populate
#undef Get_Container_T_Class
#undef Container_T_Class
#undef T
#undef Container_T
