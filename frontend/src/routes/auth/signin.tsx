import { createFileRoute } from "@tanstack/react-router";
import { LoginForm } from "@/components/LoginForm";

export const Route = createFileRoute("/auth/signin")({
  component: RouteComponent,
});

function RouteComponent() {
  return (
    <div className='flex h-screen w-full items-center justify-center px-4'>
      <LoginForm />
    </div>
  );
}
