class Client {
  final String _name;
  double _purchasesAmount = 0.0;

  Client(this._name);

  double get purchasesAmount => _purchasesAmount;
  void set purchasesAmount(double value) => _purchasesAmount = value;
}

class LoyalClient extends Client {
  LoyalClient(String name) : super(name);

  double get totalPurchasesAmount => super.purchasesAmount;

  void discount() {
    final currentAmount = super.purchasesAmount;
    final discountedAmount = currentAmount - (currentAmount * 0.1);
    super.purchasesAmount = -currentAmount;
    super.purchasesAmount = discountedAmount;
  }
}

void main() {
  final client = Client('Dan');
  client.purchasesAmount = 100.0;
  print(client.purchasesAmount);

  final loyalClient = LoyalClient('Bogdan');
  loyalClient.purchasesAmount = 200.0;
  loyalClient.discount();
  print(loyalClient.totalPurchasesAmount);
}
