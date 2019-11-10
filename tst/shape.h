#ifndef SHAPE_H
#define SHAPE_H
#include "cobject.h"

#ifdef __cplusplus
extern "C" {
#endif

union Shape;
union Shape_Class
{
    
    struct
    {
    struct Class Class;
    char const * (* _private get_name)(union Shape * const shape);
void (* _private print_info)(union Shape * const shape);

    };
};

union Shape
{
    union Shape_Class * vtbl;
        struct
    {
      union Object Object;
      char const *  _private name;

    };
};

extern union Shape_Class * Get_Shape_Class(void);

extern void Shape_populate(union Shape * const shape, char const *  const name);

extern char const * Shape_get_name(union Shape * const shape);

extern void Shape_print_info(union Shape * const shape);

#ifdef __cplusplus
}
#endif
#endif /* SHAPE_H */
