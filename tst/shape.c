
#include <stdio.h>
#include "shape-internal.h"

static void shape_print_info(union Shape * const shape);
static char const * shape_get_name(union Shape * const shape);

void shape_override(union Shape_Class * const shape)
{
    shape->print_info = shape_print_info;
    shape->get_name = shape_get_name;
}

void shape_delete(union Shape * const shape) {}

void shape_print_info(union Shape * const shape)
{
    printf("Shape name: %s\n", shape->name);
}

char const * shape_get_name(union Shape * const shape)
{
    return shape->name;
}

void Shape_populate(union Shape * const shape, char const * name)
{
    Object_populate(&shape->Object, &Get_Shape_Class()->Class);
    shape->name = name;
}

