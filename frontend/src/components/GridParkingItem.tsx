

type GridParkingItemProps = {
  title: string;
  occupation: string;
}

export function GridParkingItem({ title, occupation }: Readonly<GridParkingItemProps>) {
  return (
    <div className='flex flex-col w-full h-full p-5 bg-sky-100 items-center justify-center gap-4'>
      <span className='text-sky-700 text-3xl font-semibold text-center'>{title}</span>
      <div className='bg-sky-200 w-full  rounded-[4.7rem]'>
        <img src="/parking.png" alt="Parking" className='p-2' />
      </div>
      <div className='bg-sky-800 rounded-3xl p-2'>
        <span className='text-white text-3xl'>Occupation: {occupation}</span>
      </div>
    </div>
  )
}