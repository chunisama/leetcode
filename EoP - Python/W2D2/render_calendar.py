# Write a program that takes a set of events, and determines the maximum number of events 
# that take place concurrently.

events = [[1, 5], [2, 7], [4, 5], [6, 10], [8, 9], [9, 17], [11, 13], [12, 15], [14, 15]]

class Endpoint():
  def __init__(self, val, is_start):
    self.val = val
    self.is_start = is_start

def find_max_simultaneous_events(events):
  endpoints_arr = []
  max_counter, counter = 0, 0
  for event in events:
    start = Endpoint(event[0], True) 
    end = Endpoint(event[1], False)
    endpoints_arr.append(start)
    endpoints_arr.append(end)
  endpoints_arr.sort(key=lambda e:(e.val))
  for event in endpoints_arr:
    if event.is_start:
      counter += 1
    else:
      counter -= 1
    max_counter = max(max_counter, counter)
  return max_counter


print(find_max_simultaneous_events(events))
