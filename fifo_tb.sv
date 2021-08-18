module fifo_tb();
reg clk;
reg enq,deq;
reg[7:0] din,random8;
wire[7:0] dout;
wire full,empty;
reg rst;
integer outfile;
fifo #(.F_DEPTH(4),.F_WIDTH(8),.A_WIDTH(2)) uut(clk,rst,din,dout,enq,deq,full,empty);

initial
begin
clk=0;
forever
#10 clk=~clk;
end

initial
begin
rst=0;
#30 rst=1;
end

always@(posedge clk)
begin
random8=$urandom%128;
enq=random8[2];
deq=random8[3];    //1 bit random number
if (enq)
din=random8;
else
din=8'b0;         //Just for convenience
end

always@(*)
begin
if(full & empty)
$display("full empty at same time %0t",$time);
end

initial begin
    outfile=$fopen("fifo_git.txt","w");
    #10;
    forever begin
    $fdisplay(outfile,"%d %d %d %d %d %d ",enq,deq,din,dout,full,empty);
    #20;
    end
end    


endmodule


