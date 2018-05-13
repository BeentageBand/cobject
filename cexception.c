#include <assert.h>
#include "cexception.h"

struct CException_Context * CException_Current_Context = NULL;

void CException_Throw(int exception)
{
   /* no exception context saved, exit program */
   if(! CException_Current_Context ) exit(exception);

   while(CException_Current_Context->ptr)
   {
      CException_Current_Context->ptr->func(CException_Current_Context->ptr->ptr);
      CException_Current_Context->ptr = CException_Current_Context->ptr->next;  
   }

   longjmp(CException_Current_Context->context, exception);
}

struct Protected_Pointer New_Protected_Pointer(struct Protected_Pointer * this, void * ptr, void (* ptr_free)(void *))
{
   if(CException_Current_Context)
   {
      this->next = CException_Current_Context->ptr;
      this->ptr = ptr;
      this->func = ptr_free;
      CException_Current_Context->ptr = ptr;
   }
   return * this;
}
