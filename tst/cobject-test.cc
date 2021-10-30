/*
 * cobject-test.cc
 *
 *  Created on: Oct 21, 2019
 *      Author: roalanis
 */

#include <gtest/gtest.h>

#include "circle.h"
#include "rectangle.h"
#include "shape.h"

static char const *Circle_Name = "circle";
static union Circle Circle = {NULL};

static char const *Rectangle_Name = "rectangle";
static union Rectangle Rectangle = {NULL};

TEST(ShapeClass, override) {
  union Shape_Class *clazz = Get_Shape_Class();
  ASSERT_TRUE(NULL != clazz);
  ASSERT_TRUE(NULL != clazz->Class.destroy);

  ASSERT_EQ(sizeof(union Shape_Class), clazz->Class.offset);

  ASSERT_TRUE(NULL != clazz->get_name);
  ASSERT_TRUE(NULL != clazz->print_info);
}

TEST(CircleClass, override) {
  union Circle_Class *clazz = Get_Circle_Class();
  ASSERT_TRUE(NULL != clazz);
  ASSERT_TRUE(NULL != clazz->Class.destroy);

  ASSERT_EQ(sizeof(union Circle_Class), clazz->Class.offset);

  ASSERT_TRUE(NULL != clazz->get_name);
  ASSERT_TRUE(NULL != clazz->print_info);
  ASSERT_TRUE(NULL != clazz->get_radius);
}

TEST(RectangleClass, override) {
  union Rectangle_Class *clazz = Get_Rectangle_Class();
  ASSERT_TRUE(NULL != clazz);
  ASSERT_TRUE(NULL != clazz->Class.destroy);

  ASSERT_EQ(sizeof(union Rectangle_Class), clazz->Class.offset);

  ASSERT_TRUE(NULL != clazz->get_name);
  ASSERT_TRUE(NULL != clazz->print_info);
  ASSERT_TRUE(NULL != clazz->get_height);
  ASSERT_TRUE(NULL != clazz->get_width);
}

TEST(Constructor, Circle) {

  float r = 0.1;
  Circle_populate(&Circle, Circle_Name, r);

  ASSERT_TRUE(NULL != Circle.vtbl);

  ASSERT_EQ(r, Circle_get_radius(&Circle));
  ASSERT_EQ(Circle_Name, Circle_get_name(&Circle));

  Circle_print_info(&Circle);
}

TEST(Constructor, Rectangle) {
  float h = 0.1;
  float w = 0.1;

  Rectangle_populate(&Rectangle, Rectangle_Name, h, w);

  ASSERT_EQ(h, Rectangle_get_height(&Rectangle));
  ASSERT_EQ(w, Rectangle_get_width(&Rectangle));
  ASSERT_EQ(Rectangle_Name, Rectangle_get_name(&Rectangle));

  Rectangle_print_info(&Rectangle);
}

TEST(Interface, Shape) {
  union Shape *shape[] = {&Circle.Shape, &Rectangle.Shape};

  printf("shape 0\n");
  Shape_print_info(shape[0]);
  ASSERT_TRUE(&Circle != _cast(shape[0], Circle));
  ASSERT_EQ(Circle_Name, Shape_get_name(shape[0]));

  printf("shape 1\n");
  Shape_print_info(shape[1]);
  ASSERT_TRUE(&Rectangle != _cast(shape[1], Rectangle));
  ASSERT_EQ(Rectangle_Name, Shape_get_name(shape[1]));
}

TEST(Shape, equals) {
  ASSERT_NE(0, _compare(&Circle, &Rectangle));
  ASSERT_EQ(0, _compare(&Rectangle, &Rectangle));
}


TEST(Dynamic, new_and_delete) {
  union Rectangle * r = _new(union Rectangle);
  Rectangle_populate(r, Rectangle_Name, 0.1, 0.1);

  _delete(r);
}
