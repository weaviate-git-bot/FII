class Queue {
  List _list = [];

  void push(dynamic element) {
    _list.add(element);
  }

  dynamic pop() {
    if (_list.isEmpty) {
      return null;
    }
    return _list.removeAt(0);
  }

  dynamic front() {
    if (_list.isEmpty) {
      return null;
    }
    return _list[0];
  }

  dynamic back() {
    if (_list.isEmpty) {
      return null;
    }
    return _list.last;
  }

  bool isEmpty() {
    return _list.isEmpty;
  }

  @override
  String toString() {
    return _list.toString();
  }
}

void main() {
  Queue queue = Queue();
  queue.push(1);
  queue.push(2);
  queue.push(3);
  queue.push(4);
  queue.push(5);
  print(queue);
  print(queue.pop());
  print(queue);
  print(queue.front());
  print(queue.back());
  print(queue.isEmpty());
}
