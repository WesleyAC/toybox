#include "buffer.h"

#include <string.h>
#include <sys/param.h> // Provides min/max on most linux/bsd machines

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
