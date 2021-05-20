/*
 * rectangle.c
 *
 *  Created on: Oct 25, 2019
 *      Author: roalanis
 */
#include "rectangle-internal.h"

static float rectangle_get_height(union Rectangle *const rectangle);
static float rectangle_get_width(union Rectangle *const rectangle);

void Rectangle_populate(union Rectangle *const rectangle,
                        char const *const name, float const height,
                        float const width) {
  Shape_populate(&rectangle->Shape, name);
  rectangle->vtbl = Get_Rectangle_Class();
  rectangle->height = height;
  rectangle->width = width;
}

void rectangle_override(union Rectangle_Class *const rectangle) {
  rectangle->get_height = rectangle_get_height;
  rectangle->get_width = rectangle_get_width;
}

float rectangle_get_height(union Rectangle *const rectangle) {
  return rectangle->height;
}

float rectangle_get_width(union Rectangle *const rectangle) {
  return rectangle->width;
}
