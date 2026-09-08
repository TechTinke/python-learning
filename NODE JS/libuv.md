## Libuv

-> Native library that is used by Node Js

-> Helps Node Js handle async operations across different os systems

1. event loop

- Check for completed i/o operations
- Timers - check if some timers are in ready state
- Check for pending callbacks
- Socket Activity

2. worker thread pool

- Libuv provides a shared thread worker pool
- The pool that we have is used for operations that cannot be handled efficiently
- Used when:
  -> Many file system operations
  -> Cryptographic operations
  -> Compression related work

3. timers
   -> Help Node Js track all the timers
   -> Determine when a timer is eligible to execute

4. async I/O

- V8 does not provide:
  -> fs operations
  -> network socket handling
  -> timers
  -> general event loop for node js apis
- Node JS needs another layer that wil co-ordinate these runtime features
