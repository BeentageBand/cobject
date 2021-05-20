#ifndef CONTAINER_T_INT_H
#define CONTAINER_T_INT_H
#define CONTAINER_T_IMPLEMENTATION

#include "container.h"

static void container_t_override(union Container_T_Class *const container_t);

union Container_T_Class *Get_Container_T_Class(void) {
  static union Container_T_Class clazz;
  if (0 != clazz.Class.offset)
    return &clazz;
  Class_populate(&clazz.Class, sizeof(clazz), NULL);
  container_t_override(&clazz);
  return &clazz;
}
T Container_T_get_shape(union Container_T *const container_t) {
  return container_t->vtbl->get_shape(container_t);
}

#endif /*CONTAINER_T_INT_H*/
