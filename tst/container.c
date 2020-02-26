/*
 * container.c
 *
 *  Created on: Nov 10, 2019
 *      Author: roalanis
 */

#include "container-internal.h"

#define Container_populate TEMPLATE(Container, Container_Params, populate)
#define container_get_shape TEMPLATE(container, Container_Params, get_shape)

static T container_get_shape(union Container_T * const container);

void container_override(union Container_Class * const clazz) {
    clazz->get_shape = container_get_shape;
}

void container_delete(union Container_T * const container) {
//  _delete(&container->shape);
}

T container_get_shape(union Container_T * const container) {
  return container->shape;
}

void Container_populate(union Container_T * const container, T const shape) {
    Object_populate(&container->Object, &Get_Container_Class()->Class);
    container->shape = shape;
}

#undef T
#undef container_override
#undef container_delete
#undef Container_T
#undef Container_Class
#undef Get_Container_Class
#undef Container_populate
#undef container_get_shape
