def transposer(list_of_strings):
  return [" ".join(y[z] for y in [x.split() for x in list_of_strings]) for z in range(len(list_of_strings))]


transposer(['abc def ghi', 'jkl mno pqr', 'stu vwx yz'])
