#ifndef COBJECT_IMPLEMENTATION
#undef _private 
#define _private const
#else
#undef _private 
#define _private const
#endif /*COBJECT_IMPLEMENTATION*/

#ifndef COBJECT_H_
#define COBJECT_H_

#include "xmac.h"

struct Object
{
	struct Class * vtbl;
};

struct Class
{
	struct Class * base;
	void (* destroy)(struct Object * const);
};

extern void Object_Init(struct Object * const object, struct Class * vtbl, size_t const vtbl_size);

extern struct Object * Object_Cast(struct Class const * const cast_vtbl, struct Object * const object);

#define _cast(_class, _object) (CAT(_class, _Class_T) *) Object_Cast(&CAT(_class, _Class).Class, &(_object)->Object)

#define _delete(_object)  ( (_object)->Object.vtbl->destroy(&(_object)->Object) )

#endif /*COBJECT_H_*/

