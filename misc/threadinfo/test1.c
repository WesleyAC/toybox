#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>

void *print_thread_info();

// Fuck error handling :/

main() {
     pthread_t thread1, thread2;

     pthread_create( &thread1, NULL, print_thread_info, NULL);
     pthread_create( &thread2, NULL, print_thread_info, NULL);

     pthread_join(thread1, NULL);
     pthread_join(thread2, NULL);

     exit(EXIT_SUCCESS);
}

void *print_thread_info() {
     int fd;
     fd = open("/proc/self/status", O_RDONLY);
     char *buf[1024];
     int n;
     while (n=read(fd, buf, 1024)) {
	write(1, buf, n);
     }
}
