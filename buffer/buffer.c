#include <stdio.h>
#include <string.h>
#include <sys/param.h> // Provides min/max on most linux/bsd machines

#define BUFFER_SIZE 256
typedef struct buffer buffer;
struct buffer {
  char buf[BUFFER_SIZE];
  char tail;
  char head;
};

int buffer_free_space(const buffer *const buf) {
  if (buf->head > buf->tail) {
    return (BUFFER_SIZE-1) - (buf->head - buf->tail);
  } else if (buf->head < buf->tail) {
    return (BUFFER_SIZE+1) - (buf->tail - buf->head);
  } else {
    return BUFFER_SIZE;
  }
}

int buffer_used_space(const buffer *const buf) {
  return BUFFER_SIZE - buffer_free_space(buf);
}

int buffer_put(buffer *const buf, const char *const data, int size) {
  size = MIN(buffer_free_space(buf), size);
  int end = (buf->head < buf->tail) ? buf->tail : BUFFER_SIZE;
  int first_write_size = MIN(end - buf->head, size);
  memcpy(buf->buf + buf->head, data, first_write_size);
  memcpy(buf->buf + buf->head + first_write_size, data + first_write_size, size - first_write_size);
  buf->head = (buf->head + size) % BUFFER_SIZE;
  return size;
}

int buffer_get(buffer *const buf, char *const data, int size) {
  size = MIN(buffer_used_space(buf), size);
  int end = (buf->head < buf->tail) ? BUFFER_SIZE : buf->head;
  int first_read_size = MIN(end - buf->tail, size);
  memcpy(data, buf->buf + buf->tail, first_read_size);
  memcpy(data + first_read_size, buf->buf + buf->tail + first_read_size, size - first_read_size);
  buf->tail = (buf->tail + size) % BUFFER_SIZE;
  return size;
}


int main() {
  buffer buf = { 0, 0, 0 };

  char write_data[9] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'};
  char read_buffer[20];

  buffer_put(&buf, write_data, 9);
  buffer_get(&buf, read_buffer, 20);

  printf("%d %d %d %d", read_buffer[0], read_buffer[1], read_buffer[2], read_buffer[3]);
}
