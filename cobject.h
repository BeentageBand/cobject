#ifndef COBJECT_IMPLEMENTATION
#undef _private 
#define _private const
#else
#undef _private 
#define _private
#endif /*COBJECT_IMPLEMENTATION*/

#ifndef COBJECT_H_
#define COBJECT_H_

#include "xmac.h"
#include "std_reuse.h"

struct Object
{
	struct Class * vtbl;
};

struct Class
{
	void (* destroy)(struct Object * const);
	struct Class * base;
};

extern void Object_Init(struct Object * const object, struct Class * const vtbl, 
		size_t vtbl_size);

extern struct Object * Object_Cast(struct Class const * const cast_class, 
		struct Object * const object);

extern void Object_Delete(struct Object * const object);

#define _delete(_obj) Object_Delete(&(_obj)->Object)

#define _cast(_class, _obj) (CAT(_class,_T) *) Object_Cast(&CAT(_class, _Class).Class, &(_obj)->Object)

#define _using(_class, _obj, _method, ...) CAT(_class, _Class)._method(&(_obj)->_class, \
		__VA__ARGS__)

#endif /*COBJECT_H_*/
