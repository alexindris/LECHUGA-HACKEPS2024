import { createFileRoute } from "@tanstack/react-router";
import { GET_HEALTH } from "@/lib/api";
import { useQuery } from "@apollo/client";
import { useCounterStore } from "@/stores/storeProvider";
import { observer } from "mobx-react-lite";

const AboutComponent = observer(() => {
  const { data } = useQuery(GET_HEALTH);

  console.log(data);
  const counterStore = useCounterStore();

  return (
    <div className='p-2'>
      <h3>About</h3>
      <p>Status: {data && data.health.status}</p>
      <p>Time: {data && data.health.time}</p>
      <h1>Count: {counterStore.count}</h1>
      <button
        onClick={() => {
          console.log(counterStore.count);
          counterStore.increment();
        }}
      >
        Increment
      </button>
      <button onClick={() => counterStore.decrement()}>Decrement</button>
    </div>
  );
});

export const Route = createFileRoute("/about")({
  component: AboutComponent,
});
