import 'dart:io';

class Lifo<T> {
  late RandomAccessFile _dataFile;
  late RandomAccessFile _indexFile;
  int _top = -1;

  Lifo(String dataFilePath, String indexFilePath) {
    _dataFile = File(dataFilePath).openSync(mode: FileMode.write);
    _indexFile = File(indexFilePath).openSync(mode: FileMode.write);
    _indexFile.writeByteSync(_top);
  }

  void push(int element) {
    _top++;
    _dataFile.setPositionSync(_top * 4);
    _dataFile.writeByteSync(element);
    _indexFile.setPositionSync(0);
    _indexFile.writeByteSync(_top);
  }

  int? pop() {
    if (_top == -1) {
      return null;
    }
    _dataFile.setPositionSync(_top * 4);
    int value = _dataFile.readByteSync();
    _top--;
    _indexFile.setPositionSync(0);
    _indexFile.writeByteSync(_top);
    return value;
  }

  int get size => _top + 1;
  bool get isEmpty => _top == -1;
}

void main() {
  var stack = Lifo('data.txt', 'index.txt');
  stack.push(10);
  stack.push(20);
  stack.push(30);
  print(stack.pop());
  print(stack.pop());
  print(stack.pop());
  stack.push(40);
  print(stack.pop());
  print(stack.pop());
}
