#ifndef CIRCLE_INT_H
#define CIRCLE_INT_H
#define CIRCLE_IMPLEMENTATION

#include "circle.h"

static void circle_override(union Circle_Class *const circle);

union Circle_Class *Get_Circle_Class(void) {
  static union Circle_Class clazz;
  if (0 != clazz.Class.offset)
    return &clazz;
  Class_populate(&clazz.Class, sizeof(clazz), &Get_Shape_Class()->Class);
  circle_override(&clazz);
  return &clazz;
}
char const *Circle_get_name(union Circle *const circle) {
  return circle->vtbl->get_name(circle);
}

void Circle_print_info(union Circle *const circle) {
  return circle->vtbl->print_info(circle);
}

float Circle_get_radius(union Circle *const circle) {
  return circle->vtbl->get_radius(circle);
}

#endif /*CIRCLE_INT_H*/
