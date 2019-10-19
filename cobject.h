/*
 * cobject.h
 *
 *  Created on: Sep 27, 2019
 *      Author: roalanis
 */

#ifndef COBJECT_H_
#define COBJECT_H_

#include <stdlib.h>

typedef void (*Class_Delete_T)(struct Object * const);

struct Object
{
  struct Class * clazz;
};

struct Class
{
  size_t offset;
  struct Class * parent;
  Class_Delete_T destroy;
};

extern void Class_populate(struct Class * const clazz, size_t const offset,
			   struct Class * const parent,
			   Class_Delete_T const destroy);

extern void Object_populate(struct Object * const object, struct Class * const clazz);

extern struct Object * Object_cast(struct Object * const object, struct Class * const target_class);

extern void Object_delete(struct Object * const object);

#endif /* COBJECT_H_ */
