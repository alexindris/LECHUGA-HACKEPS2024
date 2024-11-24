import * as React from 'react'
import { createFileRoute } from '@tanstack/react-router'
import { observer } from 'mobx-react-lite';
import { Input } from '@/components/ui/input';
import { useUserStore } from '@/stores/storeProvider';



const RouteComponent = observer(() => {
  const userStore = useUserStore();

  return (
    <>
      User token: {userStore.userToken}
      <Input value={userStore.userToken ?? ''} onChange={(e) => userStore.setToken(e.target.value)} />
    </>
  )
}

);

export const Route = createFileRoute('/test')({
  component: RouteComponent,
})