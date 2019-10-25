#ifndef SHAPE_INT_H
#define COBJECT_IMPLEMENTATION

#include "shape.h"

static void shape_override(union Shape_Class * const shape);
static void shape_delete(union Shape * const shape);

union Shape_Class * Get_Shape_Class(void)
{
  static union Shape_Class clazz;
  if (NULL != clazz.Class.destroy) return &clazz;
  Class_populate(&clazz.Class, sizeof(clazz),
		 NULL,
		 (Class_Delete_T)shape_delete);
  shape_override(&clazz);
  return &clazz;
}
char const * Shape_get_name(union Shape * const shape)
{
  return shape->vtbl->get_name(shape);
}

void Shape_print_info(union Shape * const shape)
{
  return shape->vtbl->print_info(shape);
}


#endif /* SHAPE_INT_H */
