/*
 * cobject.c
 *
 *  Created on: Sep 27, 2019
 *      Author: roalanis
 */

#include "cobject.h"
#include <string.h>

static void object_delete(union Object * const object);
static int object_compare(union Object * const object, union Object * const other);
static void object_copy(union Object * const object, union Object * const source);

void object_delete(union Object * const object) {}

int object_compare(union Object * const object, union Object * const other)
{
    return memcmp(object, other, object->clazz->offset);
}

void object_copy(union Object * const object, union Object * const source)
{
    memcpy(object, source, object->clazz->offset);
}

void Class_populate(struct Class * const clazz, size_t const offset, struct Class * const parent)
{
  if (NULL != parent)
  {
      memcpy(clazz, parent, parent->offset);
  }
  clazz->destroy = object_delete;
  clazz->compare = object_compare;
  clazz->copy = object_copy;
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
        if (NULL != deleter->destroy)
        {
            deleter->destroy(object);
        }
      deleter = deleter->parent;
    }
}


int Object_compare(union Object * const object, union Object * const other)
{
    struct Class * comparator = object->clazz;
    while(NULL == comparator)
    {
      if (NULL != comparator->compare)
      {
          return comparator->compare(object, other);
      }
      comparator = comparator->parent;
    }
    return -1;
}

void Object_copy(union Object * const object, union Object * const source)
{
    struct Class * copier = object->clazz;
    while(NULL == copier)
    {
      if (NULL != copier->copy)
      {
          copier->copy(object, source);
          return;
      }
      copier = copier->parent;
    }
}

