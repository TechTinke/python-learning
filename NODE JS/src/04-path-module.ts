// Build and read file paths
import { log } from "node:console";
import path from "node:path";

//const filePath = projectRoot + "/uploads" + filename - bad practise

// path.join()
// - Uses the correct separator for the current os because there are different separators for diff versions of os

// C:\Users\25474\OneDrive\Pictures\Screenshots - Windows
// Users/username/Pictures/Screenshots - macOS
// /home/username/Pictures/Screenshots - linux

process.cwd(); // the folder in which NodeJS was started
const projectRoot = process.cwd();
console.log(projectRoot);

// HYPOTHETICAL EXAMPLE
// A user uploads a file and the file is to be stored in this designated location(/uploads/users/67/profile_photo.png)
const userId = "42";
const originalName = "profile_photo.png";

// NOTE: path.join() creates a path string and not the actual folder itself
// - It does not check whether the file exists or not

const uploadFilePath = path.join(
  projectRoot,
  "uploads",
  "users",
  userId,
  originalName,
);
console.log(uploadFilePath);

const fileName = path.basename(uploadFilePath); // - final part of a path(file name)
const fileExt = path.extname(uploadFilePath); // - extension of file name
const parentFolder = path.dirname(uploadFilePath); // - directory path to file name
console.log(fileName);
console.log(fileExt);
console.log(parentFolder);
