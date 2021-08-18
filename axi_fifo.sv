module fifo(clk,rst,din,dout,enq,deq,full,empty);
parameter F_DEPTH=4,
	  F_WIDTH=8,
          A_WIDTH=$clog2(F_DEPTH);
input clk,rst,enq,deq;
input [F_WIDTH-1:0] din;
output [F_WIDTH-1:0] dout;
output empty,full;
reg [A_WIDTH:0] r_addr,w_addr;
reg [A_WIDTH-1:0] count;
reg [F_WIDTH-1:0] mem[F_DEPTH-1:0];

always@(posedge clk)
begin


if(rst==0) begin
	r_addr<=0;
	w_addr<=0;
	end
else begin 
	if(enq & !full) 
		w_addr<=w_addr+1'b1;

	if(deq & !empty)
		r_addr<=r_addr+1'b1;
	
end


end


always@(posedge clk)
begin
if(enq & !full)
mem[w_addr[A_WIDTH-1:0]]<=din;

end

assign empty=r_addr==w_addr? 1'b1:1'b0;
assign full= r_addr[A_WIDTH]==w_addr[A_WIDTH] ? 1'b0 : (r_addr[A_WIDTH-1:0]==w_addr[A_WIDTH-1:0] ? 1'b1:1'b0);
assign dout=mem[r_addr[A_WIDTH-1:0]];
endmodule


