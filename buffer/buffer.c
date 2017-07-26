#include <stdio.h>
#include <string.h>
#include <sys/param.h> // Provides min/max on most linux/bsd machines

#define BUFFER_SIZE 256
typedef struct buffer buffer;
struct buffer {
  char buf[BUFFER_SIZE];
  unsigned char tail;
  unsigned char head;
  unsigned char num_items;
};

int buffer_put(buffer *const buf, const char *const data, int size) {
  size = MIN(BUFFER_SIZE - buf->num_items, size);
  int end = (buf->head < buf->tail) ? buf->tail : BUFFER_SIZE;
  int first_write_size = MIN(end - buf->head, size);
  memcpy(buf->buf + buf->head, data, first_write_size);
  memcpy(buf->buf + buf->head + first_write_size, data + first_write_size, size - first_write_size);
  buf->head = (buf->head + size) % BUFFER_SIZE;
  buf->num_items += size;
  return size;
}

int buffer_get(buffer *const buf, char *const data, int size) {
  size = MIN(buf->num_items, size);
  int end = (buf->head < buf->tail) ? BUFFER_SIZE : buf->head;
  int first_read_size = MIN(end - buf->tail, size);
  memcpy(data, buf->buf + buf->tail, first_read_size);
  memcpy(data + first_read_size, buf->buf + buf->tail + first_read_size, size - first_read_size);
  buf->tail = (buf->tail + size) % BUFFER_SIZE;
  buf->num_items -= size;
  return size;
}


int main() {
  buffer buf = { 0, 0, 0, 0 };

  char write_data[5] = {1, 2, 3, 4, 5};
  char read_buffer[6];

  int write_num = buffer_put(&buf, write_data, 5);
  int read_num = buffer_get(&buf, read_buffer, 6);

  printf("w: %d r: %d\n%d %d %d %d", write_num, read_num, read_buffer[0], read_buffer[1], read_buffer[2], read_buffer[3]);
}
