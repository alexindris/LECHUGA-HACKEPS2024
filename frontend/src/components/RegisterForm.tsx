import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardHeader,
} from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Link, useNavigate } from "@tanstack/react-router";
import { useForm } from "react-hook-form";
import { z } from "zod";
import { zodResolver } from "@hookform/resolvers/zod";
import {
  Form,
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "./ui/form";
import { useState } from 'react';
import { ErrorMessage } from './ErrorMessage';
import { registerSchema } from '@/formSchemas/signupSchema';
import { Checkbox } from './ui/checkbox';
import { CREATE_USER } from '@/lib/api';
import { apolloClient } from '@/lib/utils';


export function RegisterForm() {
  const form = useForm<z.infer<typeof registerSchema>>({
    resolver: zodResolver(registerSchema),
    defaultValues: {
      name: "",
      email: "",
      password: "",
      confirmPassword: "",
      terms: false,
    },
  });

  const navigate = useNavigate();
  const [errorMessage, setErrorMessage] = useState<string | null>(null);

  async function onSubmit(values: z.infer<typeof registerSchema>) {
    try {
      await apolloClient.mutate({
        mutation: CREATE_USER,
        variables: { email: values.email, name: values.name, password: values.password },
      });
      navigate({ to: '/auth/signin' })
    } catch (e: any) {
      return setErrorMessage(e.message)
    }

  }

  return (
    <Card className='mx-auto max-w-sm border-none shadow-none'>
      <CardHeader>
        <img src='/app_logo.png' alt='logo' />
      </CardHeader>
      <CardContent>
        <ErrorMessage errorMessage={errorMessage} />
        <Form {...form}>
          <form onSubmit={form.handleSubmit(onSubmit)}>
            <div className='grid gap-4 items-center'>
              <FormField
                control={form.control}
                name='name'
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>Name</FormLabel>
                    <FormControl>
                      <Input {...field} placeholder='Name' />
                    </FormControl>
                    <FormDescription className='text-slate-500'>Enter your name</FormDescription>
                    <FormMessage className='text-red-500' />
                  </FormItem>
                )}
              />
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
              <FormField
                control={form.control}
                name='password'
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>Password</FormLabel>
                    <FormControl>
                      <Input {...field} type='password' placeholder='Password' />
                    </FormControl>
                    <FormDescription className='text-slate-500'>Enter your password</FormDescription>
                    <FormMessage className='text-red-500' />
                  </FormItem>
                )}
              />
              <FormField
                control={form.control}
                name='confirmPassword'
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>Confirm password</FormLabel>
                    <FormControl>
                      <Input {...field} type='password' placeholder='Confirm password' />
                    </FormControl>
                    <FormDescription className='text-slate-500'>Confirm your password</FormDescription>
                    <FormMessage className='text-red-500' />
                  </FormItem>
                )}
              />
              <FormField
                control={form.control}
                name='terms'
                render={({ field }) => (
                  <FormItem >
                    <FormControl>
                      <Checkbox
                        checked={field.value}
                        onCheckedChange={field.onChange}
                        className='bg-white mr-2'
                      />
                    </FormControl>
                    <FormLabel>Accept terms and conditions</FormLabel>
                    <FormMessage className='text-red-500' />
                  </FormItem>
                )}
              />
              <div className='w-full items-center justify-center flex'>
                <Button type='submit' className='w-fit'>
                  Continue
                </Button>
              </div>
            </div>
            <div className='mt-4 text-center text-sm'>
              Do you have an account?{' '}
              <Link to='/auth/signin' className='underline'>
                Sign in
              </Link>
            </div>
          </form>
        </Form>
      </CardContent>
    </Card>
  );
}
