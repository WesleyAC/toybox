#include <stdio.h>

#define BUFFER_SIZE 255

typedef struct buffer buffer;
struct buffer {
  char *buf;
  int size;
  int tail;
  int head;
};

int buffer_put(buffer buf, char *data, int size) {
  return size;
}

int buffer_get(buffer buf, char *data, int size) {
  return size;
}


int main() {
  char data[BUFFER_SIZE];
  buffer buf = { data, BUFFER_SIZE, 0, 0 };

  char write_data[4] = {42, 13, 7, 21};
  char read_buffer[4];

  buffer_put(buf, write_data, 4);
  buffer_get(buf, read_buffer, 4);

  printf("%d %d %d %d", read_buffer[0], read_buffer[1], read_buffer[2], read_buffer[3]);
}
