// represents your current running Node Js program

// env variables - infromation(variables) contained in your env file
// env - where you keep all the sensitive infromation(URLs, passwords, API keys, Google Auth secrets)

// command line arguments
// exit code
// process lifecycle events

// Importance of process object
// - Read backend ports from env file
// - Read secrets - db urls, api keys, passwords, google auth secrets
// - Read CLI arguments in scripts

import { log } from "node:console";
import process from "node:process";

// dotenv - read env variables directly in our NodeJS project

const nodeEnv = process.env.NODE_ENV ?? "development";
// process.env - read all the env variables(URLs, secrets)
// process.env values are always string or undefined

const command = process.argv[2] ?? "start";
// process.argv[2]->
// // the first two elements are usually reserved by NodeJS(path to Node & path to file)

// [
//     "/path/to/node"  // [0] path to node
//     "src/01-process-object.ts" // [1] path to file
//     "start" // [2] custom argument/command
// ]

// fail flag
// crash flag

const shouldFail = process.argv.includes("--fail");
const shouldCrash = process.argv.includes("--crash");

process.on("exit", (code) => {
  console.log(`Process finished with exit code ${code}`);
});

// do not use async here as Node is already shutting down
// - Final log
// - Final clean up

function runApp(): void {
  console.log({ command });
  if (shouldFail) {
    console.error("Manual failure triggered with --error flag");
    process.exit(1);
  }
  if (shouldCrash) {
    console.error("Manual crash triggered with --crash flag");
    process.exit(1);
  }
}
runApp();
