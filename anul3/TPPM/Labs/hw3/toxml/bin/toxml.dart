import 'package:xml/xml.dart';

class Example {
  int varA;
  int varB;
  String varC;
  List<int> varD;
  double varE;

  Example(
      {this.varA = 0,
      this.varB = 0,
      this.varC = '',
      this.varD = const [],
      this.varE = 0.0});

  factory Example.fromXml(XmlElement element) {
    return Example(
      varA: int.parse(element.getElement('varA')?.text ?? '0'),
      varB: int.parse(element.getElement('varB')?.text ?? '0'),
      varC: element.getElement('varC')?.text ?? '',
      varD: element
              .getElement('varD')
              ?.childElements
              .map((e) => int.parse(e.text))
              .toList() ??
          [],
      varE: double.parse(element.getElement('varE')?.text ?? '0.0'),
    );
  }

  XmlElement toXml() {
    return XmlElement(
      XmlName('Example'),
      [
        XmlAttribute(XmlName('varA'), varA.toString()),
        XmlAttribute(XmlName('varB'), varB.toString()),
        XmlAttribute(XmlName('varC'), varC),
        XmlAttribute(XmlName('varD'), varD.join(',')),
        XmlAttribute(XmlName('varE'), varE.toString()),
      ],
    );
  }
}

void main() {
  final xml = '''<Example>
  <varA>1</varA>
  <varB>2</varB>
  <varC>hello world bzv</varC>
  <varD>
    <item>1</item>
    <item>2</item>
    <item>3</item>
  </varD>
  <varE>127</varE>
</Example>''';

  final element = XmlDocument.parse(xml).rootElement;
  final example = Example.fromXml(element);
  print(example.varA);
  print(example.varB);
  print(example.varC);
  print(example.varD);
  print(example.varE);
  final newValues = example.toXml();
  print(newValues.toXmlString(pretty: true, indent: '  '));
}
