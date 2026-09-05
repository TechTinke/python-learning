import { error } from "node:console";
import http, { IncomingMessage, Server, ServerResponse } from "node:http";
import { url } from "node:inspector";

const PORT = 5000;

const server = http.createServer(
  (req: IncomingMessage, res: ServerResponse) => {
    const method = req.method ?? "GET";
    const requestUrl = new URL(req.url ?? "/", `http:${req.headers.host}`);
    const requestUrl2 = new URL(req.url ?? "http://" + req.headers.host);
    // -> It is critical to use the nullish coalescing operator before initializing a URL inspector constructor
    // because the req.url attribute on Incoming message is typed as optional and could theoretically be undefined,because of some network connection edge cases, which would break the URL constuctor.
    // The fallback ensures the URL constrcutor receives a valid path string

    // -> req.headers.host extracts the target domain name or port location from the incoming client request headers to dynamically construct a valid URL origin.

    // -> The second base host argument is included because the standard global browser compatible URL constructor
    // throws a runtime error if passed a relative path reference (like /users) without an absolute path origin
    const pathName = requestUrl.pathname;
    res.setHeader("Content-Type", "text/plain");

    if (method === "GET" && pathName === "/health") {
      res.statusCode = 200;
      res.end("Server is healthy; up and running");
      return;
    }

    if (method == "GET" && pathName === "/users") {
      res.statusCode = 200;
      res.end("LIST OF USERS");
      return;
    }

    // if (method === "GET" && pathName === "/health") {
    //   res.statusCode = 200;
    //   res.end("OK");
    // }
    // res.statusCode = 404;
    // res.end("Not Found");

    // Without an early return, code execution continues. The server writes the "OK" stream payload,
    //  but because there is no return statement, it continues executing and invokes res.end("Not Found") causing an ERR_STREAM_WRITE_AFTER_END node exception error

    res.statusCode = 404;
    // -> statusCode 404 means that the server successfully parsed the request destination, but could not map it to an active endpoint matching the requested path or HTTP verb
    res.end("Route not found");
  },
);

server.listen(PORT, () => {
  console.log(`Server is now running on ${PORT}`);
});

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

// server1.listen(PORT1, () => {
//   console.log(`Server 1 is up and running and port ${PORT1}`);
// });

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
    res.end("Route does not exist");
  },
);

// server2.listen(PORT2, () => {
//   console.log(`Server 2 is up and runnign at port ${PORT2}`);
// });

// Task 3: Dynamic Route Parameter Matching (Regex Pattern)
// Requirement: In production, routes often contain dynamic IDs (e.g., /users/3).
// Implement a router segment that intercepts GET /users/:id using a regular expression match.
// Extract the exact numeric ID string out of the URL path name and return it in the response.

const PORT3 = 5002;
const server3 = http.createServer(
  (req: IncomingMessage, res: ServerResponse) => {
    const method = req.method ?? "GET";
    const requestUrl = new URL(req.url ?? "/", `http:${req.headers.host}`);
    const urlPathName = requestUrl.pathname;
    const userMatch = urlPathName.match(/^\/users\/(\d+)$/); // Route Parameter
    // -> Route Parameters - represent distinct embedded variable placeholdrs inside the structural path layout itself(e.g /users/:id)
    // -> Query Parameters - key value string blocks appended behind a path delimiter(e.g ?id=3)
    res.setHeader("Content-Type", "text/plain");

    if (method === "GET" && userMatch) {
      const userId = userMatch[1];
      res.statusCode = 200;
      res.end(`FETCHING DATA FOR USER ID: ${userId}`);
      return;
    }
    res.statusCode = 404;
    res.end("Route does not exist");
  },
);
// server3.listen(PORT3, () => {
//   console.log(`Server 3 is running at port ${PORT3}`);
// });

// Task 4: Parsing JSON Request Bodies inside a Route
// Requirement: Write the data aggregation stream logic needed to read incoming payload data for the POST /users route.
// Because Node.js handles requests as raw data streams, you must capture incoming chunks, assemble them, parse the JSON body, and return a personalized success message.

const PORT4 = 5003;

type UserRegisterPayload = {
  name: number;
  email: string;
  address: string;
};

const server4 = http.createServer(
  (req: IncomingMessage, res: ServerResponse) => {
    const method = req.method ?? "POST";
    const requestUrl = new URL(req.url ?? "/", `${req.headers.host}`);
    const requestPathName = requestUrl.pathname;

    if (method === "POST" && requestPathName === "/users") {
      const chunks: Buffer[] = [];

      req.on("data", (chunk: Buffer) => {
        chunks.push(chunk);
      });
      req.on("end", () => {
        try {
          const rawBody = Buffer.concat(chunks).toString("utf-8");

          if (!rawBody) {
            res.statusCode = 400;
            res.end("Empty request body");
            return;
          }

          const body = JSON.parse(rawBody) as UserRegisterPayload;

          if (!body.name || !body.email) {
            res.statusCode = 400;
            res.end("Both name and address are required");
          }
          res.statusCode = 201;
          res.end(
            `User created successfully: ${body.name}, ${body.email}, ${body.address}`,
          );
        } catch {
          res.statusCode = 400;
          res.end("Invalid JSON body");
          return;
        }
      });
      req.on("error", () => {
        res.statusCode = 500;
        res.end("Failed to read request body");
        return;
      });
    }
    res.statusCode = 404;
    res.end(`The path ${requestUrl} does not exist`);
  },
);

// server4.listen(PORT4, () => {
//   console.log(`Server 4 is running on port ${PORT4}`);
// });

// DOESN'T WORK PROPERLY

// Task 5: Centralized Router Registry Refactoring
// Requirement: As routing blocks expand, conditional if/else statements become difficult to maintain.
// Refactor your server code to map string keys (METHOD /path) directly to target handler execution functions stored inside an object registry.

const PORT5 = 5004;
type Handler = (req: IncomingMessage, res: ServerResponse) => void;

const routesRegistry: Record<string, Handler> = {
  "GET /health": (req, res) => {
    res.statusCode = 200;
    res.end("Healthy Registry");
  },
  "GET /users": (req, res) => {
    res.statusCode = 200;
    res.end("Users Registry");
  },
};

const server5 = http.createServer(
  (req: IncomingMessage, res: ServerResponse) => {
    const method = req.method ?? "GET";
    const requestUrl = new URL(req.url ?? "/", `${req.headers.host}`);
    const pathName = requestUrl.pathname;

    const routeLookupKey = `${method} ${pathName}`;
    const executionTarget = routesRegistry[routeLookupKey];

    if (executionTarget) {
      executionTarget(req, res);
    } else {
      res.statusCode = 404;
      res.end("Route Registry Location Missing");
      return;
    }
  },
);

server5.listen(PORT5, () => {});

// NB: Frameworks like Express provide routing wrappers instead of using native http.createServer blocks inside high-scale production systems
// because Native modules lack abstract built-in middleware cascading engines, making complex route parameter extraction and ayload pre-parsing code repetitive
