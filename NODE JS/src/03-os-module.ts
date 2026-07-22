import { log } from "node:console";
import * as os from "node:os";

// - Different information related to operating system
// os information
// cpu information
// memory information
// home directory
// os type

function runOsDemo(): void {
  console.log("platform", os.platform()); //platform
  console.log("architecture", os.arch()); //architecture
  console.log("os type", os.type()); // type
  console.log("os release", os.release()); // version release
  console.log("home directory", os.homedir()); // home directory
  console.log("temp directory", os.tmpdir()); // template directory

  // CPU information
  const cpus = os.cpus();
  console.log(cpus.length);

  if (cpus.length > 0) {
    console.log("First CPU Model", cpus[0].model, cpus[0].speed, cpus[0].times);
  }

  //Memory Information
  console.log(os.totalmem(), os.freemem());
}
runOsDemo();
