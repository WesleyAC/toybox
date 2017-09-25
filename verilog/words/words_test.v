`include "words.v"

module words_test();

reg clock, reset;
reg [7:0] words;
wire valid;

reg [7:0] test_words [0:15];
integer index;

initial begin
	$display("start");

	test_words[0] = 8'd0;
	test_words[1] = 8'd0;
	test_words[2] = 8'd0;
	test_words[3] = 8'd0;
	test_words[4] = 8'd0;
	test_words[5] = 8'd0;
	test_words[6] = 8'd0;
	test_words[7] = 8'd1; // xx
	test_words[8] = 8'd2;
	test_words[9] = 8'd0;
	test_words[10] = 8'd81; // Qx
	test_words[11] = 8'd1;
	test_words[12] = 8'd0;
	test_words[13] = 8'd81; // QU
	test_words[14] = 8'd85;
	test_words[15] = 8'd0;

	index = 0;

	reset = 1'b1;
	clock = 1'b0;
	#11 reset = 1'b0;
	$display("reset done");
	words = 8'd0;
	#100 $finish;
end

always begin
	#5 clock = ~clock;
	if (reset == 1'b1) begin
		index = 0;
	end else begin
		words = test_words[index];
		index = index + 1;
	end
end

words dut(
	clock,
	reset,
	words,
	valid
);

endmodule
