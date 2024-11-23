import { ApolloClient, InMemoryCache } from '@apollo/client';
import { clsx, type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

// Initialize Apollo Client
export const apolloClient = new ApolloClient({
  uri: "http://localhost:8000/graphql/",
  cache: new InMemoryCache(),
});