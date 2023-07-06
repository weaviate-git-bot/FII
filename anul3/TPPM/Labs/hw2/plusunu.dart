// Ex1
List<int> plusOne(List<String> numbers) {
  List<int> digits = [];
  String completeNumber = "";

  numbers.forEach((element) {
    completeNumber += element;
  });

  int number = int.parse(completeNumber);
  number += 1;

  while (number != 0) {
    digits.add(number % 10);
    number = number ~/ 10;
  }

  return digits.reversed.toList();
}

void main(List<String> arguments) {
  print(plusOne(arguments));
}
