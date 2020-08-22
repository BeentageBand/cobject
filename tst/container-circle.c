#define CONTAINER_T_IMPLEMENTATION
#include "container-circle.h"

typedef union Circle Circle;
#define Container_Params Circle
#include "container-int-template.h"
#undef Container_Params
