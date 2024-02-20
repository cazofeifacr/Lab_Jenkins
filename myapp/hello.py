import fire

def hello(name="World from Jenkins"):
  return "Hello %s!" % name

if __name__ == '__main__':
  fire.Fire(hello)
