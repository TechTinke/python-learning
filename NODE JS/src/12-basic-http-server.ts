import http, { IncomingMessage, ServerResponse } from "node:http";

const PORT = 3000;

// http.createServer() - used for creating low level http servers
// The callback, req: IncomingMessage, res: ServerResponse)=>{}, runs for every incoming http request

const server = http.createServer(
  (req: IncomingMessage, res: ServerResponse) => {
    // req -> request object

    // 1. req.method - method that we are using (get, post, put, options, delete)
    const method = req.method
    // 1. get - read data
    // 2. post - create/write data
    // 3. put - replace data
    // 4. patch - update partial data
    // 5. delete - delete data

    // 2. req.url? - url path that the client is actually requesting(/users, /shopping-cart)
    const url = req.url

    // http://localhost:5000/users --> /users - the url

    // 3. req.headers - actual metadata sent by client
    // - Extra infromation that we send along with our request (browser type, authorization token, content type(JSON, normal text))
    const userAgent = req.headers["user-agent"]

    // 4. req body -> data

    // res -> response object
    // - Sending something back to the client

    // 1. status code
    res.statusCode = 200 // setting the http status code
    // 200, 429, 400, 401
    // Diff status codes are used in a certain position or situation to represent something

    // 2. response headers
    res.setHeader("Content-Type", "text/plain")
    // res.setHeader("Content-Type", "application/json")
    
    // 3. response body

    res.end(`Basic http node server: ${method} : ${url} : ${userAgent}`) //end the response
  },
);

server.listen(PORT, () =>{
  console.log(`Server is now running on port ${PORT}`);
})// server has to listen to that particular port in order for a request to start and get a response back
