import { RegisterForm } from '@/components/RegisterForm';
import { createNonLoggedRoute } from '@/lib/protectRoute';

export const Route = createNonLoggedRoute({
  path: "/auth/signup",
  component: RouteComponent,
});

function RouteComponent() {
  return (
    <div className='flescreen w-full items-center justify-center px-4 bg-sky-100'>
      <RegisterForm />
    </div>
  );
}
