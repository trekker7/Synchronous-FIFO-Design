class fifo:
    def __init__(self):
        self.size=4
        self.q=[0]*self.size
        self.addr_width=3;
        self.wr_pointer=0
        self.rd_pointer=0
        
    def io_port(self,enq,deq,din=0):
        ret_val=self.q[self.rd_pointer%self.size]
        rdp=self.rd_pointer
        rwp=self.wr_pointer
        full=1 if self.full() else 0
        empty=1 if self.empty() else 0
        if enq and full==0:
            self.enq(din)
        if deq and empty==0:
            self.deq()
        return [ret_val, full, empty]  
    
    def enq(self,din):
        self.q[self.wr_pointer%self.size]=din;
        self.update_wr_pointer()
    def deq(self):
        self.update_rd_pointer()
        #return ret_val;
    def empty(self):
        if self.wr_pointer==self.rd_pointer:
            return True
        else:
            return False
    def full(self):
        if abs(self.wr_pointer-self.rd_pointer)==2**(self.addr_width-1):
            return True
        else:
            return False
    def update_rd_pointer(self):
        if self.rd_pointer==2**(self.addr_width)-1:
            self.rd_pointer=0
        else:
            self.rd_pointer=self.rd_pointer+1
    def update_wr_pointer(self):
        if self.wr_pointer==2**(self.addr_width)-1: 
            self.wr_pointer=0
        else:
            self.wr_pointer=self.wr_pointer+1
    def status(self):
        print('q is',self.q)
        #print("rd_pointer",format(self.rd_pointer, '03b'),"wr_pointer",format(self.wr_pointer, '03b'))
        #print("empty",self.empty(),"full",self.full())

        


# In[10]:


import random
from random import randint
z=fifo()
seq=open("fifo_git.txt")
i=0
#enq,deq,din,dout,full,empty,read_pointer,write_pointer column in .txt file
ok=True
while True:
    a=seq.readline()
    if a=="":
        break
    a=a.split()
    out_model=z.io_port(int(a[0]),int(a[1]),int(a[2])) #enq,deq,din
    #out_model=[dout, full, empty,read pointer,write pointer] from reference model
    out_sim=[int(a[3]),int(a[4]),int(a[5])] 
    #dout,full,empty,read_pointer,write_pointer from RTL model
    
    if out_sim!=out_model:
        print('At iter ',i, "stimuli  " ,end="")
        print('enq,deq,din',int(a[0]),int(a[1]),int(a[2]))
        print('dout,full,empty from simulator and model are',out_sim,out_model)
        ok=False
    #z.status()
    i=i+1
seq.close()

if ok:
    print("passed pseudorandom test")
else:
    print("failed for at least one case")






