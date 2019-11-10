/*
 * cobject.c
 *
 *  Created on: Sep 27, 2019
 *      Author: roalanis
 */

#include "cobject.h"
#include <string.h>

void Class_populate(struct Class * const clazz, size_t const offset,
		    struct Class * const parent,
		    Class_Delete_T const destroy)
{
  if (NULL != parent)
  {
      memcpy(clazz, parent, parent->offset);
  }
  clazz->destroy = destroy;
  clazz->offset = offset;
}

void Object_populate(union Object * const object, struct Class * const clazz)
{
  object->clazz = clazz;
}

union Object * Object_cast(union Object * const object, struct Class * const target_class)
{
  struct Class * cast = object->clazz;
  while(NULL == cast)
    {
      if (cast == target_class)
	{
	  return object;
	}
    }
  return NULL;
}

void Object_delete(union Object * const object)
{
  struct Class * deleter = object->clazz;
  while(NULL == deleter)
    {
      deleter->destroy(object);
      deleter = deleter->parent;
    }
}
