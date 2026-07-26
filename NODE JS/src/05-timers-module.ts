// run code after some delay
// run code repeatedly after some interval

import { log } from "console";
import { error, time } from "node:console";
import { setTimeout as sleep } from "node:timers/promises";

// settimeout
// setinterval
// cleartimeout
// clearinterval
// setimmediate

// setTimeout - run the callback after some defined period of time(milli seconds)
function runSetTimeout(): void {
  console.log("Waiting for promise based timer");
  setTimeout(() => {
    console.log("Promise based timer finishes after 5.5 seconds");
  }, 5500);
  // console.log("This runs immediately");
}

function runClearTimeout(): void {
  const setTimerId = setTimeout(() => {
    console.log("Callback delay of 3 seconds has ended");
  }, 3000);
  clearTimeout(setTimerId);
  console.log(
    "Callback has been cleared and callback delay of 3 seconds will not run",
  );
}

// // setInterval - run the callback again and again after the fixed delay
function runSetInterval(): void {
  let count = 0;
  console.log("Count has started");
  const setIntervalId = setInterval(() => {
    count++;
    console.log(`Count: ${count}`);
    if (count === 5) {
      clearInterval(setIntervalId);
      console.log("Count has reached 5");
    }
  }, 5000);
}

// // setImmediate() - run the callback after the current synchronous code finishes immediately
// sychronous programming - executes tasks sequantially, blocking the next operation until the current one completes
function runSetImmediate(): void {
  setImmediate(() => {
    console.log("Immediate callback");
  });
  console.log("Synchronous code after setImmediate");
}

// NB: The rimary difference betweeen setTimeout() and Promise Based Timer
// - setTimeout() - relies on a callback function
// - promiseBasedTimer() - returns a Promise object that resolves after the specified delay
async function runPromiseTimer(): Promise<void> {
  console.log("Waiting for promise based timer");

  await sleep(5500);
  console.log("Promise based timer finishes after 5.5 seconds");
}
function runTimerDemo(): void {
  // runSetTimeout();
  // runClearTimeout();
  // runSetInterval();
  // runSetImmediate();
}
runTimerDemo();
runPromiseTimer().catch((error: unknown) => {
  console.error("Timer based demo failed", error);
});
