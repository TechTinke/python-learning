// Streams - handling large amounts of data like files, network requests in chunks and not as a whole
// Handling massive amounts of data can cause performance bottlenecks and memory exhaustion
// Streams help with memory efficiency as data is processed in chunks rather than loading the entire dataset into memory
// Streams help build scalable applications that can efficiently handle daunting datasets

import { read } from "node:fs";
import { Readable, Transform, Writable } from "node:stream";
import { pipeline } from "node:stream/promises";

// COMMON USE CASES
// - read large files
// - upload files
// - compression
// - downloading files
// - video/audio processing
// - processing large datasets
// CHUNKS - small data pieces

//  STREAM TYPES
// 1. READBLE STREAMS
// - Used to sequantially read a source of data e.g http request body, files, standard inputs e.t.c

// 2. WRITABLE STREAMS
// - Useful for creating files, uploading data or any task that invloves sequantilly outputting data
// - They act as the destination for your data
// - Transform streams - read the data, change it e.g convert it to uppercase, lowercase and pass it forward

const readableStream = Readable.from(["hello", "from", "node js", "streams"]);

const upperTransform = new Transform({
  transform(chunk, encoding, callback) {
    const text = chunk.toString();
    callback(null, text.toUpperCase());
  },
});

const writableStream = new Writable({
  write(chunk, encoding, callback) {
    console.log("received chunk", chunk.toString());
    callback(); // The job is alr done and the chunk can be moved on to the next
  },
});

// PIPELINE - connect all the streams together
async function main(): Promise<void> {
  try {
    await pipeline(readableStream, upperTransform, writableStream);
    console.log("Stream completed");
  } catch (error) {
    const msg = error instanceof Error ? error.message : "unknown error";
    console.error("Stream failed", msg);
  }
}
main();
