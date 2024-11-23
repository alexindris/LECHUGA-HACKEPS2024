import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Link, useNavigate } from "@tanstack/react-router";
import { useForm } from "react-hook-form";
import { z } from "zod";
import { zodResolver } from "@hookform/resolvers/zod";
import { loginSchema } from "@/formSchemas/loginSchema";
import {
  Form,
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "./ui/form";
import { useUserStore } from '@/stores/storeProvider';
import { useState } from 'react';
import { ErrorMessage } from './ErrorMessage';
import Cookies from 'js-cookie';

export function LoginForm() {
  const form = useForm<z.infer<typeof loginSchema>>({
    resolver: zodResolver(loginSchema),
    defaultValues: {
      email: "",
      password: "",
    },
  });

  const navigate = useNavigate();
  const userStore = useUserStore();
  const [errorMessage, setErrorMessage] = useState<string | null>(null);

  async function onSubmit(values: z.infer<typeof loginSchema>) {
    const a = await userStore.login(values.email, values.password);
    if (a.token) {
      Cookies.set('auth', a.token);
      navigate({ to: '/me' })
    }
    else if (a?.errorMessage) setErrorMessage(a.errorMessage);
    else setErrorMessage('Unknown error')
  }

  return (
    <Card className='mx-auto max-w-sm border-none shadow-none'>
      <CardHeader>

        <img src='/public/app_logo.png' alt='logo' />
      </CardHeader>
      <CardContent>
        <ErrorMessage errorMessage={errorMessage} />
        <Form {...form}>
          <form onSubmit={form.handleSubmit(onSubmit)}>
            <div className='grid gap-4 items-center'>
              <div className='grid gap-2'>
                <FormField
                  control={form.control}
                  name='email'
                  render={({ field }) => (
                    <FormItem>
                      <FormLabel>Email</FormLabel>
                      <FormControl>
                        <Input {...field} placeholder='Email' />
                      </FormControl>
                      <FormDescription className='text-slate-500'>Enter your email address</FormDescription>
                      <FormMessage className='text-red-500' />
                    </FormItem>
                  )}
                />
              </div>
              <div className='grid gap-2'>
                <FormField
                  control={form.control}
                  name='password'
                  render={({ field }) => (
                    <FormItem>
                      <FormLabel>Password</FormLabel>
                      <FormControl>
                        <Input {...field} type='password' />
                      </FormControl>
                      <FormDescription className='text-slate-500'>Enter your password</FormDescription>
                      <FormMessage className='text-red-500' />
                    </FormItem>
                  )}
                />
              </div>
              <div className='w-full items-center justify-center flex'>
                <Button type='submit' className='w-fit'>
                  Continue
                </Button>
              </div>

            </div>
            <div className='mt-4 text-center text-sm'>
              Don&apos;t have an account?{" "}
              <Link href='#' className='underline'>
                Sign up
              </Link>
            </div>
          </form>
        </Form>
      </CardContent>
    </Card>
  );
}
