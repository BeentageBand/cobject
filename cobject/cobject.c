/*
 * cobject.c
 *
 *  Created on: Sep 27, 2019
 *      Author: roalanis
 */

#include "cobject.h"
#include <stdio.h>
#include <string.h>

static int object_compare(union Object const *const object,
                          union Object const *const other);
static void object_copy(union Object *const object,
                        union Object const *const source);
static void object_delete(union Object *const object);

int object_compare(union Object const *const object,
                   union Object const *const other) {
  return memcmp(object, other, object->clazz->offset);
}

void object_copy(union Object *const object, union Object const *const source) {
  memcpy(object, source, source->clazz->offset);
}

void object_delete(union Object *const object) {}

void Class_populate(struct Class *const clazz, size_t const offset,
                    struct Class *const parent) {
  if (NULL != parent) {
    memcpy(clazz, parent, parent->offset);
  }
  clazz->destroy = object_delete;
  clazz->compare = object_compare;
  clazz->copy = object_copy;
  clazz->offset = offset;
}

void Object_populate(union Object *const object, struct Class *const clazz) {
  object->clazz = clazz;
}

union Object *Object_cast(union Object *const object,
                          struct Class *const target_class) {
  struct Class *cast = object->clazz;
  while (NULL == cast) {
    if (cast == target_class) {
      return object;
    }
  }
  return NULL;
}

void Object_delete(union Object *const object) {
  struct Class *deleter = object->clazz;
  while (NULL != deleter) {
    deleter->destroy(object);
    deleter = deleter->parent;
  }
}

int Object_compare(union Object const *const object,
                   union Object const *const other) {
  if (object == other)
    return 0;
  if (object->clazz != other->clazz)
    return -1;

  struct Class *comparator = other->clazz;
  while (NULL != comparator) {
    comparator->compare(object, other);
    comparator = comparator->parent;
  }
}

void Object_copy(union Object *const object, union Object const *const source) {
  if (object == source)
    return;

  struct Class *copier = source->clazz;
  while (NULL != copier) {
    if (NULL != copier->copy)

    {
      copier->copy(object, source);
      return;
    }
    copier = copier->parent;
  }
}
