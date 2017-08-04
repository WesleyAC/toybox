`include "alu.v"

module alu_test();

reg [0:15] a;
reg [0:15] b;
reg [0:2] opcode;
wire [0:15] out;

initial begin
  $display("ALU logical operations test");
  $monitor("%b\t%g\t%g\t%g", opcode, a, b, out);

  a = 64;
  b = 32;

  // ADD
  opcode = 3'b000;
  #1

  // SUB
  opcode = 3'b001;
  #1

  // INC
  b = 0;
  opcode = 3'b010;
  #1

  // DEC
  opcode = 3'b011;
  #1

  $display("ALU bitwise operations test");
  $monitor("%b\t%b\n\t%b\n\t%b\n", opcode, a, b, out);
  // AND
  a = 16'b0000001111111111;
  b = 16'b1111111111000000;
  opcode = 3'b100;
  #1

  // OR
  a = 16'b0000000000111111;
  b = 16'b1111110000000000;
  opcode = 3'b101;
  #1

  // XOR
  a = 16'b0001110000111111;
  b = 16'b1111110000111000;
  opcode = 3'b110;
  #1

  // NOT
  a = 16'b0001111110000111;
  b = 16'b0000000000000000;
  opcode = 3'b111;

  $finish;
end

alu U_alu(
  a,
  b,
  opcode,
  out
);

endmodule
