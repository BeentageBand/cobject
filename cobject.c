#define COBJECT_IMPLEMENTATION
#include "cobject.h"

void Object_Init(struct Object * const object, struct Class * vtbl, size_t const vtbl_size)
{
	if(NULL != object->vtbl)
	{
		memcpy(vtbl + 1U, object->vtbl + 1, vtbl_size - sizeof(struct Class));
	}

	object->vtbl = vtbl;
}

struct Object * Object_Cast(struct Class const * const cast_vtbl, struct Object * const object)
{
	struct Object * casted_obj = NULL;
	struct Class const * cast_class = object->vtbl;

	while(NULL != cast_class)
	{
		if(cast_vtbl == cast_class)
		{
			casted_obj = object;
			break;
		}

		cast_class = cast_class->base;
	}
	return casted_obj;
}

void Object_Delete(struct Object * const object)
{
	Isnt_Nullptr(object, );

	if(NULL != object->vtbl)
	{
		object->vtbl->destroy(object);
	}
}
