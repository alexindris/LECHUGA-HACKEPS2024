// src/utils/protectRoute.ts
import {
  createFileRoute,
  FileRoutesByPath,
  redirect,
} from "@tanstack/react-router";
import React from "react";

// Keep any existing beforeLoad logic
type ProtectedRouteOptions = {
  path: keyof FileRoutesByPath;
  component: React.FC;
};

export function createProtectRoute({ path, component }: ProtectedRouteOptions) {
  return createFileRoute(path)({
    component: component,
    beforeLoad: async ({ location }) => {
      // if (!isAuthenticated()) {
      if (true) {
        throw redirect({
          to: "/auth/signin",
          search: {
            // Use the current location to power a redirect after login
            // (Do not use `router.state.resolvedLocation` as it can
            // potentially lag behind the actual current location)
            redirect: location.href,
          },
        });
      }
    },
  });
}
