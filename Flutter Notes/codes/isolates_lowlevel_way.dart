import 'dart:async';
import 'dart:isolate';

//send port send messages & corresponding reciver port recieves

main() async {
  //main isolate's port
  var receivePort = new ReceivePort();
  await Isolate.spawn(echo, receivePort.sendPort);

  // The 'echo' isolate sends it's SendPort as the first message so this will be poiting to sendPort
  //sendPort is of echo isolate
  //recievePort is of main(default) isolate
  var echoIsolate_sendPort = await receivePort.first;

  //Message is send from echo isolate & must be recieved by main isolate
  var msg = await sendReceive(echoIsolate_sendPort, "foo");
  print('received $msg');
  msg = await sendReceive(echoIsolate_sendPort, "bar");
  print('received $msg');
}

// the entry point for the isolate
Future<void> echo(SendPort sendPort) async {
  // Open the ReceivePort for incoming messages.
  var port = new ReceivePort();

  // Notify any other isolates what port this isolate (i.e `echo`) listens to.
  // Echo isolate is telling main isolate what is its send Port Number
  sendPort.send(port.sendPort);

  //Recieve Port is Stream of messages so here waiting till message arrives from stream & then exit
  await for (var msg in port) {
    var data = msg[0];
    SendPort replyTo = msg[1];
    replyTo.send(data);
    if (data == "bar") port.close();
  }
}

/// sends a message on a port, receives the response,
/// and returns the message
Future sendReceive(SendPort port, msg) {
  ReceivePort response = new ReceivePort();
  port.send([msg, response.sendPort]);
  return response.first;
}
