#include <stdio.h>
#include <string.h>
#include <sys/param.h> // Provides min/max on most linux/bsd machines

#define BUFFER_SIZE 255

typedef struct buffer buffer;
struct buffer {
  char *buf;
  int size;
  int tail;
  int head;
};

int buffer_free_space(buffer *buf) {
  if (buf->head > buf->tail) {
    return (buf->size-1) - (buf->head - buf->tail);
  } else if (buf->head < buf->tail) {
    return (buf->size+1) - (buf->tail - buf->head);
  } else {
    return buf->size;
  }
}

int buffer_used_space(buffer *buf) {
  return buf->size - buffer_free_space(buf);
}

int buffer_put(buffer *buf, char *data, int size) {
  size = MIN(buffer_free_space(buf), size);
  int end = (buf->head < buf->tail) ? buf->tail : buf->size;
  int first_write_size = MIN(end - buf->head, size);
  memcpy(buf->buf + buf->head, data, first_write_size);
  memcpy(buf->buf, data + first_write_size, size - first_write_size);
  buf->head = (buf->head + size) % buf->size;
  return size;
}

int buffer_get(buffer *buf, char *data, int size) {
  size = MIN(buffer_used_space(buf), size);
  int end = (buf->head < buf->tail) ? buf->size : buf->head;
  int first_read_size = MIN(end - buf->tail, size);
  memcpy(data, buf->buf + buf->tail, first_read_size);
  memcpy(data, buf->buf + buf->tail + first_read_size, size - first_read_size);
  buf->tail = (buf->tail + size) % buf->size;
  return size;
}


int main() {
  char data[BUFFER_SIZE];
  buffer buf = { data, BUFFER_SIZE, 0, 0 };

  char write_data[4] = {42, 13, 7, 21};
  char read_buffer[4];

  buffer_put(&buf, write_data, 4);
  buffer_get(&buf, read_buffer, 4);

  printf("%d %d %d %d", read_buffer[0], read_buffer[1], read_buffer[2], read_buffer[3]);
}
