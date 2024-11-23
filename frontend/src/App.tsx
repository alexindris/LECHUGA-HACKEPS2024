import React from "react";
import { ApolloProvider } from "@apollo/client";
import { createRouter, RouterProvider } from "@tanstack/react-router";
import { routeTree } from "./routeTree.gen";
import { AppStoreProvider } from "./stores/storeProvider";
import { apolloClient } from './lib/utils';


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
      <ApolloProvider client={apolloClient}>
        <AppStoreProvider>
          <RouterProvider router={router} />
        </AppStoreProvider>
      </ApolloProvider>
    </React.StrictMode>
  );
};
