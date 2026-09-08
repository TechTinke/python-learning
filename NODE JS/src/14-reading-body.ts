import { resolveSoa } from "node:dns";
import http, { IncomingMessage, ServerResponse } from "node:http";
const PORT = 5001;
type createUserBody = {
  name: string;
  email: string;
};

// creating a web server object
const server = http.createServer(
  (req: IncomingMessage, res: ServerResponse) => {
    const method = req.method ?? "POST";
    const requestUrl = new URL(req.url ?? "/", `http:${req.headers.host}`);
    const pathName = requestUrl.pathname;
    res.setHeader("Content-Type", "text/plain");

    if (method === "POST" && pathName == "/users") {
      const chunks: Buffer[] = [];
      const chunksss: Buffer[] = [];

      // data event is going to run everytime node receives a new body chunk
      // The chunk emitted in each "data" event is a Buffer

      // If it's going to be string data, the best thing is to collect the data in an array then at "end", concatenate it and stringify it
      req.on("data", (chunk: Buffer) => {
        chunks.push(chunk);
      });
      req.on("end", () => {
        try {
          const rawBody = Buffer.concat(chunks).toString("utf-8");
          // const rawBodyBuffer = Buffer.concat(chunks);
          // console.log(rawBodyBuffer);

          if (!rawBody) {
            res.statusCode = 404;
            res.end("Empty request body");
            return;
          }

          const body = JSON.parse(rawBody) as createUserBody;

          if (!body.name || !body.email) {
            res.statusCode = 404;
            res.end("Both name and email is required");
            return;
          }
          res.statusCode = 201;
          res.end(`User created successfully ${body.name}, ${body.email}`);
        } catch {
          res.statusCode = 400;
          res.end("Invalid json body");
          return;
        }
      });
      // Listener for the "error" event emitted on the request stream so that the error is not thrown and cause the program to crash
      req.on("error", () => {
        res.statusCode = 500;
        res.end("Failed to read request body");
        return;
      });
    }
    // res.statusCode = 404;
    // res.end("Route not found");
    // return;
  },
);

server.listen(PORT, () => {
  console.log(`Server is up and running at port ${PORT}`);
});
