import { log } from "console";

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
findUserWithCallback(3, (error, user) => {
  if (error) {
    console.log("Callback error", error.message);
    console.log("Callback result", user?.id, user?.name, user?.role);
  }
});
