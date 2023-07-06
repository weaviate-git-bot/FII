import 'dart:async';
import 'dart:math';

import 'package:flutter/material.dart';
import 'package:shoppingliswt/ui/category_image_painter.dart';

class CartScreen extends StatefulWidget {
  const CartScreen({super.key});
  final String title = 'My Cart';
  @override
  State<CartScreen> createState() => _CartScreenState();
}

class _CartScreenState extends State<CartScreen> {
  final TextEditingController _controller = TextEditingController();
  List<Map<String, String>> _items = [];
  String? _category;
  final Map<String, Color> _colors = {
    'Grocery': Colors.blue,
    'Clothing': Colors.pink,
    'Electronics': Colors.green,
    'Home': Colors.blueAccent,
    'Other': Colors.orange,
  };
  late final Timer _timer;

  _CartScreenState() {
    _timer = Timer.periodic(const Duration(seconds: 5), (timer) {
      setState(() {
        if (_items.isEmpty || !mounted) return;
        for (dynamic key in _colors.keys) {
          _colors[key] = Color((Random().nextDouble() * 0xFFFFFF).toInt())
              .withOpacity(1.0);
        }
      });
    });
  }

  @override
  void dispose() {
    _timer.cancel();
    _controller.dispose();
    super.dispose();
  }

  void _addItem() {
    setState(() {
      if (_controller.text.isEmpty) return;
      _category ??= 'Grocery';

      _items.add({
        'value': _controller.text,
        'category': _category!,
      });
      _controller.clear();
      _category = null;
    });
  }

  void _deleteItem(int index) {
    setState(() {
      _items.removeAt(index);
    });
  }

  Color getColorByCategory(String category) {
    return _colors[category] ?? Colors.white;
  }

  Widget _buildItem(BuildContext context, int index) {
    return Card(
        elevation: 4.0,
        child: Padding(
            padding: const EdgeInsets.all(4.0),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              mainAxisSize: MainAxisSize.max,
              children: <Widget>[
                CustomPaint(
                  painter: CategoryImagePainter(
                      color: getColorByCategory(_items[index]['category']!),
                      category: _items[index]['category']!),
                  child: Container(
                    width: 50,
                    height: 50,
                  ),
                ),
                Expanded(
                  child: Text(_items[index]['value']!),
                ),
                IconButton(
                  icon: const Icon(Icons.delete),
                  onPressed: () => _deleteItem(index),
                ),
              ],
            )));
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Column(
        children: <Widget>[
          Row(
            children: [
              Expanded(
                child: TextField(
                  controller: _controller,
                  decoration: InputDecoration(
                    hintText: 'Enter an item',
                    contentPadding: const EdgeInsets.all(16.0),
                  ),
                  onSubmitted: (_) => _addItem(),
                ),
              ),
              DropdownButton<String>(
                  value: _category,
                  hint: const Text('Select a category'),
                  items: <String>[
                    'Grocery',
                    'Clothing',
                    'Electronics',
                    'Home',
                    'Other'
                  ].map<DropdownMenuItem<String>>((String value) {
                    return DropdownMenuItem<String>(
                      value: value,
                      child: Text(
                        value,
                        style: TextStyle(fontSize: 30),
                      ),
                    );
                  }).toList(),
                  onChanged: (String? newValue) {
                    setState(() {
                      _category = newValue;
                    });
                  }),
              TextButton(
                onPressed: _addItem,
                child: Text('Add'),
              ),
            ],
          ),
          Expanded(
            child: GridView.builder(
              padding: const EdgeInsets.all(16.0),
              gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
                crossAxisCount: 2,
                childAspectRatio: 3 / 1,
                crossAxisSpacing: 16.0,
                mainAxisSpacing: 16.0,
              ),
              itemCount: _items.length,
              itemBuilder: _buildItem,
            ),
          ),
        ],
      ),
      // floatingActionButton: FloatingActionButton(
      //   onPressed: _addItem,
      //   tooltip: 'Add new item',
      //   child: const Icon(Icons.add),
      // ), // This trailing comma makes auto-formatting nicer for build methods.
    );
  }
}
