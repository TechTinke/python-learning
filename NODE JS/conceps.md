## node js - JS runtime(environment where you run some code)

- JS runs outside of the browser(on the computer or on a server)

- Node Js uses V8(same engine that Google Chrome uses) - takes Javascript and runs it on your machine

## npm - node package manager

- Helps you run package scripts
- Helps you install various packages
- Manage dependencies

## dependencies / runtime package

- Needed when the app is running e.g Express
- something your code imports and uses while doing an actual work and the app can fail or crash when they are missing

## devdependencies

- Needed while developing or building
- Something you use to write, compile or check code but not but not something that you need while running that particular code in production

# folder, file -> holding any responsibility

utils -> can't hold any routing
mixing -> service logic and db repository(db patterns - which files you are going to do your db queries) which is a bad practise
routing -> can't handle service logic - bad practise

- Always have one entry/root file and should contai information of your entire source code

## CORE MODULES

- process object
- path module
- file system module
- event loop basics
- callback promise async/await (IQ)
- event emitter
- buffers
- crypto module
- error handling
- streams
