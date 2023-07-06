int wordSum(List<String> arguments) {
  Map<String, int> points = {};
  int i = 0;

  while (i < arguments.length - 1) {
    points[arguments[i]] = int.parse(arguments[i + 1]);
    i += 2;
  }

  String word = arguments[arguments.length - 1];

  int sum = 0;
  for (int idx = 0; idx < word.length; ++idx) {
    sum += points[word[idx]]!;
  }
  return sum;
}

void main(List<String> arguments) {
  print(wordSum(arguments));
}
