// buffers - work with raw binary data
// binary data - data stored in bytes

// USE CASES
// - reading files
// - receiving http req bodies
// - working with streams
// - handling images, pdf files, videos
// - encrytion and hashing

const textBuffer = Buffer.from("Node"); // converts normal text into raw bytes(hexadecimal format)
// console.log(textBuffer);
// N - 4e
// O - 6f
// D - 64
// E - 65
// console.log(textBuffer.toString("utf-8"));

// Buffer Length
const engBuffer = Buffer.from("Hello");
// console.log(engBuffer.length);

// .alloc
// - create a empty buffer of a fixed length
const fixedBuffer = Buffer.alloc(5); // empty fixed buffer of length 5 bytes
// console.log("empty fixed buffer", fixedBuffer);

//.write
// - write data into an existing buffer
fixedBuffer.write("API");
// console.log("fixed buffer as text", fixedBuffer.toString("utf-8"));

// .concat - combine diff data chunks in buffers into one buffer
const chunks = [Buffer.from("Hello"), Buffer.from("Node"), Buffer.from("JS")];
const combinedBuffer = Buffer.concat(chunks);
console.log(combinedBuffer);
console.log(combinedBuffer.toString("utf-8"));
