import { createFileRoute } from "@tanstack/react-router";
import { GET_HEALTH } from "@/lib/api";
import { useQuery } from "@apollo/client";
import { observer } from "mobx-react-lite";
import { useParkingStore, useUserStore } from '@/stores/storeProvider';

const AboutComponent = observer(() => {
  const { data } = useQuery(GET_HEALTH);

  console.log(data);
  const userStore = useUserStore();
  const parkingStore = useParkingStore();

  return (
    <div className='p-2'>
      <h3>About</h3>
      <p>Status: {data && data.health.status}</p>
      <p>Time: {data && data.health.time}</p>
      <h3>Parkings</h3>
      {parkingStore.parkings.map((parking) => (
        <p key={parking.id}>{parking.displayDetails()}</p>
      ))}
      <h3>User</h3>
      <p>Token: {userStore.userToken}</p>
      {/* Input that changes userToken */}
      <input
        type='text'
        value={userStore.userToken ?? ''}
        onChange={(e) => userStore.setToken(e.target.value)}
      />
    </div>
  );
});

export const Route = createFileRoute("/about")({
  component: AboutComponent,
});
