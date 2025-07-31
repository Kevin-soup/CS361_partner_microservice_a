Microservice A - EncryptionConverter

---

A. How to REQUEST data.


  &nbsp;&nbsp; After setting up your ZeroMQ environment, connect to socket 5555:
      `socket.connect("tcp://localhost:5555")`
  
  &nbsp;&nbsp; To send a request message for binary-plaintext conversion, use:
      `socket.send_string(message)`
      
  &nbsp;&nbsp; Example Call:
  ```
  message = "hi"
  socket.send_string(message)
  ```
  &nbsp;&nbsp; Note: 
  &nbsp;&nbsp; Binary messages should include spaces. 
  &nbsp;&nbsp; Multiple requests are allowed when the microservice is running.
  
---

B. How to RECIEVE data




  &nbsp;&nbsp; To recieve the converted message, use:
      `response = socket.recv().decode()`

  &nbsp;&nbsp; Example Call:
  ```
  response = socket.recv().decode()
  print(response)  --> "01101000 01101001"
  ```

  &nbsp;&nbsp; Note:
  &nbsp;&nbsp; Microservice utilizes ZeroMQ REQ-REP sockets.
  
---  

C. UML Sequence Diagram


