#ifndef CIRCLE_H
#define CIRCLE_H
#include "shape.h"

#ifdef CIRCLE_IMPLEMENTATION 
#define _private
#else
#define _private const
#endif 

#ifdef __cplusplus
extern "C" {
#endif

union Circle;
union Circle_Class
{
    union Shape_Class Shape;

    struct
    {
    struct Class Class;
    char const * (* _private get_name)(union Circle * const circle);
void (* _private print_info)(union Circle * const circle);
float (* _private get_radius)(union Circle * const circle);

    };
};

union Circle
{
    union Circle_Class * vtbl;
    union Shape Shape;
    struct
    {
      union Object Object;
      char const *  _private name;
float _private radius;

    };
};

extern union Circle_Class * Get_Circle_Class(void);

extern void Circle_populate(union Circle * const circle, char const *  const name, float const radius);

extern char const * Circle_get_name(union Circle * const circle);

extern void Circle_print_info(union Circle * const circle);

extern float Circle_get_radius(union Circle * const circle);

#ifdef __cplusplus
}
#endif
#undef _private
#endif /* CIRCLE_H */
