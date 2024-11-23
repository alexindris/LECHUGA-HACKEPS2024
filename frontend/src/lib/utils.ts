import { ApolloClient, InMemoryCache, NormalizedCache, NormalizedCacheObject } from '@apollo/client';
import { clsx, type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}


// const authLink = setContext((_, { headers }) => {
//   // get the authentication token from local storage if it exists
//   const token = localStorage.getItem('token');
//   // return the headers to the context so httpLink can read them
//   return {
//     headers: {
//       ...headers,
//       authorization: token ? `Bearer ${token}` : "",
//     }
//   }
// });


// Initialize Apollo Client
export const apolloClient = new ApolloClient({
  uri: "http://localhost:8000/graphql/",
  cache: new InMemoryCache(),
});

// export class CustomApolloClient {

//   client: ApolloClient<NormalizedCacheObject>;

//   constructor() {
//     this.client = new ApolloClient({
//       uri: "http://localhost:8000/graphql/",
//       cache: new InMemoryCache(),
//     });
//   }

//   public addAuthToken(token: string) {
//     this.client.setHeaders({
//       authorization: token
//     });
//   }
// }