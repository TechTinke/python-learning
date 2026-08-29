import { error } from "node:console";
import http, { IncomingMessage, ServerResponse } from "node:http";
import { url } from "node:inspector";

// const PORT = 5000;

// const server = http.createServer(
//   (req: IncomingMessage, res: ServerResponse) => {
//     const method = req.method ?? "GET";
//     const requestUrl = new URL(req.url ?? "/", `http:${req.headers.host}`);
//     const pathName = requestUrl.pathname;
//     res.setHeader("Content-Type", "text/plain");

//     if (method === "GET" && pathName === "/health") {
//       res.statusCode = 200;
//       res.end("Server is healthy; up and running");
//       return;
//     }
//     res.statusCode = 404;
//     if (method == "GET" && pathName === "/users") {
//       res.statusCode = 200;
//       res.end("LIST OF USERS");
//       return;
//     }
//     res.end("Route not found");
//   },
// );

// server.listen(PORT, () => {
//   console.log(`Server is now running on ${PORT}`);
// });

//ASSSESSMENT TASKS
// Task 1: Route Fix and Early Return Refactoring
// Requirement: The /users route in your current boilerplate contains a critical bug
// it hits res.statusCode = 404 before evaluating the condition, causing mixed signaling.
// Refactor the code block into a clean, early-return conditional structure that fixes this bug and adds an exact match for a POST /users endpoint.

const PORT1 = 5000;

const server1 = http.createServer(
  (req: IncomingMessage, res: ServerResponse) => {
    const method = req.method ?? "GET";
    const requestUrl = new URL(req.url ?? "/", `http:${req.headers.host}`);
    const pathName = requestUrl.pathname;
    res.setHeader("Content-Type", "text/plain");

    if (method === "GET" && pathName === "/users") {
      res.statusCode = 200;
      res.end("List of users has been fectched successfully");
      return;
    }

    if (method === "GET" && pathName === "/health") {
      res.statusCode = 200;
      res.end(JSON.stringify({ message: "Route found" }));
      return;
    }

    if (method === "POST" && pathName === "/users") {
      res.statusCode = 200;
      res.end(JSON.stringify({ message: "LIST OF USERS" }));
    }

    res.statusCode = 404;
    res.end(JSON.stringify({ error: "Route not found" }));
  },
);

server1.listen(PORT1, () => {
  console.log(`Server 1 is up and running and port ${PORT1}`);
});

// Task 2: Query Parameter Extraction RoutingRequirement
// Implement a search feature on the GET /users route.
// Extract a role query parameter (e.g., /users?role=super-admin) using the native URLSearchParams API.
// If the parameter exists, print a custom message identifying the filtered role.

const PORT2 = 5001;
const server2 = http.createServer(
  (req: IncomingMessage, res: ServerResponse) => {
    const method = req.method ?? "GET";
    const requestUrl = new URL(req.url ?? "/", `http:${req.headers.host}`);
    const pathName = requestUrl.pathname;
    const role = requestUrl.searchParams.get("role");
    res.setHeader("Content-Type", "text/plain");

    if (method === "GET" && pathName === "/users") {
      const role = requestUrl.searchParams.get("role");
      res.statusCode = 200;
      if (role) {
        res.end(`Users filtered by role: ${role}`);
      }
      res.end("LIST OF USERS");
    }
    res.statusCode = 404;
    res.end("Route dies not exist");
  },
);

server2.listen(PORT2, () => {
  console.log(`Server 2 is up and runnign at port ${PORT2}`);
});
