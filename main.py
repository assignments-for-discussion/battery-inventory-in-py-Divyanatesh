
def count_batteries_by_usage(cycles):
  my_dict = {"lowcount":0,"mediumCount":0,"highcounCount":0}
  for c in cycles:
    if c < 400:
      my_dict["lowCount"] += 1
      elif 400 <= c <= 919:
        my_dict["mediumCount"] += 1
        elif c >= 920:
          my_dict[highCount"] += 1
   return my_dict               


def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  assert(counts["lowCount"] == 2)
  assert(counts["mediumCount"] == 3)
  assert(counts["highCount"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
