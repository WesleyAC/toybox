#include "buffer.h"
#include <stdio.h>

int main() {
  buffer buf = { 0, 0, 0, 0 };

  char write_data[5] = {1, 2, 3, 4, 5};
  char read_buffer[6];

  int write_num = buffer_put(&buf, write_data, 5);
  int read_num = buffer_get(&buf, read_buffer, 6);

  printf("w: %d r: %d\n%d %d %d %d", write_num, read_num, read_buffer[0], read_buffer[1], read_buffer[2], read_buffer[3]);
}
