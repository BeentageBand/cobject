#include "cexception.h"
#include <stdlib.h>

#include <assert.h>

struct CException * CException_Current = NULL;

void CException_throw(int exception, char const * const message)
{
   /* no exception context saved, exit program */
   if(! CException_Current ) exit(exception);

   CException_Current->msg = message;
   longjmp(CException_Current->context, exception);
}
