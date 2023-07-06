int goodPairs(List<int> list) {
  int counter = 0;

  for (var idx = 0; idx < list.length; ++idx) {
    for (var idx2 = idx + 1; idx2 < list.length; ++idx2) {
      if (list[idx] == list[idx2] && idx != idx2) {
        ++counter;
      }
    }
  }

  return counter;
}

void main() {
  print(goodPairs([1, 2, 3, 1, 1, 3]));
}
