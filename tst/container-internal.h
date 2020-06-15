#if !defined(CONTAINER_INT_H) || defined(Container_Params)
#define CONTAINER_INT_H

static void container_t_override(union Container_T_Class * const container);

union Container_T_Class * Get_Container_T_Class(void)
{
  static union Container_T_Class clazz;
  if (0 != clazz.Class.offset) return &clazz;
  Class_populate(&clazz.Class, sizeof(clazz), NULL);
  container_t_override(&clazz);
  return &clazz;
}

T Container_T_get_shape(union Container_T * const container)
{
  return container->vtbl->get_shape(container);
}

#endif /* !define(CONTAINER_INT_H) || defined(Container_T_Params) */
