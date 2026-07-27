import { rejects } from "assert";
import { removeListener } from "cluster";
import { error, log } from "console";
import { resolve } from "dns";

// type User = {
//   id: number;
//   name: string;
//   role: "user" | "super-admin";
// };

// const users: User[] = [
//   {
//     id: 1,
//     name: "Oscar",
//     role: "user",
//   },
//   {
//     id: 2,
//     name: "Erick",
//     role: "super-admin",
//   },
//   {
//     id: 3,
//     name: "Abel",
//     role: "super-admin",
//   },
//   {
//     id: 4,
//     name: "Morris",
//     role: "user",
//   },
//   {
//     id: 5,
//     name: "Michael",
//     role: "user",
//   },
// ];
// callback - function that you are going to pass into another function
// callback(error, result) - classic callback pattern

function findUserWithCallback(
  userId: number,
  callback: (error: Error | null, user?: User) => void,
): void {
  setTimeout(() => {
    const user = users.find((currentUser) => currentUser.id === userId);
    if (!user) {
      callback(new Error(`User with id ${userId} does not exist`));
      return;
    }
    callback(null, user);
  }, 500);
}
// findUserWithCallback(4, (error, user) => {
//   if (error) {
//     console.log(error.message);
//     return;
//     console.log("Callback result", user?.id, user?.name, user?.role);
//   }
// });
function findUserWithPromise(userId: number): Promise<User> {
  return new Promise((resolve, reject) => {
    const user = users.find((currentUser) => currentUser.id === userId);
    if (!user) {
      reject(new Error(`User with id ${userId} does not exist`));
      return;
    }
    resolve(user);
  });
}
// findUserWithPromise(3)
//   .then((user) => {
//     console.log("Promise result", user?.id, user?.name, user?.role);
//   })
//   .catch((error: Error) => {
//     console.log("Promise error", error.message);
//   });
async function findUserWithAsyncAwait(userId: number): Promise<void> {
  try {
    const user = await findUserWithPromise(userId);
    console.log("async/await", user.name);
  } catch (error) {
    const message = error instanceof Error ? error.message : "unknown error";
    console.log("async/await", message);
  }
}
// findUserWithAsyncAwait(10);

type User = {
  id: number;
  name: string;
  role: "user" | "super-admin";
};

type Order = {
  orderId: string;
  userId: number;
  amount: number;
};

type AuditLog = {
  logId: string;
  action: string;
  timestamp: number;
};

const users: User[] = [
  { id: 1, name: "Oscar", role: "user" },
  { id: 2, name: "Erick", role: "super-admin" },
  { id: 3, name: "Abel", role: "super-admin" },
  { id: 4, name: "Morris", role: "user" },
  { id: 5, name: "Michael", role: "user" },
];

const orders: Order[] = [
  { orderId: "ORD-001", userId: 1, amount: 250 },
  { orderId: "ORD-002", userId: 4, amount: 120 },
  { orderId: "ORD-003", userId: 1, amount: 45 },
];

// Practical Assessment Tasks
// Task 1: The Callback Pattern (Error-First)Scenario:
// You need to fetch user data using a legacy Node.js callback style.
// Requirement: Implement a function called fetchUserCallback that simulates a 500ms database delay.
// It must follow the standard Node.js error-first callback pattern.

function fetchUserCallback(
  userId: number,
  callback: (error: Error | null, user?: User) => void,
): void {
  setTimeout(() => {
    const user = users.find((currentUser) => currentUser.id === userId);
    if (!user) {
      console.log(new Error(`User with id ${userId} does not exist`));
    }
    callback(null, user);
  }, 500);
}
// fetchUserCallback(3, (error, user) => {
//   if (error) {
//     console.log("Callback error - ", error.message);
//   }
//   console.log("Callback result - ", user?.id, user?.name, user?.role);
// });

// Task 1.1: Error-First Node.js Callback Finder
// Requirement: Implement a function findUserByIdCallback(id, callback) that looks up a user in the users array after a 300ms delay.
// It must use the Node.js standard error-first signature (err, data).
// Throw an error if the user is missing.

// Soln 1
function findUserByIdCallback(
  id: number,
  callback: (error: Error | null, user?: User) => void,
): void {
  setTimeout(() => {
    const user = users.find((currentUser) => currentUser.id === id);
    if (!user) {
      console.log(new Error(`User with id ${id} does not exist`));
      return;
    }
    callback(null, user);
  });
}
// findUserByIdCallback(6, (error, user) => {
//   if (error) {
//     console.log("Callback error -", error.message);
//   }
//   console.log("Callback result - ", user?.id, user?.name, user?.role);
// });

// Soln 2
function findUserByIdCallback1(
  id: number,
  callback: (err: Error | null, user?: User) => void,
) {
  setTimeout(() => {
    const user = users.find((u) => u.id === id);
    if (!user) {
      return callback(new Error(`User with ID ${id} not found`));
    }
    callback(null, user);
  }, 300);
}
// findUserByIdCallback1(7, (err, user) => {
//   if (err) console.log("Error:", err.message);
//   else console.log("Task 1.1 Success:", user);
// });
