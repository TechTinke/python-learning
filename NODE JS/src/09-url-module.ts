// url module - helps us deal with URLs safely
// https://api.example.com/users?page=2&limit=10

function runUrlDemo(): void {
  // Creating a URL object from a URL string
  const apiUrl = new URL(
    "https://api.pixietechnologies/users?page=2&limit=10&sort=latest",
  );

  //   console.log(apiUrl.href);
  //   console.log(apiUrl.protocol);
  //   console.log(apiUrl.hostname);
  //   console.log(apiUrl.search);
  //   console.log(apiUrl.pathname);
  //   console.log(apiUrl.searchParams);

  // ? - query parameters
  // searchParams - read query parameters
  const page = apiUrl.searchParams.get("page");
  const limit = apiUrl.searchParams.get("limit");
  const sort = apiUrl.searchParams.get("sort");
  console.log(page, limit, sort);

  // .set - update query parameters
  apiUrl.searchParams.set("page", "10");
  apiUrl.searchParams.set("limit", "20");
  console.log(apiUrl.href);

  // creating a searchParam which you can append to your URL
  const queryParams = new URLSearchParams({
    search: "node js",
    page: "1",
    limit: "5",
  });
  console.log(queryParams.toString());
}
runUrlDemo();
