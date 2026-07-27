import { rejects } from "assert";
import { removeListener } from "cluster";
import { error, log } from "console";
import { resolve } from "dns";

type User = {
  id: number;
  name: string;
  role: "user" | "super-admin";
};

const users: User[] = [
  {
    id: 1,
    name: "Oscar",
    role: "user",
  },
  {
    id: 2,
    name: "Erick",
    role: "super-admin",
  },
  {
    id: 3,
    name: "Abel",
    role: "super-admin",
  },
  {
    id: 4,
    name: "Morris",
    role: "user",
  },
  {
    id: 5,
    name: "Michael",
    role: "user",
  },
];
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
findUserWithCallback(4, (error, user) => {
  if (error) {
    console.log(error.message);
    return;
    console.log("Callback result", user?.id, user?.name, user?.role);
  }
});
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
findUserWithPromise(3)
  .then((user) => {
    console.log("Promise result", user?.id, user?.name, user?.role);
  })
  .catch((error: Error) => {
    console.log("Promise error", error.message);
  });
async function findUserWithAsyncAwait(userId: number): Promise<void> {
  try {
    const user = await findUserWithPromise(userId);
    console.log("async/await", user.name);
  } catch (error) {
    const message = error instanceof Error ? error.message : "unknown error";
    console.log("async/await", message);
  }
}
findUserWithAsyncAwait(10);
