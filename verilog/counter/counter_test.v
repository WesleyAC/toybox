`include "counter.v"

module counter_test();

reg clock, reset, enable;
wire [3:0] counter_out;

initial begin
  $display("time\tclk\treset\tenable\tcounter");
  $monitor("%g\t%b\t%b\t%b\t%b",
  $time, clock, reset, enable, counter_out);

  clock = 1;
  reset = 0;
  enable = 0;
  #5 reset = 1;
  #10 reset = 0;
  #5 enable = 1;
  #100 enable = 0;
  #10 $finish;
end

always begin
  #5 clock = ~clock;
end

counter U_counter(
  clock,
  reset,
  enable,
  counter_out
);

endmodule
