import path from "node:path";
import fs, { read, Stats, write, writeFile } from "node:fs";
import { log } from "console";
import { mainModule } from "node:process";
import fsPromises from "node:fs/promises";
import { stat } from "node:fs/promises";
import { reduceEachLeadingCommentRange } from "typescript/unstable/ast";
// file system - allows you to work with files and folders
// - Perform file and directory operations on server e.g

// - create folders
// - create files
// - read files
// - check file information
// - delete files

//1. Sychronous APIs
//2. Callback APIs
//3. Promise APIs

//1. Synchronous APIs
// When to Use
// - small startup scripts
// - building scripts
// - local demos

// When to not use
// - high traffic apis
// - background jobs
// - http req handlers

const FOLDER_PATH = path.join(process.cwd(), "file-system", "fs-demo");
const SYNC_FILE_PATH = path.join(FOLDER_PATH, "sync-note.txt");
const CALLBACK_FILE_PATH = path.join(FOLDER_PATH, "callback-note.txt");
const PROMISE_FILE_PATH = path.join(FOLDER_PATH, "promise-note.txt");

type FileResult = {
  style: string;
  fileName: string;
  dirName: string;
  content: string;
  sizeInBytes: number;
};
function ensureDemoFolderExists(): void {
  if (!fs.existsSync(FOLDER_PATH)) {
    fs.mkdirSync(FOLDER_PATH, { recursive: true });
    // { recursive: true} - ensures that all nested parent directories missing from target path are generated
    // along with the target folder without throwing errors
  }
}
function runSyncExample(): FileResult {
  // Write content to a file
  fs.writeFileSync(SYNC_FILE_PATH, "Created using sync fs", "utf-8"); // utf-8 means normal text
  // writeFileSync automatically creates the file if it doesn't exist. If it exists then the original file contents are completely overwritten and teplaced by the new string contents
  // Apend content
  fs.appendFileSync(SYNC_FILE_PATH, "Appended using sync fs", "utf-8");

  const fileContent = fs.readFileSync(SYNC_FILE_PATH, "utf-8");
  const fileStats = fs.statSync(SYNC_FILE_PATH);

  return {
    style: "sync",
    content: fileContent,
    fileName: path.basename(SYNC_FILE_PATH),
    dirName: path.dirname(SYNC_FILE_PATH),
    sizeInBytes: fileStats.size,
  };
}

//2. Callback APIs
function runCallbackExample(): Promise<FileResult> {
  return new Promise((resolve, reject) => {
    fs.writeFile(
      CALLBACK_FILE_PATH,
      "Created using callback fs",
      "utf-8",
      (writeError) => {
        if (writeError) {
          reject(writeError);
          return;
        }
        fs.appendFile(
          CALLBACK_FILE_PATH,
          "Appended using callback fs",
          "utf-8",
          (appendError) => {
            if (appendError) {
              reject(appendError);
              return;
            }
            fs.readFile(
              CALLBACK_FILE_PATH,
              "utf-8",
              (readError, fileContent) => {
                if (readError) {
                  reject(readError);
                  return;
                }
                fs.stat(CALLBACK_FILE_PATH, (statError, stats) => {
                  if (statError) {
                    reject(statError);
                    return;
                  }
                  resolve({
                    style: "callback",
                    fileName: path.basename(CALLBACK_FILE_PATH),
                    content: fileContent,
                    dirName: path.dirname(CALLBACK_FILE_PATH),
                    sizeInBytes: stats.size,
                  });
                });
              },
            );
          },
        );
      },
    );
  });
}

//3. Promise APIs
// - You have to imort fsPromises from "node:fs/promises"
// Asynchronous function - block of code that performs a task without freezing the rest of the program and
// instead of idly waiting for the task to finish, the program moves on to run other code and handles the result when it arrives

// example: fetching data from an internal api or database

async function runPromiseExample(): Promise<FileResult> {
  await fsPromises.writeFile(
    PROMISE_FILE_PATH,
    "Created using promise",
    "utf-8",
  );
  await fsPromises.appendFile(
    PROMISE_FILE_PATH,
    "Appended using promise",
    "utf-8",
  );
  const fileContent = await fsPromises.readFile(PROMISE_FILE_PATH, "utf-8");
  const stats = await fsPromises.stat(PROMISE_FILE_PATH);

  return {
    style: "promise",
    fileName: path.basename(PROMISE_FILE_PATH),
    dirName: path.dirname(PROMISE_FILE_PATH),
    sizeInBytes: stats.size,
    content: fileContent,
  };
}

async function main(): Promise<void> {
  try {
    ensureDemoFolderExists();
    // const syncResult = runSyncExample();
    // const callbackResult = await runCallbackExample();
    // const promiseResult = await runPromiseExample();
    // console.log(syncResult);
    // console.log(callbackResult);
    // console.log(promiseResult);
  } catch (error) {
    const message = error instanceof Error ? error.message : "unknown error";
    console.error("File System error", message);
  }
}
// main();

// ASSESSMENTS
// Task 1: Safe Directory Creation with Metadata CheckRequirement
// Implement an asynchronous function verifyAndPrepareDirectory(dirPath).
// It must check if a directory exists using fsPromises.stat().
// If it does not exist, create it recursively using fsPromises.mkdir().
// If it exists but is a file instead of a directory, throw an error.

async function verifyAndPrepareDirectory(dirPath: string): Promise<void> {
  try {
    const pathStats = await fsPromises.stat(dirPath);
    if (!pathStats.isDirectory) {
      throw new Error(
        `Path target exists but is a file, not a directory: ${dirPath}`,
      );
    }
  } catch (error: any) {
    if (error.code === "ENOINT") {
      await fsPromises.mkdir(dirPath);
    } else {
      throw error;
    }
  }
}
// verifyAndPrepareDirectory("file-system/fs-demo/callback-note.txt");

// Task 2: Atomic File Write and Read VerificationRequirement
// Write a function atomicWriteAndRead(filePath, content) using fsPromises.
// Write the text content to the file, and immediately read it back to verify that the file size matches the written string length exactly.
// Return the FileResult payload shape.

async function atomicWriteAndRead(
  filePath: string,
  content: string,
): Promise<FileResult> {
  await fsPromises.writeFile(filePath, content, "utf-8");
  // await fsPromises.appendFile(filePath, "Appended using fsPromises", "utf-8")
  const stats = await fsPromises.stat(filePath);
  const readContent = await fsPromises.readFile(filePath, "utf-8");
  return {
    style: "promise",
    fileName: path.basename(filePath),
    content: readContent,
    dirName: path.dirname(filePath),
    sizeInBytes: stats.size,
  };
}

// Task 3: Converting Legacy Callback File Reader to PromiseRequirement
// Node.js legacy code bases use callback-based fs functions.
// Write a utility function customReadFilePromise(filePath) that wraps the traditional fs.readFile callback function inside a native JavaScript Promise manually without using node:util.

// Utility function - reusable helper function designed to perform specific, common tasks across an application
// The first argument passed into the callback handler following the error-first standard pattern(err, data)=>{} represents the operational error state

function customReaddFilePromise(filePath: string): Promise<string> {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, "utf-8", (err, data) => {
      if (err) {
        return reject(err);
      }
      resolve(data);
    });
  });
}

// Task 4: Content Appender with Automated Pre-cleanupRequirement
// Create a function refreshAndAppendLog(filePath, logMessage) using fsPromises
// If the target log file exists and its size exceeds 1KB (1024 bytes),
// completely wipe the old contents before appending the new logMessage.
// If it is under 1KB, append the message normally.

async function refreshAndAppendLog(
  filePath: string,
  logMessage: string,
): Promise<void> {
  try {
    const stats = await fsPromises.stat(filePath);
    const fileSize = stats.size;
    if (fileSize > 1024) {
      await fsPromises.writeFile(filePath, logMessage, "utf-8");
      await fsPromises.appendFile(filePath, logMessage, "utf-8");
    } else {
      await fsPromises.appendFile(filePath, logMessage, "utf-8");
    }
  } catch (error: any) {
    if (error.code === "ENOINT") {
      console.error(`The filepath ${filePath} does not exist`);
    }
  }
}

async function refreshAndAppendLogg(
  filePath: string,
  logMessage: string,
): Promise<void> {
  try {
    const stats = await fsPromises.stat(filePath);
    if (stats.size > 1024) {
      // Wipes file clean by opening it in write mode with empty string
      await fsPromises.writeFile(filePath, "", "utf-8");
    }
  } catch (error: any) {
    if (error.code !== "ENOENT") throw error;
  }

  await fsPromises.appendFile(filePath, `${logMessage}\n`, "utf-8");
}
// Task 5: Safe Cleanup Routine (File Deletion)Requirement
// Implement a cleanup routine safelyDeleteDemoFiles(filePaths).
// It must accept an array of strings, loop through them, and attempt to delete each file using fsPromises.unlink().
// Ensure that if one file is missing, it does not throw an exception or halt the removal of remaining files.
const filePaths = [];

async function safelyDeleteDemoFiles(filePaths: string[]): Promise<void> {
  for (const filePath of filePaths) {
    try {
      await fsPromises.unlink(filePath);
    } catch (error: any) {
      if (error.code === "ENOINT") {
        console.error(`Failed to delete ${filePath}, it doesn't exist`);
      }
    }
  }
}

// CONCEPTUAL NOTES

// Using synchronous file methods like fs.readFileSync and fs.writeFileSync is strictly discouraged inside
// highly concurrent Node.js production HTTP request handlers because they block the single-threaded Event loop entirely,
// preventing any other concurrent requests from being handled until the file operations complete

// If you call fs.writeFileSync("/path/to/missing-folder/file.txt", "data") when the directory missing-folder does not exist,
// Node.js throws an ENOINT error because the target file system directory path component cannot be found

// path.join() - combines path fragments using the platform-specific delimiter
// path.resolve() - computes an absolute path relative to the current working directory
