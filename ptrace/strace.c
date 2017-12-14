#include <unistd.h>
#include <errno.h>
#include <string.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/ptrace.h>
#include <sys/user.h>

int main(int argc, char **argv) {
  pid_t child = fork();
  if (child == -1) {
    printf("fork() error - %s", strerror(errno));
    exit(1);
  } else if (child == 0) {
    ptrace(PTRACE_TRACEME);
    execvp(argv[1], argv+1);
  } else {
    bool first_stop = true;
    bool syscall_enter = false; // This is a hack
    while (1) {
      int wstatus;
      waitpid(child, &wstatus, __WALL);
      if (WIFEXITED(wstatus)) {
        break;
      } else if (WIFSTOPPED(wstatus)) {
        if (first_stop) { // In practice, this is the execvp call. I don't think that this is documented anywhere.
          printf("Setting ptrace options\n");
          ptrace(PTRACE_SETOPTIONS, child, 0, PTRACE_O_TRACESYSGOOD);
          first_stop = false;
        }

        if (WSTOPSIG(wstatus) == (SIGTRAP|0x80)) {
          if (syscall_enter) {
            struct user_regs_struct regs;
            ptrace(PTRACE_GETREGS, child, 0, &regs);
            printf("Syscall: %d\n", regs.orig_rax);
          }
          syscall_enter = !syscall_enter;
        }

        ptrace(PTRACE_SYSCALL, child, 0, 0);
      } else {
        printf("Something strange has happened...\n");
      }
    }
  }
  return 0;
}
