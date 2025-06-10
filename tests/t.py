def a(s):
  try: return int(s)
  except Exception as _:
    try: return float(s)
    except Exception as _:
      return s

def b(s):
  return int(s) if s.isdigit() else float(s)
