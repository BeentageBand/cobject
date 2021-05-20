#include "container-circle.h"
#include <gtest/gtest.h>

TEST(Container, Populate) {
  union Circle circle = {NULL};
  static char const *circle_name = "Circle";
  Circle_populate(&circle, circle_name, 1.9);

  ASSERT_FALSE(NULL == Circle_get_name(&circle));
  ASSERT_STREQ(Circle_get_name(&circle), circle_name);

  union Container_Circle container = {NULL};
  Container_Circle_populate(&container, circle);

  ASSERT_FALSE(container.shape.name == NULL);
  ASSERT_STREQ(container.shape.name, circle_name);

  ASSERT_FALSE(container.shape.vtbl == NULL);
  ASSERT_TRUE(container.shape.vtbl == Get_Circle_Class());

  union Circle actual_circle = Container_Circle_get_shape(&container);
  ASSERT_FALSE(NULL == actual_circle.name);
  ASSERT_STREQ(actual_circle.name, circle_name);
  ASSERT_FALSE(NULL == actual_circle.vtbl);
  ASSERT_TRUE(actual_circle.vtbl == Get_Circle_Class());
}
