#ifndef CONTAINER_INT_H
#define CONTAINER_INT_H

#define CONTAINER_IMPLEMENTATION

#include "container.h"

static void container_override(union Container_Class * const container);

union Container_Class * Get_Container_Class(void)
{
  static union Container_Class clazz;
  if (0 != clazz.Class.offset) return &clazz;
  Class_populate(&clazz.Class, sizeof(clazz), NULL);
  container_override(&clazz);
  return &clazz;
}
T Container_get_shape(union Container * const container)
{
  return container->vtbl->get_shape(container);
}


#endif /* CONTAINER_INT_H */
