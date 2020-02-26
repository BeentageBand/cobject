#define CONTAINER_IMPLEMENTATION

#define Container_T TEMPLATE(Container, Container_Params)
#define Container_Class TEMPLATE(Container, Container_Params, Class)
#define Get_Container_Class TEMPLATE(Get, Container, Container_Params, Class)
#define Container_get_shape TEMPLATE(Container, Container_Params, get_shape)
#define container_override TEMPLATE(container, Container_Params, override)
#define container_delete TEMPLATE(container, Container_Params, delete)
#define T T_Param(1, Container_Params)

static void container_override(union Container_Class * const container);
static void container_delete(union Container_T * const container);

union Container_Class * Get_Container_Class(void)
{
  static union Container_Class clazz;
  if (0 != clazz.Class.offset) return &clazz;
  Class_populate(&clazz.Class, sizeof(clazz),
          NULL,
		 (Class_Delete_T)container_delete);
  container_override(&clazz);
  return &clazz;
}

T Container_get_shape(union Container_T * const container)
{
  return container->vtbl->get_shape(container);
}
