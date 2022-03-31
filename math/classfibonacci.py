class fibonacci:
  def __init__(self):
    self.fiboSeq = [0, 1]
    
  def __call__(self, n):
    if n < len(self.fiboSeq):
      return self.fiboSeq[n]
    else:
      # Compute the requested Fibonacci number
      fib_number = self(n - 1) + self(n - 2) 

      #Builds List
      self.fiboSeq.append(fib_number) 
      return self.fiboSeq[n]


n = int(input('Type the nth term in the fibonacci sequence: '))
fibonacci_of = fibonacci()
#Prints nth term that user inputed
print(fibonacci_of(n))