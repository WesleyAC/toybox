#define BUFFER_SIZE 255

struct buffer {
  char buf[BUFFER_SIZE];
  int tail;
  int head;
}

int buffer_put(buffer *buffer, char *data, int size) {

}

int buffer_get(buffer *buffer, char *data, int size) {

}
