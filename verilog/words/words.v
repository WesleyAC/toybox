module words(
	clock,
	reset,
	words_in,
	words_out
);

input clock;
input reset;
input [7:0] words_in;

output words_out;
wire words_out;

reg seen_q;
reg seen_u;

assign words_out = seen_q & ~seen_u;

always @ (posedge clock) begin
	if (reset == 1'b1) begin
		$display("reset");
		seen_q <= 1'b0;
		seen_u <= 1'b0;
	end else begin
		$display("w %d %d %b %b", words_in, words_out, seen_q, seen_u);
		if (words_in == 8'd0) begin
			$display(words_out);
			seen_q <= 1'b0;
			seen_u <= 1'b0;
		end else if (words_in == 8'd81) begin // Q
			seen_q <= 1'b1;
		end else if (words_in == 8'd85) begin // U
			seen_u <= 1'b1;
		end
	end
end

endmodule
