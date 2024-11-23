import React from "react";
import { ApolloClient, ApolloProvider, InMemoryCache } from "@apollo/client";
import { createRouter, RouterProvider } from "@tanstack/react-router";
import { routeTree } from "./routeTree.gen";
import { CounterStoreProvider } from "./stores/storeProvider";

// Initialize Apollo Client
const client = new ApolloClient({
  uri: "http://localhost:8000/graphql/",
  cache: new InMemoryCache(),
});

// Set up the router
const router = createRouter({
  routeTree,
  defaultPreload: "intent",
});

// Register types for TanStack Router
declare module "@tanstack/react-router" {
  interface Register {
    router: typeof router;
  }
}

export const App = () => {
  return (
    <React.StrictMode>
      <ApolloProvider client={client}>
        <CounterStoreProvider>
          <RouterProvider router={router} />
        </CounterStoreProvider>
      </ApolloProvider>
    </React.StrictMode>
  );
};
