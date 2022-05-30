void main() async {
  A i1 = A();
  print(i1.a);
  /*Future.delayed(Duration(seconds:6),(){
    print(i1.a);
  });*/
  print(i1.b);
  await Future.doWhile(() {
    return !(i1.b);
  });
  print(i1.b);
}

class A {
  int _a = 1;
  bool _b = false;
  int get a => _a;
  bool get b => _b;

  A() {
    //Future.delayed(Duration(seconds:5), (){_a = 10;});
    _assignBool();
  }

  _assignBool() async {
    await Future.delayed(Duration(seconds: 5));
    print('bool assignment finished');
    _b = true;
  }
}
