import { createProtectRoute } from "@/lib/protectRoute";

export const Route = createProtectRoute({
  path: "/me",
  component: RouteComponent,
});

function RouteComponent() {
  return "Hello /me!";
}
