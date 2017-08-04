module counter(
  clock,
  reset,
  enable,
  counter_out
);

input clock;
input reset;
input enable;

output [3:0] counter_out;

wire clock;
wire reset;
wire enable;

reg [3:0] counter_out;

always @ (posedge clock) begin
  if (reset == 1'b1) begin
    counter_out <= #1 4'b0000;
  end
  else if (enable == 1'b1) begin
    counter_out <= #1 counter_out + 1;
  end
end

endmodule
