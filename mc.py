
from urllib.request import urlopen, Request
from urllib.parse import urlencode, quote

FAIL="{\"errorCode\" : 8, \"mesage\" : \"invalid mc.py\"}"

class MC:
    def __init__(self):
        # put True here to see some logging
        self.debug = False
        # this is here so we can verify the directions
        self.directions = ["forward","left","right","back","up","down"]
    def _get(self,path):
        if self.debug:
            print("_get called with",path)
        # Code Connection listens on port 8080 localhost
        u = urlopen("http://localhost:8080/" +  path)
        data = u.read()
        u.close()
        return data

    # commands for agent
    def move(self,direction):
        if direction not in self.directions:
            return FAIL
        return self._get("move?direction="+direction)
    def turn(self,direction):
        if direction not in self.directions:
            return FAIL
        return self._get("turn?direction="+direction)
    def place(self,slotnum,direction):
        if direction not in self.directions:
            return FAIL
        if slotnum <1 or slotnum>27:
            return FAIL
        return self._get("place?slotNum="+str(slotnum) + "&direction="+direction)
    def till(self,direction):
        if direction not in self.directions:
            return FAIL
        return self._get("till?direction="+direction)
    def attack(self,direction):
        if direction not in self.directions:
            return FAIL
        return self._get("attack?direction="+direction)
    def destroy(self,direction):
        if direction not in self.directions:
            return FAIL
        return self._get("destroy?direction="+direction)
    def collect(self,item):
        return self._get("collect?item="+str(item))
    def drop(self,slotnum,quantity,direction):
        if slotnum<1 or slotnum>27:
            return FAIL
        if quantity<1 or quantity>64:
            return FAIL
        return self._get("drop?slotNum="+str(slotnum)+"&quantity="+str(quantity)+"&direction="+direction)
    def dropall(self,direction):
        if direction not in self.directions:
            return FAIL
        return self._get("dropall?direction="+direction)
    def detect(self,direction):
        if direction not in self.directions:
            return FAIL
        return self._get("detect?direction="+direction)
    def inspect(self,direction):
        if direction not in self.directions:
            return FAIL
        return self._get("inspect?direction=" + direction)
    def inspectdata(self,direction):
        if direction not in self.directions:
            return FAIL
        return self._get("inspectdata?direction=" + direction)
    def detectredstone(self,direction):
        if direction not in self.directions:
            return FAIL
        return self._get("detectredstone?direction=" + direction)
    def getitemdetail(self,slotnum):
        return self._get("getitemdetail?slotNum="+str(slotnum))
    def getitemspace(self,slotnum):
        return self._get("getitemspace?slotNum="+str(slotnum))
    def getitemcount(self,slotnum):
        return self._get("getitemcount?slotNum="+str(slotnum))
    def transfer(self,src_slotnum,quantity,dst_slotnum):
        return self._get("transfer?srcSlotNum="+str(src_slotnum) + "&quantity=" + str(quantity) + "&dstSlotNum=" + str(dst_slotnum))
    def tptoplayer(self):
        return self._get("tptoplayer")
    
    def create_block_pos(self,x,y,z,is_relative):
        if is_relative:
            prefix ="~"
        else:
            prefix = ""
        res = "{0}{1}%20{0}{2}%20{0}{3}".format(prefix,x,y,z)
        return res

    # world commands
    def clone(self, blockpos_begin, blockpos_end,blockpos_dest):
        pass
    def fill(self, fromX,fromY,fromZ,fromRel,toX,toY,toZ,toRel,tilename):
        x = self.create_block_pos(fromX,fromY,fromZ,True)
        y = self.create_block_pos(toX,toY,toZ,True)
        cmd="fill?from=" + x +"&to=" + y + "&tileName=" + tilename
        return self._get(cmd)

mc = MC()
# move agent to player first!
mc.tptoplayer()

# import time
# time.sleep(5)
# print(mc.inspect("right"))
# print(mc.inspectdata("left"))
# print(mc.turn("right"))
# print(mc.place(1,"forward"))
# print(mc.drop(1,1,"left"))
# print(mc.dropall("up"))
# print(mc.getitemdetail(1))
# print(mc.getitemspace(2))
# print(mc.getitemcount(3))
print(mc.fill(0,0,0,True,10,0,0,True,"stone"))
# print("hi")
# for i in range(10):
#    mc.turn("right")
#    mc.turn("left")
