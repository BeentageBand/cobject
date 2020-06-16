#ifndef RECTANGLE_H
#define RECTANGLE_H
#include "shape.h"

#ifdef RECTANGLE_IMPLEMENTATION 
#define _private
#else RECTANGLE_IMPLEMENTATION 
#define _private const
#endif 

#ifdef __cplusplus
extern "C" {
#endif

union Rectangle;
union Rectangle_Class
{
    union Shape_Class Shape;

    struct
    {
    struct Class Class;
    char const * (* _private get_name)(union Rectangle * const rectangle);
void (* _private print_info)(union Rectangle * const rectangle);
float (* _private get_height)(union Rectangle * const rectangle);
float (* _private get_width)(union Rectangle * const rectangle);

    };
};

union Rectangle
{
    union Rectangle_Class * vtbl;
    union Shape Shape;
    struct
    {
      union Object Object;
      char const *  _private name;
float _private height;
float _private width;

    };
};

extern union Rectangle_Class * Get_Rectangle_Class(void);

extern void Rectangle_populate(union Rectangle * const rectangle, char const *  const name, float const height, float const width);

extern char const * Rectangle_get_name(union Rectangle * const rectangle);

extern void Rectangle_print_info(union Rectangle * const rectangle);

extern float Rectangle_get_height(union Rectangle * const rectangle);

extern float Rectangle_get_width(union Rectangle * const rectangle);

#ifdef __cplusplus
}
#endif
#endif /* RECTANGLE_H */