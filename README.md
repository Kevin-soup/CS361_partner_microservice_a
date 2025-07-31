Microservice A - EncryptionConverter

---

A. How to REQUEST data.

  After setting up your ZeroMQ environment, connect to socket 5555:
      socket.connect("tcp://localhost:5555")
  
  To send a request message for binary-plaintext conversion, use:
      socket.send_string(message)
      
  Example Call:
  message = "hi"
  socket.send_string(message)
  
  Note: 
  Binary messages should include spaces. 
  Multiple requests are allowed when the microservice is running.
  
---

B. How to RECIEVE data

  To recieve the converted message, use:
      response = socket.recv().decode()

  Example Call:
  response = socket.recv().decode()
  print(response)  --> "01101000 01101001"
  
  Note:
  Microservice utilizes ZeroMQ REQ-REP sockets.
  
---  

C. UML Sequence Diagram

