/*
 * cobject.h
 *
 *  Created on: Sep 27, 2019
 *      Author: roalanis
 */

#ifndef COBJECT_H_
#define COBJECT_H_

#include <stdlib.h>

#ifndef COBJECT_IMPLEMENTATION
#define _private const
#else 
#define _private
#endif


union Object;

typedef void (*Class_Delete_T)(union Object * const);

struct Class
{
  size_t offset;
  struct Class * parent;
  Class_Delete_T destroy;
};

union Object
{
  struct Class * clazz;
};

extern void Class_populate(struct Class * const clazz, size_t const offset,
			   struct Class * const parent,
			   Class_Delete_T const destroy);

extern void Object_populate(union Object * const object, struct Class * const clazz);

extern union Object * Object_cast(union Object * const object, struct Class * const target_class);

extern void Object_delete(union Object * const object);

#define _cast(obj, clazz) (union Clazz *) Object_cast(&obj.Object, Get_##clazz##_Class())
#define _static_cast(obj, clazz) obj.clazz
#define _using(obj, clazz, method) Get_##clazz_Class()->method
#define _delete(obj) Object_delete(&obj.Object)

#endif /* COBJECT_H_ */
