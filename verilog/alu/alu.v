module alu(
  a,
  b,
  opcode,
  out
);

input clock;
input [0:15] a;
input [0:15] b;
input [0:2] opcode;

output [0:15] out;

wire [0:15] a;
wire [0:15] b;
wire [0:2] opcode;
reg [0:15] out;

always @* begin
  case (opcode)
    3'b000: out <= a + b; // ADD
    3'b001: out <= a - b; // SUB
    3'b010: out <= a + 1; // INC
    3'b011: out <= a - 1; // DEC
    3'b100: out <= a & b; // AND
    3'b101: out <= a | b; // OR
    3'b110: out <= a ^ b; // XOR
    3'b111: out <= ~a;    // NOT
  endcase
end

endmodule
