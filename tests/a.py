#!/usr/bin/env python3 -B
import random,sys
sys.path += ["../src"]

from n2m import big,csv,doc,run,the,atom, \
                Data,ydist,ysort,xdist,xdists,shuffle

def atom(x):
  for what in (int, float):
    try: return what(x)
    except Exception: pass
  x = x.strip()
  y = x.lower()
  return (y == "true") if y in ("true", "false") else x

def project(data, row, a, b, C=None):
  C = C or xdist(data,a,b)
  A,B = xdist(data,row,a), xdist(data,row,b)
  return (A*A + C*C - B*B) / (C + 1/big)

def fmap(data, rows):
  one, *some = shuffle(rows)
  some = some[:the.Few]
  far  = int(0.9 *len(some))
  a    = xdists(data, one, some)[far]
  b    = xdists(data, a, some)[far]
  if ydist(data,a) > ydist(data,b): a,b = b,a
  C = xdist(data, a,b)
  return sorted(rows,key=lambda row: abs(project(data,row,a,b,C)))

def poles(data, done):
  out=[]
  for _ in range(32):
    a,b   = random.sample(done,2)
    C     = xdist(data,a,b) + 1/big
    ya,yb = ydist(data,a), ydist(data,b)
    out  += [(abs(ya-yb)/C, ya,yb,a,b,C)]
  return sorted(out, key=lambda z:z[0])[0]

def landscape(data, done,todo):
  _,ya,yb,a,b,C = poles(data,done)
  def D(row):
    x = project(data,row,a,b,C)
    return ya + x * (yb - ya) #if -.5 < C < 1.5 else 0
  return sorted(todo, key=D)

def landscapes(data):
  rows = data._rows
  done,todo = rows[:the.start], rows[the.start:]
  n=the.start
  while len(todo)>4 and n < the.Stop - 2:
    n=n+2
    a,b,*todo =  landscape(data,done,todo)
    done += [a,b]
    todo = todo[:int(len(todo)*.66)]
  return done

def run(data):
  random.shuffle(data._rows)
  return ydist(data, ysort(data,landscapes(data))[0])

random.seed(atom(sys.argv[0]))
data = Data(csv(doc("../../../timm/moot/optimize/misc/auto93.csv")))
print(sorted([round(run(data),2) for _ in range(20)]))
