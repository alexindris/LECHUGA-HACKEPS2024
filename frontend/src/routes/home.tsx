import { GridParkingItem } from '@/components/GridParkingItem';
import SimpleNav from '@/components/SimpleNav';
import { Button } from '@/components/ui/button';
import { useParkingStore } from '@/stores/storeProvider';
import { useNavigate } from '@tanstack/react-router';
import { LuPlus } from "react-icons/lu";
import { observer } from "mobx-react-lite";
import { createProtectRoute } from '@/lib/protectRoute';

const RouteComponent = observer(() => {
  const parkingStore = useParkingStore();
  const navigator = useNavigate();

  if (parkingStore.parkings.length === 0) {
    parkingStore.getAllParkings()
  }


  return (
    <div className='flex flex-col h-screen w-full bg-sky-100'>
      <SimpleNav disabledParkingTab={true} />
      <div className='h-full w-full flex flex-col items-center'>
        <div className='bg-sky-700 w-full h-[30rem] items-center justify-center flex gap-14'>
          <span className='text-5xl font-bold text-white text-center'>
            Add new
            <br />
            parking
            <br />
            <Button
              className='text-lg font-bold text-black border-2 text-center  border-sky-200 bg-sky-100 '
              onClick={() => navigator({ to: '/parking/new' })}
            >
              <LuPlus size={70} />
            </Button>
          </span>
          <img src="/parking.png" alt="Home Background" />
        </div>
        <div className='flex h-h-screen w-full p-10 flex-col bg-sky-100'>
          <span className='text-sky-800 text-5xl w-full text-center font-semibold mb-4'>My Parkings</span>
          <div className='grid justify-between w-full h-full gap-10 md:grid-cols-4 sm:grid-cols-1'>
            {parkingStore.parkings.map((parking) => {
              if (!parking) return;
              return <GridParkingItem key={parking.identifier} title={parking.name} occupation={parking.occupiedLots + '/' + parking.totalLots} />
            })}
          </div>
        </div>
      </div >
    </div >
  )
});

export const Route = createProtectRoute({
  path: "/home",
  component: RouteComponent,
});
