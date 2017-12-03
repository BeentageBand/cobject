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
#include "std_reuse.h"

struct Object
{
	struct Class * vtbl;
};

struct Class
{
	struct Class * base;
	void (* destroy)(struct Object * const);
};

extern void Object_Init(struct Object * const object, struct Class * const vtbl, 
		size_t vtbl_size);

extern struct Object * Object_Cast(struct Class const * const cast_class, 
		struct Object * const object);

#define _cast(_class, _object) \
	(CAT(_class, _T) *) Object_Cast(&CAT(_class, _Class).Class, \
			&(_object)->Object)

#define _delete(_object) (_object)->Object.vtbl->destroy((struct Object *)(_object))

#define _using(_class, _object, _method, ...) 
		
#endif /*COBJECT_H_*/
