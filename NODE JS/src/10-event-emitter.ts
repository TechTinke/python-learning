import EventEmitter from "node:events";
// Event Emitters - emit one event
// listeners -> listen to the event emitted and do sth based on the event

// .on() - register one listener when an event is emitted
// .once() - register one listener that runs only once
// .emit() - triggers an event and sends it to the listeners

const appEvents = new EventEmitter();

type UserRegisterPayload = {
  id: number;
  email: string;
};
appEvents.once("user:registered", (user: UserRegisterPayload) => {
  console.log(`email listener: welcome email sent to ${user.email}`);
});
// whatever data is emitted by the emitter the listener is able to access that data

appEvents.on("user:registered", (user: UserRegisterPayload) => {
  console.log(`log listener: user ${user.id} and email is ${user.email}`);
});
// you can register multiple listeners for the same event

appEvents.once("app.started", () => {
  console.log("Once listener");
});

function registerUser(): void {
  const user = {
    id: 1,
    email: "sombaoscar27@gmail.com",
  };
  console.log("User saved");
  appEvents.emit("user:registered", user);
  appEvents.emit("user:registered", user)
  console.log("register user: event listens completed");
  appEvents.emit("app.started");
  appEvents.emit("app.started");
}
registerUser();
