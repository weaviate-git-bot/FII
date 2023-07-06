abstract class MathOps<T, G> {
  int sub(T obj1, G obj2);
  int prod(T obj1, G obj2);
  int mod(T obj1, G obj2);
}

class MathOpsImpl<T extends num, G extends num> extends MathOps<T, G> {
  @override
  int sub(T obj1, G obj2) {
    return (obj1 - obj2).toInt();
  }

  @override
  int prod(T obj1, G obj2) {
    return (obj1 * obj2).toInt();
  }

  @override
  int mod(T obj1, G obj2) {
    return obj1 % obj2 as int;
  }
}

class MathOpsStringImpl<T extends String, G extends String>
    extends MathOps<T, G> {
  @override
  int sub(T obj1, G obj2) {
    return obj1.length - obj2.length;
  }

  @override
  int prod(T obj1, G obj2) {
    return obj1.length * obj2.length;
  }

  @override
  int mod(T obj1, G obj2) {
    return obj1.codeUnitAt(0) % obj2.codeUnitAt(0);
  }
}

void main() {
  var mathOps = MathOpsImpl<int, double>();
  print(mathOps.sub(10, 5.5)); // Output: 4

  var mathOpsDouble = MathOpsImpl<double, int>();
  print(mathOpsDouble.prod(2.5, 3)); // Output: 7

  var stringOps = MathOpsStringImpl<String, String>();
  print(stringOps.mod('abc', 'def')); // Output: 97
}
