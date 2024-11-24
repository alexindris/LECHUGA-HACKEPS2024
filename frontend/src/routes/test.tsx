import * as React from 'react'
import { createFileRoute } from '@tanstack/react-router'
import { useUserStore } from '@/stores/storeProvider';
import { observer } from 'mobx-react-lite';

export const Route = createFileRoute('/test')({
  component: observer(RouteComponent),
})


function RouteComponent() {
  const userStore = useUserStore();

  return (
    <>
      <h1>Test</h1>
      <p>{userStore.userToken}</p>
    </>
  )
}
