#ifndef WESLEYAC_TOYBOX_BUFFER_H_
#define WESLEYAC_TOYBOX_BUFFER_H_

#define BUFFER_SIZE 256

struct buffer;
typedef struct buffer {
  char buf[BUFFER_SIZE];
  unsigned char tail;
  unsigned char head;
  unsigned char num_items;
} buffer;

int buffer_put(buffer *const buf, const char *const data, int size);
int buffer_get(buffer *const buf, char *const data, int size);

#endif
