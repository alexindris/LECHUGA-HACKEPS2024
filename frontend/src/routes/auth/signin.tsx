import { LoginForm } from "@/components/LoginForm";
import { createNonLoggedRoute } from '@/lib/protectRoute';

export const Route = createNonLoggedRoute({
  path: "/auth/signin",
  component: RouteComponent,
});

function RouteComponent() {
  return (
    <div className='flex h-screen w-full items-center justify-center px-4 bg-sky-100'>
      <LoginForm />
    </div>
  );
}
