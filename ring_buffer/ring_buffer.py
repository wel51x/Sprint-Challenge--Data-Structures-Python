class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    self.storage[self.current] = item

    if self.current < self.capacity - 1:
      self.current += 1
    else:
      self.current = 0
    
  def get(self):
    return_list = []
    for item in self.storage:
      if item is not None:
        return_list.append(item)
    return return_list
