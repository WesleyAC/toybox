#include <stdio.h>
#include <string.h>

#define BUFFER_SIZE 255

typedef struct buffer buffer;
struct buffer {
  char *buf;
  int size;
  int tail;
  int head;
};

int buffer_free_space(buffer buf) {
  if (buf.head > buf.tail) {
    return (buf.size-1) - (buf.head - buf.tail);
  } else {
    return (buf.size+1) - (buf.tail - buf.head);
  }
}

int buffer_put(buffer buf, char *data, int size) {
  int free_space = buffer_free_space(buf);
  if (size > free_space) {
    size = free_space;
  }
  int end = (buf.head < buf.tail) ? buf.tail : buf.size;
  int first_write_size = end - buf.head;
  if (first_write_size > size) {
    first_write_size = size;
  }
  memcpy(buf.buf + buf.head, data, first_write_size);
  memcpy(buf.buf, data + first_write_size, size - first_write_size);
  return size;
}

int buffer_get(buffer buf, char *data, int size) {
  memcpy(data, buf.buf, size);
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
