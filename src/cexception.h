#ifndef CEXCEPTION_H_
#define CEXCEPTION_H_

#include <setjmp.h>

#include "xmac.h"

#ifndef __STDC__
#error "cexception.h needs ISO C compiler"
#endif 


/** _try
 *  try block from try-catch structure
 *  logic flows until exception is thrown
 */
#define _try \
char const * exception_message = NULL; \
struct CException local_context; \
local_context.next = CException_Current; \
CException_Current = &local_context; \
int const exception = setjmp(CException_Current->context); \
if(0 == exception)

/** _catch
 * Starts catch block
 */
#define _catch \
else { \
    switch (exception) { \
      default:

/** _any
 * goes first after _catch
 * catches any exception not defined with _exception
 */
#define _any CException_Current = CException_Current->next;

/** _exception
 * catches specific exception
 */
#define _exception(e) \
    break; case e: _any

/** _finally
 * goes at the end of _any/_exception
 * logic is executed even an exception was thrown
 */
#define _finally \
    break; } /* ends switch */

/** _end_try
 * goes at the very end of the try-catch block
 */
#define _end_try \
} /* ends if */ \
  if (&local_context == CException_Current) { \
      _any \
      CException_throw(exception, exception_message); \
  } \

#ifdef DEBUG_THROW
#define _throw(except) \
Dbg_Fault("Exception thrown = %s - %d",  STR(except), (int)(except)) \

#else
#define _throw(e, message) \
  exception_message = message; \
  CException_throw((int)(e), exception_message);

#endif /*DEBUG_THROW*/


#ifdef __cplusplus
extern "C" {
#endif

struct CException
{
   struct CException * next;
   char const * msg;
   jmp_buf context;
};

extern struct CException * CException_Current;

extern void CException_throw(int const except, char const * const message);


#ifdef __cplusplus
}
#endif

#endif /*CEXCEPTION_H_*/
