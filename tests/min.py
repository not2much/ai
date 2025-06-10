import random

def adds(i,lst): [add(i,x) for x in lst]; return i

def cat(v): 
  it = type(v)
  inf = float('inf')
  if it is list:  return "{" + ", ".join(map(cat, v)) + "}"
  if it is float: return str(int(v)) if -inf<v<inf and v==int(v) else f"{v:.3g}"
  if it is dict:  return cat([f":{k} {cat(w)}" for k, w in v.items()])
  if it in [type(abs), type(cat)]: return v.__name__ + '()'
  return str(v)

class o:
  __init__ = lambda i, **d: i.__dict__.update(**d)
  __repr__ = lambda i: cat(i.__dict__)

the = o(some=256)

def Some(inits=[], at=0, txt=" ", rank=0):
  return adds(o(it=Some,
                n      = 0,      ## items seen  
                at     = at,     ## column position
                txt    = txt,    ## column name
                _has   = [],     ## seen
                rank   = rank,   ## used by stats, ignored otherwise
                ready  = False,
                nump   = txt[0].isupper(),
                heaven = (0 if txt[-1] == "-" else 1), ## 0,1 = minimize,maximize
                ), inits)

def add(i,x):
  if x != "?":
    i.n += 1
    if len(i._has) < the.some: 
      i.ready = False
      i._has += [x]
    elif random.random() < the.some/i.n: 
      i.ready = False
      i._has[random.randint(0, len(i._has))] = x
  return x

def ok(i):
  if not i.ready: random.shuffle(i._has)
  i.ready = True
  return i
  
local Some=klass"Some"
function Some:new(max) 
  return uses(Some, {n=0, max=max or 256, old=true, _has={}}) end

--Add to a reservoir sampling. If full, replace anything at random.
function Some:add(x) 
  self.n = self.n + 1
  if #self._has < self.max then pos = 1+#self._has 
  elseif rand() < self.max/self.n then pos = 1+(rand()*#self._has)//1 end 
  if pos then 
    self.old=true
    self._has[pos]=x end end 

-- Return the contents, sorted.
function Some:has()  
  if self.old then table.sort(self._has) end
  self.old = false
  return self._has end
