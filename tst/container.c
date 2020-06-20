
#include "container-internal.h"

#define container_t_override TEMPLATE(container, Container_Params, override)
#define container_t_delete TEMPLATE(container, Container_Params, delete)
#define container_t_get_shape TEMPLATE(container, Container_Params, get_shape)

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
