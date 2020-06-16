#include "circle-internal.h"

static float circle_get_radius(union Circle * const circle);

void circle_override(union Circle_Class * const circle) 
{
    circle->get_radius = circle_get_radius;
}

float circle_get_radius(union Circle * const circle)
{
    return circle->radius;
}

void Circle_populate(union Circle * const circle,char const * name,float radius)
{
    Shape_populate(&circle->Shape, name);
    circle->vtbl = Get_Circle_Class();
    circle->radius = radius;
}
