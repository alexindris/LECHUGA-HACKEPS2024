import { createProtectRoute } from "@/lib/protectRoute";
import { ErrorMessage } from '@/components/ErrorMessage';
import SimpleNav from '@/components/SimpleNav'
import { Button } from '@/components/ui/button';
import { Card, CardContent, CardTitle } from '@/components/ui/card'
import { Form, FormControl, FormField, FormItem, FormLabel, FormMessage } from '@/components/ui/form';
import { Input } from '@/components/ui/input';
import { createParkingSchema } from '@/formSchemas/createParkingSchema';
import { useParkingStore } from '@/stores/storeProvider';
import { zodResolver } from '@hookform/resolvers/zod';
import { useNavigate } from '@tanstack/react-router'
import { useState } from 'react';
import { useForm } from 'react-hook-form';
import { z } from 'zod';

export const Route = createProtectRoute({
  path: "/me",
  component: RouteComponent,
});

function RouteComponent() {
  const form = useForm<z.infer<typeof createParkingSchema>>({
    resolver: zodResolver(createParkingSchema),
    defaultValues: {
      address: "",
      name: "",
      totalLots: 0,
    },
  });

  const [errorMessage, setErrorMessage] = useState<string | null>(null);

  const parkingStore = useParkingStore();

  const navigator = useNavigate();

  async function onSubmit(values: z.infer<typeof createParkingSchema>) {
    const response = await parkingStore.createParking(values.name, values.address, values.totalLots);
    if (!response?.error) navigator({ to: '/home' })
    setErrorMessage("Check the address")
  }


  return (
    <>
      <SimpleNav disabledParkingTab={false} activeTab='parking' />
      <div className='flex flex-col h-screen w-full bg-sky-700 items-center justify-center'>
        <Card className='mx-auto border-none shadow-none bg-sky-100 rounded-[4.25rem] px-32 ' >
          <CardTitle>
            <img src="/parking.png" alt="Parking" className='p-2' />
          </CardTitle>
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
                        <FormMessage className='text-red-500' />
                      </FormItem>
                    )}
                  />
                  <FormField
                    control={form.control}
                    name='address'
                    render={({ field }) => (
                      <FormItem>
                        <FormLabel>Address</FormLabel>
                        <FormControl>
                          <Input {...field} placeholder='Address' />
                        </FormControl>
                        <FormMessage className='text-red-500' />
                      </FormItem>
                    )}
                  />
                  <FormField
                    control={form.control}
                    name='totalLots'
                    render={({ field }) => (
                      <FormItem>
                        <FormLabel>Total Lots</FormLabel>
                        <FormControl>
                          <Input {...field} placeholder='Total lots' type='number' />
                        </FormControl>
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
              </form>
            </Form>
          </CardContent>
        </Card>
      </div>

    </>
  )
}
