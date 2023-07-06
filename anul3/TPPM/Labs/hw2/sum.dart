int getSum(int nr) {
  int sum = 0;
  while (nr > 0) {
    sum += nr % 10;
    nr ~/= 10;
  }
  return sum;
}

int sum(int number) {
  Map<int, List<int>> pairs = {};
  int maxLength = 0;
  for (int nr = 1; nr <= number; ++nr) {
    int nrSum = getSum(nr);
    if (pairs.containsKey(nrSum)) {
      pairs[nrSum]?.add(nr);
    } else {
      pairs[nrSum] = [nr];
    }
    int currentSize = (pairs[nrSum]?.length ?? 0);
    if (currentSize > maxLength) {
      maxLength = currentSize;
    }
  }
  int howManyEqual = 0;
  pairs.forEach((key, value) {
    if (value.length == maxLength) {
      ++howManyEqual;
    }
  });
  return howManyEqual;
}

void main() {
  print(sum(13));
}
