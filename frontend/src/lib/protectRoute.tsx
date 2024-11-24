// src/utils/protectRoute.ts
import {
  createFileRoute,
  FileRoutesByPath,
  redirect,
} from "@tanstack/react-router";
import React from "react";


function isLoggedIn() {
  const auth = localStorage.getItem('auth')
  return !!auth
}


// Keep any existing beforeLoad logic
type ProtectedRouteOptions = {
  path: keyof FileRoutesByPath;
  component: React.FC;
};

export function createProtectRoute({ path, component }: ProtectedRouteOptions) {
  return createFileRoute(path)({
    component: component,
    beforeLoad: async ({ location }) => {
      if (!isLoggedIn()) {
        throw redirect({
          to: "/auth/signin",
          search: {
            redirect: location.href,
          },
        });
      }
    },
  });
}

export function createNonLoggedRoute({ path, component }: ProtectedRouteOptions) {
  return createFileRoute(path)({
    component: component,
    beforeLoad: async ({ location }) => {
      if (isLoggedIn()) {
        throw redirect({
          to: "/home",
          search: {
            redirect: location.href,
          },
        });
      }
    },
  });
}
