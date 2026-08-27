import http, { IncomingMessage, ServerResponse } from "node:http";

const PORT = 5000;

const server = http.createServer(
  (req: IncomingMessage, res: ServerResponse) => {
    const method = req.method ?? "GET";
    const requestUrl = new URL(req.url ?? "/", `http:${req.headers.host}`);
    const pathName = requestUrl.pathname;

    res.setHeader("Content-Type", "text/plain");

    if (method === "GET" && pathName === "/health") {
      res.statusCode = 200;
      res.end("Server is healthy; up and running");
      return;
    }
    res.statusCode = 404;
    res.end("Route not found");
  },
);

server.listen(PORT, () => {
  console.log(`Server is now running on ${PORT}`);
});
