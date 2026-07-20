import crypto from "node:crypto";
// built in node js module

// Uses of crypto module
// - security related tasks
// - Creating UUIDs, IDs
// - Creating secure tokens
// - Hashing data
// - Verify if data was changed or not
// - Encryption and decryption

crypto.randomUUID;
// UUID - Universal Unique Identifier
// - Used when you need a unique ID like user id, order id, session id, request id

const requestId = crypto.randomUUID();
//console.log(requestId); // will return a random UUID - 4acda3df-dcef-4cfb-829b-53449179dd0a

crypto.randomBytes;
// creating secure secret random bytes e.g password reset token, email verification token, api keys

// 32 character string
const resetToken = crypto.randomBytes(16).toString("hex"); // when you convert into hex format, 1 byte(character) become a 2-character string
//console.log(resetToken); //cce12f152d2e83881db9cc67a5fd6071
// <Buffer a9 b1 5d 02 6e 80 e8 6d 37 8d c2 22 12 90 58 7f> - before conversion to String

crypto.createHash;
// - Converts your data into a fixed length string
// - Hashing is one way cryptographic operation so if you convert input to an hash you can't convert the hash into the original input

const text = "hello node";
const hash = crypto.createHash("sha256").update(text).digest("hex");
// console.log(hash);
// console.log(text);

crypto.createHmac;
// Hmac - Hash-based message authentication code
// - Used when creating webhooks or signed tokens
// normal hash : data -> hash

// HMAC: data + secret -> signed hash

const secretKey = "secret key";
const message = "user_id=1";

const signature = crypto
  .createHmac("sha256", secretKey)
  .update(message)
  .digest("hex");
// console.log(signature);

const signatureVerify = crypto
  .createHmac("sha256", secretKey)
  .update(message)
  .digest("hex");
console.log("Signature is valid and matching", signature === signatureVerify);
