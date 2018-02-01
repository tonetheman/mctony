
import urllib2

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
        u = urllib2.urlopen("http://localhost:8080/" +  path)
        data = u.read()
        u.close()
        return data
    
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


mc = MC()
print(mc.inspect("right"))
print(mc.inspectdata("left"))
print(mc.turn("right"))
print(mc.place(1,"forward"))
print(mc.drop(1,1,"left"))
print(mc.dropall("up"))
print(mc.getitemdetail(1))
print(mc.getitemspace(2))
print(mc.getitemcount(3))