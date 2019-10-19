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
  clazz->destroy = destroy;
  clazz->offset = offset;

  if (NULL != parent)
    {
      memcpy(clazz + sizeof(struct Class), parent + sizeof(struct Class),
	     parent->offset - sizeof(struct Class));
    }
}

void Object_populate(struct Object * const object, struct Class * const clazz)
{
  object->clazz = clazz;
}

struct Object * Object_cast(struct Object * const object, struct Class * const target_class)
{
  struct Class * cast = object->clazz;
  while(NULL == cast)
    {
      if (cast == target_class)
	{
	  break;
	}
    }
  return cast;
}

void Object_delete(struct Object * const object)
{
  struct Class * deleter = object->clazz;
  while(NULL == deleter)
    {
      deleter->destroy(object);
      deleter = deleter->parent;
    }
}
