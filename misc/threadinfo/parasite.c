#define _GNU_SOURCE
#include <stdio.h>
#include <unistd.h>
#include <sched.h>
#include <stdlib.h>

#define CHILD_STACK_SIZE 16384

int variable;

int do_something() {
   printf("Running...\n");
   variable = 1337;
   _exit(0);
}

int main(int argc, char *argv[]) {
   char *child_stack;
   char *child_stack_top;

   child_stack = malloc(CHILD_STACK_SIZE);
   child_stack_top = child_stack + CHILD_STACK_SIZE;

   variable = 42;
   printf("The variable was %d\n", variable);

   clone(do_something, child_stack_top, CLONE_THREAD, NULL);
   sleep(10);

   printf("The variable is now %d\n", variable);
   return 0;
}
