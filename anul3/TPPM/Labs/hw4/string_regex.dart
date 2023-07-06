List<String> getStrings(String input, List<String> regexList) {
  List<String> result = [];
  for (String s in regexList) {
    RegExp exp = new RegExp(s);
    Iterable<Match> matches = exp.allMatches(input);
    for (Match m in matches) {
      result.add(m.group(0) ?? '');
    }
  }
  return result;
}

void main() {
  String input = "This is a test string. 1234 5678 90";
  List<String> regexList = [r"\d+", r"[a-z]+", r"[A-Z]+", r"[a-zA-Z]+"];

  List<String> result = getStrings(input, regexList);
  print(result);
}
