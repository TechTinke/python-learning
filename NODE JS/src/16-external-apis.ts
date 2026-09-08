// Web Scraping

import { time } from "node:console";

const API_URL = "https://jsonplaceholder.typicode.com/users/1";

// Data Transformation
// data format of the external api that we're fetching data from
type PlaceholderUser = {
  id: number;
  name: string;
  email: string;
  company: {
    name: string;
  };
};

// data format of the application that is being built
type PublicUser = {
  id: number;
  name: string;
  email: string;
  company: string;
};

// Data Transformation
function transformUser(rawData: PlaceholderUser): PublicUser {
  return {
    id: rawData.id,
    name: rawData.name,
    email: rawData.email,
    company: rawData.company.name,
  };
}

async function fetchExternalUser(): Promise<void> {
  // AbortController - cancel an ongoing request in a case scenario like when there is no data that is returned which in the case of a fetch it would not be possible
  //CASE SCENARIOS THAT WOULDC AUSE AN EXTERNAL API TO FAIL
  // 1.Network Instability
  // 2.Unannounced breaking schema
  // 3.Rate Limiter
  const controller = new AbortController();
  const timeOut = setTimeout(() => {
    controller.abort();
  }, 5000);

  try {
    const response = await fetch(API_URL, {
      method: "GET",
      signal: controller.signal, //connect the request to the contoller
    });

    if (!response.ok) {
      console.error(`Upstream API failed with http ${response.status}`);
      return;
    }

    const rawUser = (await response.json()) as PlaceholderUser;

    const user = transformUser(rawUser);
    console.log(user);
  } catch (error) {
    if (error instanceof Error && error.name === "AbortError") {
      console.error("Request failed - Response time was too long");
      return;
    }
    const messagee = error instanceof Error ? error.message : "unknown error";
    console.error("External API failed", messagee);
  } finally {
    clearTimeout(timeOut);
  }
}
fetchExternalUser();
