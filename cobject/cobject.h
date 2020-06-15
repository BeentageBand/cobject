/*
 * cobject.h
 *
 *  Created on: Sep 27, 2019
 *      Author: roalanis
 */

#ifndef COBJECT_H_
#define COBJECT_H_

#include <stdlib.h>

#ifdef __cplusplus
extern "C" {
#endif

union Object;

typedef int (*Class_Compare_T)(union Object const * const, union Object const * const);
typedef void (*Class_Copy_T)(union Object * const, union Object const * const);
typedef void (*Class_Delete_T)(union Object * const);

struct Class
{
  size_t offset;
  struct Class * parent;
  Class_Delete_T destroy;
  Class_Compare_T compare;
  Class_Copy_T copy;
};

union Object
{
  struct Class * clazz;
};

extern void Class_populate(struct Class * const clazz, size_t const offset, struct Class * const parent);

extern void Object_populate(union Object * const object, struct Class * const clazz);

extern union Object * Object_cast(union Object * const object, struct Class * const target_class);

extern void Object_delete(union Object * const object);

extern int Object_compare(union Object const * const object, union Object const * const other);

extern void Object_copy(union Object * const object, union Object const * const source);

#ifdef __cplusplus
}
#endif

#define _cast(obj, clazz) (union Clazz *) Object_cast(&(obj)->.Object, &Get_##clazz##_Class()->Class)
#define _using(clazz, method, ...) Get_##clazz##_Class()->method(__VA_ARGS__)
#define _delete(obj) Object_delete(&(obj)->Object)
#define _new(clazz) (clazz *) malloc(sizeof(clazz))
#define _equals(lval, rval) (0 == Object_compare(&(lval)->Object, &(rval)->Object))
#define _compare(lval, rval) Object_compare(&(lval)->Object, &(rval)->Object)
#define _copy(lval, rval) Object_copy(&(lval)->Object, &(rval)->Object)

#endif /* COBJECT_H_ */
