#ifndef CEXCEPTION_H_
#define CEXCEPTION_H_

#include <setjump.h>
#include "std_reuse.h"
#include "xmac.h"

#ifndef __STDC__
#error "cexception.h needs ISO C compiler"
#endif 

#define _try                                                                        \
do                                                                                  \
{                                                                                   \
struct CException_Context * const cexception_return_context_0 =                     \
   CException_Return_Context;                                                      \
struct CException_Context * const volatile CException_Return_Context =              \
   cexception_return_context_0? cexception_return_context_0 :                      \
   CException_Current_Context;                                                     \
struct CException_Context cexception_local_context = { CException_Current_Context };\
                                                                                    \
CException_Current_Context = &cexception_local_context;                             \
                                                                                    \
(void)CException_Return_Context;                                                    \
                                                                                    \
do                                                                                  \
{                                                                                   \
   int const exception = set_jump(CException_Current_Context->context);            \
   if(0 < exception)                                                               \
   {                                                                               \

   
#define _catch(except)                                                \
   }                                                                 \
   else if ((int)(except) == exception)                              \
   {                                                                 \
      CException_Current_Context = CException_Current_Context->next;\

#define _any                                                          \
   }                                                                 \
   else                                                              \
   {                                                                 \
      CException_Current_Context = CException_Current_Context->next;\

#define _end_try                                                   \
   }                                                              \
}while(false);                                                     \
if(CException_Current_Context == &cexception_local_context)        \
{                                                                  \
   CException_Current_Context = CException_Current_Context->next; \
}                                                                  \
}while (false);                                                    \

#define _rethrow _throw(exception)

#define _break_try break

#define return_try(...)                                    \
do{                                                        \
   CException_Current_Context = CException_Return_Context;\
   return __VA_ARGS__;                                    \
}while(false);                                             \

#ifdef DEBUG_THROW
#define _throw(except) \
Dbg_Fault("Exception thrown = %s - %d",  STR(except), (int)(except)) \

#else
#define _throw(except) CException_Throw((int)(except));

#endif /*DEBUG_THROW*/

/* Pointer Protection */

#define _protect_ptr(ptr, func)                                                    \
struct Protected_Ptr CAT(_protected, ptr) = CPointer_Protect(&CAT(_protected, ptr),\
      (void (*)(void *))(func))                                                  \

#ifdef __cplusplus
extern "C" {
#endif

struct Protected_Ptr
{
   struct Protected_Ptr * next;
   void * ptr;
   void (* func)(void *);
};

struct CException_Context
{
   struct CException_Context * next;
   struct Protected_Ptr  * stack;
   jmp_buf context;

};

extern struct CException_Context * const CException_Return_Context;
extern struct CException_Context * CException_Current_Context;

static inline struct Protected_Ptr CPointer_Protect(struct Protected_Ptr * const p_ptr,
      void * ptr, void (* func)(void *))
{
   if(CException_Current_Context)
   {
      p_ptr->next = CException_Current_Context->stack;
      p_ptr->ptr = ptr;
      p_ptr->func = func;
      CException_Current_Context->stack = p_ptr;
   }
   return * p_ptr;
}

static inline void CPointer_Unprotect(void * ptr)
{
   if(CException_Current_Context && 
      CException_Current_Context->stack &&
      CException_Current_Context->stack->ptr == ptr)
   {
      CException_Current_Context->stack = CException_Current_Context->stack->next;
   }
}

extern void CException_Throw(int except);


#ifdef __cplusplus
}
#endif

#endif /*CEXCEPTION_H_*/
