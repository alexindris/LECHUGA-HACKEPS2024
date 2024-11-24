import { ApolloClient, createHttpLink, InMemoryCache } from '@apollo/client';
import { clsx, type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";
import { setContext } from '@apollo/client/link/context';

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

const httpLink = createHttpLink({
  // uri: 'http://localhost:8000/graphql/',
  uri: "https://engiei3g8t.eu-west-3.awsapprunner.com/graphql/ "
});

const authLink = setContext((_, { headers }) => {
  const token = localStorage.getItem('auth');
  console.log(token)
  return {
    headers: {
      ...headers,
      Authorization: token ? `Token ${token}` : "",
    }
  }
});

export const apolloClient = new ApolloClient({
  link: authLink.concat(httpLink),
  cache: new InMemoryCache()
});
