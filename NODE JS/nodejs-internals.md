## main js thread

- In normal applications, JS executes on one main JS thread

## v8 engine

- Parsing javascript
- Executing Javascript
- Managing call stack
- Managing Heap memory
- Perform garbage collection

## node js core apis

- buffers
- streams
- process object
- timers
- callbacks

-> some of these core modules are usually written in js

## c++ bindings

- Connect JS Facing APIs to native functionality allowing javascript code to communicate with libuv, os apis and native libraries

## libuv

- Libuv is a native library used by Node Js
- Libuv provides;
  -> event loop
  -> worker thread loop
  -> timers
  -> async I/O handling

## os

- Operating system is going to do the low level work like;
  -> reading files
  -> writing files
  -> tracking files
