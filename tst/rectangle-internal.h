#ifndef RECTANGLE_INT_H
#define COBJECT_IMPLEMENTATION

#include "rectangle.h"

static void rectangle_override(union Rectangle_Class * const rectangle);
static void rectangle_delete(union Rectangle * const rectangle);

union Rectangle_Class * Get_Rectangle_Class(void)
{
  static union Rectangle_Class clazz;
  if (NULL != clazz.Class.destroy) return &clazz;
  Class_populate(&clazz.Class, sizeof(clazz),
		 Get_Shape_Class(),
		 (Class_Delete_T)rectangle_delete);
  rectangle_override(&clazz);
  return &clazz;
}
char const * Rectangle_get_name(union Rectangle * const rectangle)
{
  return rectangle->vtbl->get_name(rectangle);
}

void Rectangle_print_info(union Rectangle * const rectangle)
{
  return rectangle->vtbl->print_info(rectangle);
}

float Rectangle_get_height(union Rectangle * const rectangle)
{
  return rectangle->vtbl->get_height(rectangle);
}

float Rectangle_get_width(union Rectangle * const rectangle)
{
  return rectangle->vtbl->get_width(rectangle);
}


#endif /* RECTANGLE_INT_H */
