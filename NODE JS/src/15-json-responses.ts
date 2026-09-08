import http, { IncomingMessage, ServerResponse } from "node:http";

const PORT = 5002;

type User = {
  id: number;
  name: string;
  email: string;
};
type apiResponse<T> = {
  success: boolean;
  message: string;
  data?: T;
  error?: string;
};

const users: User[] = [
  { id: 1, name: "Sangam", email: "sangam@gmail.com" },
  { id: 2, name: "Rahul", email: "rahul@gmail.com" },
];

function sendJson<T>(
  res: ServerResponse,
  statusCode: number,
  body: apiResponse<T>,
): void {
  res.statusCode = statusCode;
  res.setHeader("Content-Type", "application/json"); //content type for request body
  res.end(JSON.stringify(body));
}

const server = http.createServer(
  (req: IncomingMessage, res: ServerResponse) => {
    // The function that's passed into createServer runs once for every http request that is made against that server - request handler
    // req object - Readable Stream
    // res object - Writable Stream

    const method = req.method ?? "GET";
    const requestUrl = new URL(req.url ?? "/", `http:${req.headers.host}`);
    const pathName = requestUrl.pathname;
    res.setHeader("Content-Type", "text/plain");

    if (method === "GET" && pathName === "/users") {
      sendJson(res, 200, {
        success: true,
        message: "Users fetched successfully",
        data: users,
      });
      return;
    }

    sendJson<null>(res, 404, {
      success: false,
      message: "Route not found",
      error: `${method} ${pathName} does not exist`,
    });
  },
);

server.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

// import http from "node:http";

// http
//   .createServer((request, response) => {
//     if (request.method === "POST" && request.url === "/echo") {
//       request.pipe(response);
//     } else {
//       response.statusCode = 404;
//       response.end();
//     }
//   })
//   .listen(8080);

// DELIVERABLES
// Instantiate an HTTP server with a request handler function, and have it listen on a port.
// Get headers, URL, method and body data from request objects.
// Make routing decisions based on URL and/or other data in request objects.
// Send headers, HTTP status codes and body data via response objects.
// Handle stream errors in both the request and response streams.
